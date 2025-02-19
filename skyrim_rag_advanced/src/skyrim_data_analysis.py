# Importación de las bibliotecas necesarias
import pandas as pd  # Para manipulación y análisis de datos
import matplotlib.pyplot as plt  # Para crear visualizaciones
import seaborn as sns  # Para crear visualizaciones estadísticas más atractivas

# Carga de los datos desde el archivo CSV
# pd.read_csv() lee un archivo CSV y lo convierte en un DataFrame de pandas
# El argumento '../data/skyrim_data_clean.csv' especifica la ruta relativa al archivo
df = pd.read_csv('../data/skyrim_data_clean.csv')

# Mostrar las primeras filas del DataFrame
# head() muestra por defecto las primeras 5 filas del DataFrame
# Esto nos da una vista rápida de la estructura de los datos
print("Primeras filas del DataFrame:")
print(df.head())

# Mostrar información general sobre el DataFrame
# info() proporciona un resumen conciso del DataFrame, incluyendo tipos de datos y valores no nulos
# Esto es útil para entender la estructura general de los datos y detectar valores faltantes
print("\nInformación general del DataFrame:")
print(df.info())

# Análisis básico de estadísticas descriptivas
# describe() genera estadísticas descriptivas para las columnas numéricas del DataFrame
# Incluye conteo, media, desviación estándar, mínimo, máximo y cuartiles
print("\nEstadísticas descriptivas del DataFrame:")
print(df.describe())

# Visualización de la distribución de razas
# Creamos una figura de matplotlib con un tamaño específico
plt.figure(figsize=(12, 6))

# Creamos un gráfico de barras de la distribución de razas
# value_counts() cuenta las ocurrencias únicas en la columna 'Race'
# plot(kind='bar') crea un gráfico de barras
df['Race'].value_counts().plot(kind='bar')

# Añadimos título y etiquetas a los ejes
plt.title('Distribución de Razas en Skyrim')
plt.xlabel('Raza')
plt.ylabel('Cantidad')

# Ajustamos el diseño para evitar que las etiquetas se corten
plt.tight_layout()

# Guardamos la figura en un archivo PNG
# Esto permite guardar la visualización para su uso posterior
plt.savefig('../notebooks/race_distribution.png')

# Cerramos la figura actual para liberar memoria
plt.close()

# Comparación de habilidades promedio por raza
# Lista de todas las habilidades en el juego
skills = ['Smithing', 'Heavy Armor', 'Block', 'Two-Handed', 'One-Handed', 'Archery', 
          'Light Armor', 'Sneak', 'Lockpicking', 'Pickpocket', 'Speech', 'Alchemy',
          'Illusion', 'Conjuration', 'Destruction', 'Restoration', 'Alteration', 'Enchanting']

# Calculamos el promedio de cada habilidad para cada raza
# groupby('Race') agrupa los datos por raza
# [skills].mean() calcula la media de todas las habilidades para cada grupo
avg_skills = df.groupby('Race')[skills].mean()

# Creamos una nueva figura para el mapa de calor
plt.figure(figsize=(15, 10))

# Creamos un mapa de calor usando seaborn
# annot=True muestra los valores en cada celda
# cmap='YlOrRd' establece la paleta de colores (amarillo a rojo)
# fmt='.1f' formatea los números a un decimal
sns.heatmap(avg_skills, annot=True, cmap='YlOrRd', fmt='.1f')

# Añadimos un título al mapa de calor
plt.title('Habilidades Promedio por Raza')

# Ajustamos el diseño
plt.tight_layout()

# Guardamos el mapa de calor como un archivo PNG
plt.savefig('../notebooks/skills_heatmap.png')

# Cerramos la figura
plt.close()

# Guardamos los resultados en un archivo CSV
# to_csv() guarda el DataFrame como un archivo CSV
# Esto permite un análisis más detallado en el futuro o el uso de los datos en otras aplicaciones
avg_skills.to_csv('../data/avg_skills_by_race.csv')

# Imprimimos un mensaje indicando que el análisis ha terminado
print("Análisis completado. Los resultados se han guardado en la carpeta 'data' y las visualizaciones en la carpeta 'notebooks'.")

# Análisis adicional: Top 5 razas con mayor habilidad en cada categoría
print("\nTop 5 razas con mayor habilidad en cada categoría:")
for skill in skills:
    print(f"\n{skill}:")
    # Ordenamos el DataFrame por la habilidad actual y mostramos las top 5 razas
    top_5 = avg_skills.sort_values(by=skill, ascending=False).head()
    print(top_5[skill])

# Análisis de correlación entre habilidades
print("\nCorrelación entre habilidades:")
correlation_matrix = df[skills].corr()
print(correlation_matrix)

# Visualización de la matriz de correlación
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlación entre Habilidades')
plt.tight_layout()
plt.savefig('../notebooks/correlation_matrix.png')
plt.close()

print("Análisis adicional completado. Se ha guardado la matriz de correlación en 'notebooks/correlation_matrix.png'.")

# Análisis adicional: Top 5 razas con mayor habilidad en cada categoría
print("\nTop 5 razas con mayor habilidad en cada categoría:")
for skill in skills:
    print(f"\n{skill}:")
    # Ordenamos el DataFrame por la habilidad actual y mostramos las top 5 razas
    top_5 = avg_skills.sort_values(by=skill, ascending=False).head()
    print(top_5[skill])

