import streamlit as st
import requests
import pandas as pd
import json
import langchain
import langgraph
import langsmith
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from langgraph.graph import StateGraph
from langgraph.checkpoint.memory import MemorySaver
from langsmith import Client

# ==================================
# 📌 CONFIGURACIÓN INICIAL
# ==================================
# Configuración de LangSmith para monitoreo
client = Client(api_key="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")

# Configuración de la base de datos vectorial
persist_directory = "db"
embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma(persist_directory=persist_directory, collection_name="skyrim-combined", embedding_function=embedding_function)

# Configuración de LM Studio
LM_STUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"
HEADERS = {"Content-Type": "application/json"}

# ==================================
# 📌 FUNCIONES DE BÚSQUEDA Y RESPUESTA
# ==================================
def buscar_en_bd_vectorial(consulta: str, usar_score: bool = False) -> str:
    """Realiza búsqueda en la base de datos vectorial."""
    try:
        if usar_score:
            results = db.similarity_search_with_score(consulta, k=3)
            contexto = []
            for doc, score in results:
                desc = doc.metadata.get("descripcion", "Sin contexto relevante")
                contexto.append(f"[Score: {score:.4f}] {desc}")
            return "\n".join(contexto)
        else:
            results = db.similarity_search(consulta, k=3)
            return "\n".join([r.metadata.get("descripcion", "Sin contexto relevante") for r in results])
    except Exception as e:
        return f"Error en la búsqueda vectorial: {str(e)}"

