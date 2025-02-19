import streamlit as st
import pandas as pd
from src.retrieval import load_index_and_data, search
from src.generation import generate_prompt, generate_response

# Cargar datos e índice
index, df, model = load_index_and_data()

st.title("Skyrim RAG System")

query = st.text_input("Ask a question about Skyrim:")

if query:
    with st.spinner("Searching and generating response..."):
        try:
            results = search(query, index, df, model)
            
            st.subheader("Relevant Information:")
            for _, row in results.iterrows():
                st.write(f"- {row['text']}")
            
            prompt = generate_prompt(query, results)
            response = generate_response(prompt)
            
            st.subheader("Answer:")
            st.write(response)
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Filtros
st.sidebar.header("Filters")
races = ['All'] + sorted(df['Race'].unique().tolist())
classes = ['All'] + sorted(df['Class'].unique().tolist())

selected_race = st.sidebar.selectbox("Select Race", races)
selected_class = st.sidebar.selectbox("Select Class", classes)

if selected_race != 'All' or selected_class != 'All':
    filtered_df = df
    if selected_race != 'All':
        filtered_df = filtered_df[filtered_df['Race'] == selected_race]
    if selected_class != 'All':
        filtered_df = filtered_df[filtered_df['Class'] == selected_class]
    st.subheader("Filtered Characters:")
    st.write(filtered_df[['Name', 'Race', 'Class', 'Location']])

# Sistema de retroalimentación
if st.button("This response was helpful"):
    st.success("Thank you for your feedback!")

if st.button("This response was not helpful"):
    st.warning("We're sorry the response wasn't helpful. We'll work on improving it.")