# Este bucle recorre todas las habilidades definidas anteriormente
# Para cada habilidad, realiza lo siguiente:
# 1. Imprime el nombre de la habilidad
# 2. Ordena el DataFrame avg_skills por esa habilidad en orden descendente
# 3. Selecciona las 5 primeras filas (top 5 razas)
# 4. Imprime los valores de esa habilidad para las 5 razas seleccionadas
#
# Ejemplo de salida para una habilidad:
# Smithing:
# High Elf    27.0
# Orc         28.0
# Dark Elf    26.0
# Redguard    20.0
# Nord        20.0

# Análisis de correlación entre habilidades
print("\nCorrelación entre habilidades:")
correlation_matrix = df[skills].corr()
print(correlation_matrix)

# df[skills] selecciona solo las columnas de habilidades del DataFrame
# .corr() calcula la matriz de correlación entre estas columnas
# La correlación mide la relación lineal entre dos variables
# Los valores van de -1 (correlación negativa perfecta) a 1 (correlación positiva perfecta)
# 0 indica que no hay correlación lineal

# Visualización de la matriz de correlación
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlación entre Habilidades')
plt.tight_layout()
plt.savefig('../notebooks/correlation_matrix.png')
plt.close()

# Creamos una nueva figura de 12x10 pulgadas
# Usamos seaborn para crear un mapa de calor de la matriz de correlación
# annot=True muestra los valores numéricos en cada celda
# cmap='coolwarm' establece una paleta de colores que va del azul (correlación negativa) al rojo (correlación positiva)
# fmt='.2f' formatea los números a 2 decimales
# Añadimos un título al gráfico
# Ajustamos el diseño y guardamos la figura como un archivo PNG
# Cerramos la figura para liberar memoria

print("Análisis adicional completado. Se ha guardado la matriz de correlación en 'notebooks/correlation_matrix.png'.")

# Este análisis adicional proporciona información valiosa sobre:
# 1. Qué razas destacan en cada habilidad
# 2. Cómo se relacionan las diferentes habilidades entre sí
#
# Por ejemplo, podrías observar que:
# - Ciertas razas son consistentemente buenas en múltiples habilidades
# - Algunas habilidades están fuertemente correlacionadas (por ejemplo, magia de destrucción y conjuración)
# - Otras habilidades podrían tener correlaciones negativas, indicando especializaciones opuestas

# Análisis de clases de personajes
print("\nDistribución de clases de personajes:")
class_distribution = df['Class'].value_counts()
print(class_distribution)

# Visualización de la distribución de clases
plt.figure(figsize=(12, 6))
class_distribution.plot(kind='bar')
plt.title('Distribución de Clases de Personajes en Skyrim')
plt.xlabel('Clase')
plt.ylabel('Cantidad')
plt.tight_layout()
plt.savefig('../notebooks/class_distribution.png')
plt.close()

# Análisis de habilidades promedio por clase
avg_skills_by_class = df.groupby('Class')[skills].mean()

plt.figure(figsize=(15, 10))
sns.heatmap(avg_skills_by_class, annot=True, cmap='YlOrRd', fmt='.1f')
plt.title('Habilidades Promedio por Clase')
plt.tight_layout()
plt.savefig('../notebooks/skills_by_class_heatmap.png')
plt.close()

print("Análisis de clases completado. Se han guardado las visualizaciones en la carpeta 'notebooks'.")

# Análisis de razas y clases
print("\nDistribución de razas:")
race_distribution = df['Race'].value_counts()
print(race_distribution)

print("\nDistribución de clases:")
class_distribution = df['Class'].value_counts()
print(class_distribution)

# Visualización de la distribución de razas y clases
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

race_distribution.plot(kind='bar', ax=ax1)
ax1.set_title('Distribución de Razas')
ax1.set_xlabel('Raza')
ax1.set_ylabel('Cantidad')

class_distribution.plot(kind='bar', ax=ax2)
ax2.set_title('Distribución de Clases')
ax2.set_xlabel('Clase')
ax2.set_ylabel('Cantidad')

plt.tight_layout()
plt.savefig('../notebooks/race_class_distribution.png')
plt.close()

print("Análisis de razas y clases completado. Se ha guardado la visualización en 'notebooks/race_class_distribution.png'.")
# Análisis de facciones
print("\nAnálisis de facciones:")

# Crear una lista de todas las facciones únicas
all_factions = []
for factions in df['Factions'].dropna():
    all_factions.extend(factions.split(';'))
unique_factions = list(set(all_factions))

# Contar cuántos personajes pertenecen a cada facción
faction_counts = {faction: sum(df['Factions'].str.contains(faction, na=False)) for faction in unique_factions}

# Ordenar las facciones por número de miembros
sorted_factions = sorted(faction_counts.items(), key=lambda x: x[1], reverse=True)

# Mostrar las 10 facciones más comunes
print("Las 10 facciones más comunes:")
for faction, count in sorted_factions[:10]:
    print(f"{faction}: {count}")

# Visualización de las facciones más comunes
plt.figure(figsize=(12, 6))
factions, counts = zip(*sorted_factions[:10])
plt.bar(factions, counts)
plt.title('Las 10 Facciones más Comunes en Skyrim')
plt.xlabel('Facción')
plt.ylabel('Número de Personajes')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('../notebooks/top_factions.png')
plt.close()

print("Análisis de facciones completado. Se ha guardado la visualización en 'notebooks/top_factions.png'.")

