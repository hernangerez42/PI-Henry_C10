# <h2 align=center> **Proyecto Individual Machine Learning Operations (MLOps)** </h1>

***Extract, transform, and load (ETL)***

Antes de utilizar el conjunto de datos para consultas o análisis en tu proyecto, es necesario realizar un proceso de Extracción, Transformación y Carga (ETL). El ETL es un proceso común en proyectos de análisis de datos y se compone de las siguientes etapas:

* Desanidación de campos: Se han desanidado los campos anidados, como belongs_to_collection y production_companies y otras columnas para poder unirlos al conjunto de datos principal y facilitar las consultas en la API. Los datos relevantes de estos campos se han extraído y agregado como columnas independientes.

* Relleno de valores nulos: Los campos revenue y budget ahora tienen el valor 0 en lugar de los valores nulos. Esto se ha realizado para asegurar la integridad de los datos y evitar problemas al realizar cálculos posteriores.

* Eliminación de valores nulos en release_date: Se han eliminado las filas que tenían valores nulos en el campo release_date, ya que no se pueden asignar formatos de fecha válidos a estos registros.

* Formato de fechas: Se ha asegurado que las fechas en el campo release_date sigan el formato AAAA-mm-dd para mantener la consistencia en el manejo de las fechas. Además, se ha creado la columna release_year, donde se ha extraído el año de la fecha de estreno para facilitar el análisis por año.

* Creación de columna de retorno de inversión: Se ha añadido la columna return que representa el retorno de inversión. Esta columna se ha calculado dividiendo los valores de revenue y budget. En caso de que los datos no estén disponibles para calcularlo, se ha asignado el valor 0.

* Eliminación de columnas no utilizadas: Se han eliminado las columnas video, imdb_id, adult, original_title, vote_count, poster_path y homepage del conjunto de datos, ya que no serán utilizadas en las consultas de la API y no aportan información relevante.

Estas modificaciones aseguran que el conjunto de datos esté preparado para su uso en consultas y análisis en la API, proporcionando datos limpios y estructurados.

Lo siguiente consistió en el desarrollo de una API que permite obtener información sobre películas. Como MLOps Engineer, he creado 6 funciones que permiten obtener información específica de la base de datos. Estas funciones fueron diseñadas para facilitar el acceso y extracción de datos relevantes para su posterior análisis

***Creacion de las funciones***

* La primera función que hemos desarrollado en la API permite ingresar un mes como parámetro y devuelve la cantidad exacta de películas que se estrenaron durante ese mes en particular. Esta funcionalidad es de gran utilidad para obtener estadísticas precisas sobre la distribución de estrenos a lo largo del año y comprender mejor la actividad cinematográfica en períodos específicos.
Al utilizar esta función en la API, los usuarios pueden ingresar el nombre del mes o su equivalente numérico, y obtendrán como resultado la cantidad exacta de películas que se estrenaron durante ese período. Esto les brinda una visión clara y cuantitativa de la cantidad de películas lanzadas en un mes determinado.

* La segunda función que desarrollamos permite ingresar un día de la semana como parámetro y devuelve la cantidad de películas que se estrenaron en ese día en particular. Esta característica resulta útil para analizar y comparar la distribución de estrenos a lo largo de la semana. Al utilizar esta función en la API, los usuarios pueden obtener fácilmente información sobre la cantidad de películas lanzadas en un día específico, lo que les brinda una visión detallada de la actividad cinematográfica semanal.

* La tercera función que implementamos en la API permite ingresar el nombre de una franquicia cinematográfica como parámetro y devuelve la cantidad de películas pertenecientes a dicha franquicia, así como la ganancia total y el promedio de ganancias de todas las películas de la franquicia.
Esta función resulta muy útil para realizar análisis específicos sobre el desempeño de una franquicia en particular. Al ingresar el nombre de la franquicia, la API realiza una búsqueda en la base de datos de películas y cuenta la cantidad de películas que pertenecen a esa franquicia en particular. Además, la API también calcula la ganancia total sumando las ganancias de todas las películas de la franquicia y luego calcula el promedio dividiendo la ganancia total entre la cantidad de películas.

* La cuarta función que hemos desarrollado en la API permite ingresar el nombre de un país como parámetro y devuelve la cantidad de películas que se han producido en ese país.
Esta función resulta útil para obtener información sobre la producción cinematográfica de un país en particular. Al ingresar el nombre del país, la API realiza una búsqueda en la base de datos de películas y cuenta la cantidad de películas que se han producido en ese país específico.

* La quinta función implementada en la API permite ingresar el nombre de una productora como parámetro y devuelve la ganancia total generada por las películas producidas por dicha productora, así como la cantidad de películas que ha producido.
Esta función es especialmente útil para realizar análisis financieros y evaluar el rendimiento de una productora en particular. Al ingresar el nombre de la productora, la API realiza una búsqueda en la base de datos de películas y calcula la ganancia total sumando las ganancias de todas las películas producidas por esa productora. Además, también cuenta la cantidad de películas que han sido producidas por dicha productora.

* La sexta función que hemos implementado en la API permite ingresar el nombre de una película como parámetro y devuelve información relevante sobre la misma, incluyendo la inversión realizada para su producción, la ganancia generada, el retorno de la inversión y el año en que fue lanzada.
Al ingresar el nombre de la película, la API busca en la base de datos y recupera los datos financieros asociados a dicha película. Proporciona información sobre la inversión total que se realizó para producir la película, la ganancia generada hasta la fecha, el cálculo del retorno de inversión (ROI) y el año en que la película fue lanzada al mercado.

* Por último, hemos desarrollado un modelo de recomendación de películas. Al ingresar el nombre de una película, el modelo utiliza algoritmos de recomendación para generar una lista de cinco películas similares que podrían ser de interés para el usuario.
Este modelo aprovecha técnicas de filtrado colaborativo y análisis de contenido para encontrar películas que compartan características similares con la película proporcionada.

Después de completar el proceso de implementación del modelo, utilizando la plataforma Render.com, ahora hemos logrado poner el modelo en línea y está disponible para su acceso desde cualquier dispositivo conectado a Internet. Este exitoso despliegue brinda a los usuarios la oportunidad de utilizar el modelo para llevar a cabo análisis detallados y tomar decisiones informadas basadas en los datos proporcionados.
Render.com ha proporcionado una infraestructura sólida y confiable para alojar el modelo, asegurando su disponibilidad y rendimiento óptimo. Esto significa que los usuarios pueden acceder al modelo en cualquier momento y desde cualquier lugar, sin preocuparse por problemas técnicos o interrupciones en el servicio.

Para acceder a todas las funcionalidades mencionadas anteriormente, te invitamos a visitar el siguiente [enlace](https://pi-henry-89yk.onrender.com/docs). Allí encontrarás la documentación completa de la API, la cual te permitirá probar y comprender todas las funcionalidades disponibles en la plataforma. La documentación es una herramienta valiosa para cualquier usuario que desee utilizar el modelo de manera efectiva, ya que brinda información detallada sobre cómo utilizar la API y cómo interpretar los resultados obtenidos. ¡No dudes en revisar la documentación para sacar el máximo provecho del modelo!