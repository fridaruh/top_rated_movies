# Tablero de Películas Top Rated

Este tablero interactivo ha sido desarrollado utilizando **Streamlit** y toma datos de un archivo CSV disponible en el siguiente repositorio de GitHub:  
[Top Rated Movies CSV](https://raw.githubusercontent.com/fridaruh/top_rated_movies/refs/heads/master/Top_Rated_Movies.csv).

### Funcionalidades:

1. **Total de películas**: Muestra el número total de películas presentes en el dataset.
   
2. **Distribución de Votos**: Una gráfica interactiva de histograma que muestra la distribución de los votos en la columna `vote_average`. Se puede visualizar cómo se distribuyen las calificaciones de las películas.

3. **Filtro por Año**: Permite filtrar las películas según el año de lanzamiento mediante un slider. Al seleccionar un año, se actualizan los datos que se muestran en el tablero.

4. **Gráfica de Pastel por Mes**: Para el año seleccionado en el filtro, se muestra una gráfica de pastel que representa los lanzamientos por mes en ese año.

### Requerimientos:

Para ejecutar este tablero, es necesario tener instalados los siguientes paquetes:
- `streamlit`
- `pandas`
- `matplotlib`
- `seaborn`

Puedes instalar las dependencias utilizando el siguiente comando:

```bash
pip install streamlit pandas matplotlib seaborn
```

### Instrucciones de Ejecución:

Para ejecutar este tablero de Streamlit, sigue los siguientes pasos:

1. Clona este repositorio o descarga el código.
2. Asegúrate de tener instaladas las dependencias necesarias.
3. Ejecuta el tablero utilizando el siguiente comando en tu terminal:

```bash
streamlit run <nombre_del_archivo>.py
```

4. El tablero se abrirá automáticamente en tu navegador por defecto.

### Fuente de Datos:
El tablero obtiene los datos del archivo CSV que contiene una lista de películas mejor calificadas con varias características como el nombre, fecha de lanzamiento, promedio de votos, etc.

Este archivo se encuentra en:  
[Top Rated Movies CSV](https://raw.githubusercontent.com/fridaruh/top_rated_movies/refs/heads/master/Top_Rated_Movies.csv)
