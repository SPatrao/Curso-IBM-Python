import pandas as pd
import logging
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores.chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_data(file_path):
    """Carga datos desde un archivo CSV o JSON y los devuelve como una lista de diccionarios."""
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.json'):
            df = pd.read_json(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_path}")
        
        df = df.fillna('')  # Rellenar valores nulos
        return df.to_dict(orient='records')
    except Exception as e:
        logger.error(f"Error loading data from {file_path}: {str(e)}")
        raise

def create_embeddings(data, text_key="Description", collection_name="skyrim-knowledge"):
    """Crea embeddings y los guarda en una base de datos vectorial."""
    try:
        if not data:
            raise ValueError("Empty data provided")
            
        if not all(text_key in item for item in data):
            raise ValueError(f"Key '{text_key}' missing in some data items")
        
        # Preparar los textos para crear los embeddings
        texts = [str(item[text_key]) for item in data]
        
        # Dividir los textos en chunks
        text_splitter = CharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
            separator="\n"
        )
        
        docs = text_splitter.split_text("\n".join(texts))
        logger.info(f"Created {len(docs)} text chunks")
        
        # Crear embeddings usando HuggingFace
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'}
        )
        
        # Crear la base de datos vectorial con Chroma
        db = Chroma.from_texts(
            texts=docs,
            embedding=embeddings,
            collection_name=collection_name,
            persist_directory="db"
        )
        
        logger.info("Embeddings created and saved to vector database.")
        return db
    except Exception as e:
        logger.error(f"Error creating embeddings: {str(e)}")
        raise

def save_to_vector_db():
    """Carga datos, genera descripciones y guarda embeddings en la base de datos vectorial."""
    try:
        # Cargar los datos desde los archivos CSV y JSON
        books_data = load_data("data/skyrim_books.csv")
        characters_data = load_data("data/Skyrim_Named_Characters_Propio.csv")
        images_data = {item['Name']: item for item in load_data("data/skyrim_images.json")}  # Mapear por nombre

        # Preprocesar los datos de libros
        for book in books_data:
            book["Description"] = (
                f"'{book.get('Title', 'Desconocido')}' tiene un precio de {book.get('Cost', 'Desconocido')}, "
                f"fue escrito por {book.get('Author', 'Desconocido')}. "
                f"Resumen: {book.get('Description', 'Sin descripción.')}. "
                f"Su lectura produce subida de habilidad '{book.get('Skill', 'ninguna')}'."
            )

        # Preprocesar los datos de personajes
        for character in characters_data:
            character["Description"] = (
                f"{character.get('Name', 'Desconocido')} es un {character.get('Gender', 'ser')} "
                f"de la raza {character.get('Race', 'desconocida')}. "
                f"Vive en {character.get('Home City', 'lugar desconocido')} "
                f"en su casa {character.get('House', 'desconocida')}. "
                f"Su clase es {character.get('Class', 'indefinida')}. "
                f"Sus habilidades principales son {character.get('Primary Skills', 'desconocidas')}. "
                f"Su moralidad es {character.get('Morality', 'indefinida')}, "
                f"así que ten cuidado porque es {character.get('Aggression', 'desconocido')}. "
                f"Pertenece a la Facción de {character.get('Faction(s)', 'ninguna')}. "
                f"{f'Se rumorea que {character.get('Race Details')}' if character.get('Race Details') else ''} "
                f"Sus estadísticas son: Vida {character.get('Health (PC=10)', 'desconocida')}, "
                f"Magia {character.get('Magicka (PC=10)', 'desconocida')} y "
                f"Aguante {character.get('Stamina (PC=10)', 'desconocido')}."
            )
            
            # Agregar imagen si está disponible
            image_data = images_data.get(character['Name'])
            if image_data:
                character["Description"] += (
                    f"\n\nPuedes ver su imagen aquí: {image_data.get('Image', 'Sin imagen disponible')}. "
                    f"Fuente: {image_data.get('Source', 'Sin fuente disponible')}"
                )
        
        # Combinar los datos de libros y personajes
        all_data = books_data + characters_data
        
        # Crear embeddings y guardarlos en la base de datos
        db = create_embeddings(all_data, collection_name="skyrim-combined")
        logger.info("Datos guardados correctamente en la base de datos vectorial.")
    
    except Exception as e:
        logger.error(f"Error en save_to_vector_db: {str(e)}")
        
if __name__ == "__main__":
    save_to_vector_db()
