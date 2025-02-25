import streamlit as st
import requests
import pandas as pd
import json
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langgraph.graph import StateGraph
from langgraph.checkpoint.memory import MemorySaver
import langsmith

# ============================
# 🔹 CONFIGURACIÓN DE BASE DE DATOS VECTORIAL
# ============================
# Se usa Chroma como base de datos vectorial para almacenar y buscar información relacionada con Skyrim.
# HuggingFaceEmbeddings se utiliza para transformar texto en vectores numéricos que facilitan la búsqueda semántica.

persist_directory = "db"
embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma(persist_directory=persist_directory, collection_name="skyrim-combined", embedding_function=embedding_function)

# ============================
# 🔹 CONFIGURACIÓN DE LM STUDIO (MODELO DE LENGUAJE LOCAL)
# ============================
# LM Studio es un servidor local que permite hacer consultas a modelos de lenguaje (LLMs) sin depender de la nube.

LM_STUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"
HEADERS = {"Content-Type": "application/json"}

# Función para generar respuestas usando el modelo de LM Studio
def generar_respuesta(prompt):
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

# ============================
# 🔹 INTEGRACIÓN DE LangGraph PARA MANEJO DE DIÁLOGOS
# ============================
# LangGraph nos permite estructurar mejor las respuestas del chatbot definiendo flujos de conversación.

# Definimos un estado del chatbot donde guardamos la pregunta y el contexto
class ChatState:
    def __init__(self, pregunta):
        self.pregunta = pregunta
        self.contexto = ""
        self.respuesta = ""

# Función para obtener contexto desde la base de datos vectorial
def obtener_contexto(state: ChatState):
    results = db.similarity_search(state.pregunta, k=3)
    state.contexto = "\n".join([r.metadata.get("descripcion", "Sin contexto relevante") for r in results])
    return state

# Función para generar respuesta con el modelo de lenguaje
def generar_respuesta_con_contexto(state: ChatState):
    prompt = f"Pregunta: {state.pregunta}\nContexto: {state.contexto}\nRespuesta:"
    state.respuesta = generar_respuesta(prompt)
    return state

# Creación del flujo de conversación con LangGraph
graph = StateGraph(ChatState)
graph.add_node("obtener_contexto", obtener_contexto)
graph.add_node("generar_respuesta", generar_respuesta_con_contexto)

graph.set_entry_point("obtener_contexto")
graph.add_edge("obtener_contexto", "generar_respuesta")

graph = graph.compile(checkpointer=MemorySaver())

# ============================
# 🔹 INTERFAZ DE USUARIO CON STREAMLIT
# ============================
st.title("🔹 Chatbot Skyrim con BD Vectorial y LangGraph")

opcion = st.sidebar.radio("Selecciona una opción", ["Chat con IA", "Buscar Personajes"])




