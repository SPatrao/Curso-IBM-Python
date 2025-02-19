import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer

def load_index_and_data():
    index = faiss.read_index('../data/skyrim_index.faiss')
    df = pd.read_csv('../data/prepared_skyrim_data.csv')
    model = SentenceTransformer('../data/sentence_transformer_model')
    return index, df, model

def search(query, index, df, model, k=5):
    query_vector = model.encode([query])
    D, I = index.search(query_vector.astype('float32'), k)
    results = df.iloc[I[0]]
    return results

if __name__ == '__main__':
    index, df, model = load_index_and_data()
    results = search("Tell me about Nord warriors", index, df, model)
    print(results['text'].tolist())