def generar_respuesta_llm(prompt: str) -> str:
    """Genera respuesta usando LM Studio."""
    payload = {
        "model": "deepseek-coder-v2-lite-instruct",
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post(LM_STUDIO_URL, json=payload, headers=HEADERS)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"⚠️ Error al conectar con LM Studio: {e}"

# ==================================
# 📌 INTEGRACIÓN CON LANGGRAPH
# ==================================
class ChatState:
    def __init__(self, pregunta: str, usar_score: bool = False, solo_bd: bool = True):
        self.pregunta = pregunta
        self.usar_score = usar_score
        self.solo_bd = solo_bd
        self.contexto = ""
        self.respuesta = ""


def obtener_contexto(state: dict) -> dict:
    with langsmith.trace("busqueda_vectorial") as trace:
        contexto = buscar_en_bd_vectorial(state["pregunta"], state["usar_score"])
        trace.add_metadata({"tipo_busqueda": "con_score" if state["usar_score"] else "normal"})
        state["contexto"] = contexto
    return state


def generar_respuesta_con_contexto(state: dict) -> dict:
    with langsmith.trace("generacion_respuesta") as trace:
        if state["solo_bd"]:
            prompt = f"Pregunta: {state['pregunta']}\nContexto: {state['contexto']}\nRespuesta:"
        else:
            prompt = state["pregunta"]
        respuesta = generar_respuesta_llm(prompt)
        trace.add_metadata({"tipo_respuesta": "con_contexto" if state["solo_bd"] else "directa"})
        state["respuesta"] = respuesta
    return state


def create_chat_graph():
    graph = StateGraph()
    graph.add_node("obtener_contexto", obtener_contexto)
    graph.add_node("generar_respuesta", generar_respuesta_con_contexto)
    graph.set_entry_point("obtener_contexto")
    graph.add_edge("obtener_contexto", "generar_respuesta")
    return graph.compile()


def mostrar_interfaz_chat():
    st.header("💬 Habla con el Agente")
    consulta = st.text_input("Escribe tu pregunta:")
    col1, col2 = st.columns(2)

    with col1:
        fuente_buscada = st.radio("Fuente de búsqueda:", ("Solo en la base de datos", "Búsqueda directa con IA"))

    with col2:
        tipo_buscada = st.radio("Tipo de búsqueda vectorial:", ("Normal", "Con Score"))

    if st.button("Enviar") and consulta:
        with st.spinner("Procesando tu consulta..."):
            graph = create_chat_graph()
            usar_score = tipo_buscada == "Con Score"
            solo_bd = fuente_buscada == "Solo en la base de datos"
            initial_state = {
                "pregunta": consulta,
                "usar_score": usar_score,
                "solo_bd": solo_bd,
                "contexto": "",
                "respuesta": ""
            }
            final_state = graph.invoke(initial_state)
            st.write("🧠 Respuesta de la IA:")
            if solo_bd and usar_score:
                st.write("📊 Contexto encontrado (con puntuaciones):")
                st.write(final_state["contexto"])
            st.write(final_state["respuesta"])

# ==================================
# 📌 FUNCIONES DE CARGA DE DATOS
# ==================================
def cargar_datos_personajes():
    """Carga datos de personajes desde CSV y JSON."""
    try:
        df = pd.read_csv("data/Skyrim_Named_Characters_Propio.csv")
        with open("data/skyrim_images.json") as f:
            images_data = json.load(f)
        return df, images_data
    except Exception as e:
        st.error(f"Error al cargar datos: {str(e)}")
        return None, None

# ==================================
# 📌 INTERFACES DE USUARIO
# ==================================
def mostrar_interfaz_chat():
    """Muestra la interfaz de chat."""
    st.header("💬 Habla con el Agente")
    
    # Configuración de la consulta
    consulta = st.text_input("Escribe tu pregunta:")
    col1, col2 = st.columns(2)
    
    with col1:
        fuente_buscada = st.radio(
            "Fuente de búsqueda:",
            ("Solo en la base de datos", "Búsqueda directa con IA")
        )
    
    with col2:
        tipo_buscada = st.radio(
            "Tipo de búsqueda vectorial:",
            ("Normal", "Con Score")
        )
    
    if st.button("Enviar") and consulta:
        with st.spinner("Procesando tu consulta..."):
            # Crear y ejecutar el grafo
            graph = create_chat_graph()
            usar_score = tipo_buscada == "Con Score"
            solo_bd = fuente_buscada == "Solo en la base de datos"
            
            initial_state = ChatState(consulta, usar_score, solo_bd)
            final_state = graph.invoke(initial_state)
            
            # Mostrar resultados
            st.write("🧠 Respuesta de la IA:")
            if solo_bd and usar_score:
                st.write("📊 Contexto encontrado (con puntuaciones):")
                st.write(final_state.contexto)
            st.write(final_state.respuesta)

def mostrar_interfaz_personajes():
    """Muestra la interfaz de búsqueda de personajes."""
    st.header("🔍 Filtrar Personajes")
    
    # Cargar datos
    df, images_data = cargar_datos_personajes()
    if df is None:
        return
    
    # Filtros en columnas
    col1, col2, col3 = st.columns(3)
    
    with col1:
        raza = st.selectbox("Raza", ["Todas"] + sorted(df['Race'].unique().tolist()))
    with col2:
        genero = st.selectbox("Género", ["Todos"] + sorted(df['Gender'].unique().tolist()))
    with col3:
        clase = st.selectbox("Clase", ["Todas"] + sorted(df['Class'].unique().tolist()))
    
    # Aplicar filtros
    filtered_df = df.copy()
    if raza != "Todas":
        filtered_df = filtered_df[filtered_df['Race'] == raza]
    if genero != "Todos":
        filtered_df = filtered_df[filtered_df['Gender'] == genero]
    if clase != "Todas":
        filtered_df = filtered_df[filtered_df['Class'] == clase]
    
    # Mostrar resultados
    st.write("### Resultados de la búsqueda:")
    
    if not filtered_df.empty:
        # Tabla de resultados
        columns_to_show = ['Name', 'Home City', 'House', 'Race', 'Gender', 'Level', 
                          'Class', 'Primary Skills', 'Faction(s)', 'Location']
        st.dataframe(filtered_df[columns_to_show])
        
        # Detalles del personaje seleccionado
        selected_personaje_name = st.selectbox(
            "Selecciona un personaje para más detalles:",
            filtered_df['Name'].tolist()
        )
        
        if selected_personaje_name:
            col1, col2 = st.columns([1, 2])
            
            # Buscar imagen y datos del personaje
            personaje_image = next(
                (item for item in images_data if item["Name"] == selected_personaje_name),
                None
            )
            selected_personaje = filtered_df[
                filtered_df['Name'] == selected_personaje_name
            ].iloc[0]
            
            # Mostrar imagen
            with col1:
                if personaje_image:
                    st.image(personaje_image["Image"], caption=selected_personaje_name)
            
            # Mostrar detalles
            with col2:
                st.subheader(f"📖 Detalles de {selected_personaje_name}")
                st.write(f"**Ciudad:** {selected_personaje['Home City']}")
                st.write(f"**Raza:** {selected_personaje['Race']}")
                st.write(f"**Género:** {selected_personaje['Gender']}")
                st.write(f"**Nivel:** {selected_personaje['Level']}")
                st.write(f"**Clase:** {selected_personaje['Class']}")
                st.write(f"**Habilidades:** {selected_personaje['Primary Skills']}")
                st.write(f"**Facción:** {selected_personaje['Faction(s)']}")
                st.write(f"**Ubicación:** {selected_personaje['Location']}")
                
                if personaje_image:
                    st.markdown(f"🔗 [Ver en Wiki]({personaje_image['Source']})")
    else:
        st.warning("⚠️ No se encontraron personajes con los filtros seleccionados.")

# ==================================
# 📌 FUNCIÓN PRINCIPAL
# ==================================
def main():
    st.title("🔹 Chatbot Skyrim con RAG y LangChain")
    
    # Menú principal
    opcion = st.sidebar.radio("Selecciona una opción", ["Chat con IA", "Buscar Personajes"])
    
    if opcion == "Chat con IA":
        mostrar_interfaz_chat()
    else:
        mostrar_interfaz_personajes()

if __name__ == "__main__":
    main()