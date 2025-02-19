import os
import pandas as pd

def load_and_prepare_data(file_path):
    # Obtener la ruta absoluta al directorio del script actual
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construir la ruta al archivo de datos
    full_path = os.path.join(current_dir, '..', 'data', os.path.basename(file_path))
    
    df = pd.read_csv(full_path)
    
    # Combinar información relevante en un solo campo de texto
    df['text'] = df['Name'] + ': ' + df['Race'] + ' ' + df['Class'] + ' from ' + df['Location'].fillna('Unknown') + \
                 '. Skills: ' + df['Primary Skills'].fillna('Unknown')
    
    return df

if __name__ == '__main__':
    df = load_and_prepare_data('skyrim_data_clean.csv')
    print(df['text'].head())
    df.to_csv('../data/prepared_skyrim_data.csv', index=False)

import os
import pandas as pd

def load_and_prepare_data(file_path):
    # Obtener la ruta absoluta al directorio del script actual
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construir la ruta al archivo de datos
    full_path = os.path.join(current_dir, '..', 'data', os.path.basename(file_path))
    
    df = pd.read_csv(full_path)
    
    # Combinar información relevante en un solo campo de texto
    df['text'] = df['Name'] + ': ' + df['Race'] + ' ' + df['Class'] + ' from ' + df['Location'].fillna('Unknown') + \
                 '. Skills: ' + df['Primary Skills'].fillna('Unknown')
    
    return df

if __name__ == '__main__':
    df = load_and_prepare_data('skyrim_data_clean.csv')
    print(df['text'].head())
    df.to_csv('../data/prepared_skyrim_data.csv', index=False)

