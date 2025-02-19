import subprocess
import time
import os
import sys

def install_dependencies():
    print("Installing dependencies...")
    dependencies = [
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "streamlit",
        "requests",
        "sentence-transformers",
        "faiss-cpu"
    ]
    for dep in dependencies:
        subprocess.check_call([sys.executable, "-m", "pip", "install", dep])

def run_python_script(script_path):
    subprocess.run([sys.executable, script_path], check=True)

def check_lm_studio():
    try:
        import requests
        url = "http://localhost:1234/v1/models"
        response = requests.get(url)
        if response.status_code == 200:
            print("LM Studio is running and accessible.")
            return True
    except:
        print("LM Studio is not running or not accessible.")
    return False

def main():
    # Cambiar al directorio del script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
       
    print("Setting up Skyrim RAG system...")

    # Instalar dependencias
    install_dependencies()

    # Preparar los datos
    print("Preparing data...")
    run_python_script("src/data_preparation.py")

    # Crear el índice FAISS
    print("Creating FAISS index...")
    run_python_script("src/indexing.py")

    # Verificar LM Studio
    print("Checking LM Studio...")
    if not check_lm_studio():
        print("Please start LM Studio and ensure it's running on http://localhost:1234")
        print("Press Enter when LM Studio is ready...")
        input()

    # Iniciar la aplicación Streamlit
    print("Starting Streamlit application...")
    os.system(f"{sys.executable} -m streamlit run app.py")

if __name__ == "__main__":
    main()
    

