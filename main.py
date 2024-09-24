import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openai

# Cargar los datos del CSV desde GitHub
url = 'https://raw.githubusercontent.com/fridaruh/top_rated_movies/refs/heads/master/Top_Rated_Movies.csv'
df = pd.read_csv(url)

# Convertir la columna 'release_date' a datetime para poder trabajar con fechas
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# Título
st.title('Peliculas geniales')

# Mostrar el total de películas
st.header('Total de películas')
total_peliculas = df.shape[0]
st.write(f"Total de películas: {total_peliculas}")

# Distribución de los votos en la columna 'vote_average'
st.header('Distribución de los votos')
fig, ax = plt.subplots()
sns.histplot(df['vote_average'], bins=20, kde=True, ax=ax)
ax.set_xlabel('Promedio de Votos')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)

# Filtro por año
st.header('Filtrar lanzamientos por año')
year_selected = st.slider('Selecciona el año', min_value=int(df['release_date'].dt.year.min()), max_value=int(df['release_date'].dt.year.max()), value=int(df['release_date'].dt.year.min()))

# Filtrar los datos por el año seleccionado
df_filtrado = df[df['release_date'].dt.year == year_selected]

# Mostrar la cantidad de películas filtradas
st.write(f"Total de películas lanzadas en {year_selected}: {df_filtrado.shape[0]}")

# Gráfica de lanzamientos por mes en formato pastel
st.header('Lanzamientos por Mes en el Año Seleccionado')

# Agregar la columna del mes
df_filtrado['month'] = df_filtrado['release_date'].dt.month

# Contar los lanzamientos por mes
lanzamientos_por_mes = df_filtrado['month'].value_counts().sort_index()

# Crear gráfica de pastel
fig3, ax3 = plt.subplots()
ax3.pie(lanzamientos_por_mes, labels=lanzamientos_por_mes.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
ax3.axis('equal')  # Para que sea un círculo
st.pyplot(fig3)

# Instanciar el cliente de OpenAI
client = openai.OpenAI(api_key=openai_api_key)

def obtener_respuesta(prompt):
  response = client.chat.completions.create(
      model="gpt-4o-mini",  # Ajusta el modelo según lo que necesites
      messages=[
          {"role": "system", "content": """
          Eres un financiero que trabaja para la aseguradora patito, eres experto en el área de solvencia,
          entonces vas a responder todo desde la perspectiva de la aseguradora. Contesta siempre en español
          en un máximo de 50 palabras.
          """}, #Solo podemos personalizar la parte de content
          {"role": "user", "content": prompt}
      ]
  )
  output = response.choices[0].message.content
  return output

prompt_user= st.text_area("Ingresa tu pregunta: ")

# Obtener la respuesta del modelo
output_modelo = obtener_respuesta(prompt_user)

# Mostrar la respuesta del modelo
st.write(output_modelo)