if opcion == "Chat con IA":
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
    
    if st.button("Enviar"):
        
        if consulta:
            # Si la opción seleccionada es "Buscar en internet también"
            if fuente_buscada == "Buscar en internet también":
                # Enviar la consulta a LM Studio para buscar en internet
                if tipo_buscada == "Normal":
                    # Realizar la búsqueda de similitud normal
                    results = db.similarity_search(consulta, k=3)  
                    contexto = "\n".join([r.metadata.get("descripcion", "Sin contexto relevante") for r in results]) if results else "Sin contexto relevante"
                else:
                    # Realizar la búsqueda de similitud con puntuaciones
                    results = db.similarity_search_with_score(consulta, k=3) 
                    # Aquí se espera que los resultados sean tuplas, así que lo manejamos en consecuencia
                    contexto = "\n".join([r[0].metadata.get("descripcion", "Sin contexto relevante") for r in results]) if results else "Sin contexto relevante"
                    
                # Enviar la consulta y contexto a LM Studio (solo con la base de datos)
                prompt = f"Pregunta: {consulta}\nContexto: {contexto}\nRespuesta:"
                respuesta = generar_respuesta(prompt)
                
                #state = ChatState(consulta)
                #state = graph.invoke(state)

                st.write("🧠 Respuesta de la IA (Internet + BD):")
                st.write(respuesta)
            else:
                # Buscar solo en la base de datos vectorial
                if tipo_buscada == "Normal":
                    # Realizar la búsqueda de similitud normal
                    results = db.similarity_search(consulta, k=3)  
                    contexto = "\n".join([r.metadata.get("descripcion", "Sin contexto relevante") for r in results]) if results else "Sin contexto relevante"
                else:
                    # Realizar la búsqueda de similitud con puntuaciones
                    results = db.similarity_search_with_score(consulta, k=3) 
                    # Aquí se espera que los resultados sean tuplas, así que lo manejamos en consecuencia
                    contexto = "\n".join([r[0].metadata.get("descripcion", "Sin contexto relevante") for r in results]) if results else "Sin contexto relevante"
                    
                # Enviar la consulta y contexto a LM Studio (solo con la base de datos)
                prompt = f"Pregunta: {consulta}\nContexto: {contexto}\nRespuesta:"
                respuesta = generar_respuesta(prompt)

                #state = ChatState(consulta)
                #state = graph.invoke(state)

                st.write("🧠 Respuesta de la IA (Solo BD Vectorial):")
                st.write(respuesta)


elif opcion == "Buscar Personajes":
    st.header("🔍 Filtrar Personajes")
    
    # Cargar datos de personajes
    csv_file = "data/Skyrim_Named_Characters_Propio.csv"
    df = pd.read_csv(csv_file)
    
    # Filtrar opciones
    raza_opciones = ["Todas"] + sorted(df['Race'].unique().tolist())
    genero_opciones = ["Todos"] + sorted(df['Gender'].unique().tolist())
    clase_opciones = ["Todas"] + sorted(df['Class'].unique().tolist())
    
    raza = st.selectbox("Selecciona una raza", raza_opciones)
    genero = st.selectbox("Selecciona un género", genero_opciones)
    clase = st.selectbox("Selecciona una clase", clase_opciones)

    # Filtrar personajes
    filtered_df = df.copy()
    if raza != "Todas":
        filtered_df = filtered_df[filtered_df['Race'] == raza]
    if genero != "Todos":
        filtered_df = filtered_df[filtered_df['Gender'] == genero]
    if clase != "Todas":
        filtered_df = filtered_df[filtered_df['Class'] == clase]

    st.write("### Resultados de la búsqueda:")
    
    if not filtered_df.empty:
        selected_personaje_name = st.selectbox("Selecciona un personaje", filtered_df['Name'].tolist())
        selected_personaje = filtered_df[filtered_df['Name'] == selected_personaje_name].iloc[0]

        # Mostrar la tabla de resultados
        filtered_df_display = filtered_df[['Name', 'Home City', 'House', 'Race', 'Gender', 'Level', 'Class', 'Primary Skills', 'Faction(s)', 'Location']]

        # Convertir la tabla a una tabla interactiva con Streamlit
        selected_rows = st.dataframe(filtered_df_display)
        
        # Obtener los datos del personaje seleccionado
        selected_personaje = filtered_df[filtered_df['Name'] == selected_personaje_name].iloc[0]

        personaje_name = selected_personaje['Name']
        
        # Cargar imágenes y enlaces de wiki desde JSON
        json_file = "data/skyrim_images.json"
        with open(json_file) as f:
            images_data = json.load(f)
        
        wiki_link = None
        image_link = None
        for item in images_data:
            if item["Name"] == personaje_name:
                wiki_link = item["Source"]
                image_link = item["Image"]
                break
        
        if wiki_link and image_link:
            st.markdown(f"### Detalles del Personaje: {personaje_name}")
            st.markdown(f"🔗 [Wiki - {personaje_name}]({wiki_link})")
            st.image(image_link, caption=personaje_name, use_container_width=True)
    else:
        st.write("⚠️ No se encontraron personajes con esos filtros.")
