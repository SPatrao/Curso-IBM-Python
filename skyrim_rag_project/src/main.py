import subprocess
import sys
import importlib

def verificar_e_instalar_dependencias():
    with open('requirements.txt', 'r') as archivo:
        bibliotecas_requeridas = archivo.read().splitlines()

    for biblioteca in bibliotecas_requeridas:
        try:
            importlib.import_module(biblioteca.split('==')[0])
            print(f"{biblioteca} ya está instalada.")
        except ImportError:
            print(f"{biblioteca} no está instalada. Instalando...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", biblioteca])
                print(f"{biblioteca} ha sido instalada correctamente.")
            except subprocess.CalledProcessError as e:
                print(f"Error al instalar {biblioteca}: {e}")
                sys.exit(1)

if __name__ == "__main__":
    verificar_e_instalar_dependencias()
    
    # Tu código principal comienza aquí
    print("Todas las dependencias están instaladas. Iniciando el programa principal...")
    
    # Importa tus módulos aquí
    import pandas as pd
    import numpy as np
    from transformers import AutoTokenizer, AutoModel
    import torch
    import faiss
    
    # Resto de tu código principal...

