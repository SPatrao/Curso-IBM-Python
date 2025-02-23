import streamlit as st
import requests
import pandas as pd
import json
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# 🔹 Configuración de la base de datos vectorial
persist_directory = "db"
embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma(persist_directory=persist_directory, collection_name="skyrim-combined", embedding_function=embedding_function)

# 🔹 Configuración de LM Studio
LM_STUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"
HEADERS = {"Content-Type": "application/json"}

# 🔹 Función para conectar con LM Studio
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

# 🔹 Cargar datos del CSV y JSON
csv_file = "data/Skyrim_Named_Characters_Propio.csv"
json_file = "data/skyrim_images.json"

# Cargar CSV de personajes
df = pd.read_csv(csv_file)

# Cargar JSON de imágenes
with open(json_file) as f:
    images_data = json.load(f)

# 🔹 Interfaz con Streamlit
st.title("🔹 Chatbot Skyrim con BD Vectorial")

# Sidebar para selección de función
opcion = st.sidebar.radio("Selecciona una opción", ["Chat con IA", "Buscar Personajes"])

if opcion == "Chat con IA":
    st.header("💬 Habla con el Agente")
    consulta = st.text_input("Escribe tu pregunta:")
    
    # Añadir una opción para seleccionar la fuente de búsqueda
    fuente_buscada = st.radio(
        "Selecciona la fuente de búsqueda:",
        ("Solo en la base de datos", "Buscar en internet también")
    )
    tipo_buscada = st.radio(
        "Selecciona el tipo de búsqueda:",
        ("Normal", "Con Score")
    )
    
    if st.button("Enviar"):
        if consulta:
            # Si la opción seleccionada es "Buscar en internet también"
            if fuente_buscada == "Buscar en internet también":
                # Enviar la consulta a LM Studio para buscar en internet
                respuesta = generar_respuesta(consulta)
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
                st.write("🧠 Respuesta de la IA (Solo BD Vectorial):")
                st.write(respuesta)

elif opcion == "Buscar Personajes":
    st.header("🔍 Filtrar Personajes")
    
    # 🔹 Filtrar las opciones de búsqueda basadas en los valores únicos del CSV
    raza_opciones = ["Todas"] + sorted(df['Race'].unique().tolist())
    genero_opciones = ["Todos"] + sorted(df['Gender'].unique().tolist())
    clase_opciones = ["Todas"] + sorted(df['Class'].unique().tolist())
    
    # 🔹 Filtros de búsqueda
    raza = st.selectbox("Selecciona una raza", raza_opciones)
    genero = st.selectbox("Selecciona un género", genero_opciones)
    clase = st.selectbox("Selecciona una clase", clase_opciones)

    # 🔹 Filtrar personajes según los filtros seleccionados
    filtered_df = df.copy()

    if raza != "Todas":
        filtered_df = filtered_df[filtered_df['Race'] == raza]
    if genero != "Todos":
        filtered_df = filtered_df[filtered_df['Gender'] == genero]
    if clase != "Todas":
        filtered_df = filtered_df[filtered_df['Class'] == clase]

    # 🔹 Mostrar resultados en una tabla con las columnas seleccionadas
    st.write("### Resultados de la búsqueda:")

    if not filtered_df.empty:
        # Mostrar la tabla de resultados
        filtered_df_display = filtered_df[['Name', 'Home City', 'House', 'Race', 'Gender', 'Level', 'Class', 'Primary Skills', 'Faction(s)', 'Location']]
        
        # Convertir la tabla a una tabla interactiva con Streamlit
        selected_rows = st.dataframe(filtered_df_display)
        
        # Convertir la tabla a una tabla interactiva con Streamlit
        selected_personaje_name = st.selectbox("Selecciona un personaje", filtered_df['Name'].tolist())

        # Obtener los datos del personaje seleccionado
        selected_personaje = filtered_df[filtered_df['Name'] == selected_personaje_name].iloc[0]
        personaje_name = selected_personaje['Name']
        wiki_link = None
        image_link = None
        
        # Buscar el enlace de la wiki y la imagen en el JSON
        for item in images_data:
            if item["Name"] == personaje_name:
                wiki_link = item["Source"]
                image_link = item["Image"]
                break
        
        # Mostrar detalles del personaje seleccionado
        if wiki_link and image_link:
            st.markdown(f"### Detalles del Personaje: {personaje_name}")
            st.markdown(f"🔗 [Wiki - {personaje_name}]({wiki_link})")
            st.image(image_link, caption=personaje_name, use_container_width=True)  # Cambiado a use_container_width=True

    else:
        st.write("⚠️ No se encontraron personajes con esos filtros.")
