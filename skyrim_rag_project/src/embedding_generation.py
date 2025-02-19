# src/embedding_generation.py

# Importamos las bibliotecas necesarias para nuestro script
import pandas as pd  # Para manejar y analizar datos estructurados
import numpy as np  # Para operaciones numéricas eficientes
from transformers import AutoTokenizer, AutoModel  # Para cargar modelos de lenguaje pre-entrenados
import torch  # Biblioteca de aprendizaje profundo para cálculos tensoriales

# Cargamos el dataset limpio desde un archivo CSV
# Asumimos que este archivo contiene datos de Skyrim ya procesados y listos para su uso
df_clean = pd.read_csv('../data/skyrim_data_clean.csv')

# Cargamos el modelo de lenguaje BERT y su tokenizador correspondiente
# BERT (Bidirectional Encoder Representations from Transformers) es un modelo de lenguaje
# pre-entrenado que puede generar representaciones contextuales de palabras
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
model = AutoModel.from_pretrained('bert-base-uncased')

# Definimos una función para generar embeddings a partir de texto
def get_embedding(text):
    """
    Esta función toma un texto como entrada y devuelve su embedding (representación vectorial).
    
    Argumentos:
    text (str): El texto del cual queremos obtener el embedding.
    
    Retorna:
    numpy.ndarray: Un vector numpy que representa el embedding del texto.
    """
    # Tokenizamos el texto y lo preparamos para el modelo
    # 'return_tensors='pt'' indica que queremos tensores PyTorch como salida
    # 'truncation=True' y 'max_length=512' limitan la longitud del texto a 512 tokens
    # 'padding=True' asegura que todas las secuencias tengan la misma longitud
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    
    # Utilizamos un context manager 'with torch.no_grad():' para desactivar el cálculo de gradientes
    # Esto es útil cuando solo estamos haciendo inferencia y no entrenamiento
    with torch.no_grad():
        # Pasamos los inputs por el modelo
        outputs = model(**inputs)
    
    # Tomamos la media de la última capa oculta para obtener una representación del texto completo
    # .mean(dim=1) toma la media a lo largo de la dimensión de los tokens
    # .squeeze() elimina las dimensiones de tamaño 1
    # .numpy() convierte el tensor de PyTorch a un array de NumPy
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

# Definimos una función para generar embeddings para todo el dataset
def generate_embeddings(df):
    """
    Esta función genera embeddings para cada entrada en el DataFrame proporcionado.
    
    Argumentos:
    df (pandas.DataFrame): El DataFrame que contiene los textos para los cuales queremos generar embeddings.
    
    Retorna:
    numpy.ndarray: Un array 2D de NumPy donde cada fila es el embedding de una entrada del DataFrame.
    """
    print("Generando embeddings...")
    embeddings = []
    
    # Iteramos sobre cada texto en la columna 'SearchText' del DataFrame
    for text in df['SearchText']:
        # Obtenemos el embedding para cada texto
        embedding = get_embedding(text)
        # Añadimos el embedding a nuestra lista
        embeddings.append(embedding)
    
    # Convertimos la lista de embeddings a un array de NumPy
    # Esto nos da una matriz 2D donde cada fila es un embedding
    embeddings_array = np.array(embeddings)
    
    print("Embeddings generados. Forma del array de embeddings:", embeddings_array.shape)
    return embeddings_array

# Este bloque se ejecuta solo si este script se ejecuta directamente (no si se importa como módulo)
if __name__ == "__main__":
    # Generamos los embeddings para nuestro dataset limpio
    embeddings = generate_embeddings(df_clean)
    
    # Guardamos los embeddings en un archivo .npy para su uso posterior
    # Los archivos .npy son un formato eficiente para guardar arrays de NumPy
    np.save('../data/skyrim_embeddings.npy', embeddings)

# Nota: Este script asume que existe una columna 'SearchText' en df_clean
# que contiene el texto para el cual queremos generar embeddings.
# Asegúrate de que esta columna existe y contiene la información relevante.

