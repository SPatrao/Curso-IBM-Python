import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def create_faiss_index(df, column='text'):
    """
    Crea un índice FAISS a partir de los datos preparados.
    """
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(df[column].tolist())
    
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings.astype('float32'))
    
    return index, model

if __name__ == '__main__':
    df = pd.read_csv('../data/prepared_skyrim_data.csv')
    index, model = create_faiss_index(df)
    faiss.write_index(index, '../data/skyrim_index.faiss')
    model.save('../data/sentence_transformer_model')

