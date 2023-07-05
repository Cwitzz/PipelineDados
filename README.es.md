# Pipeline de Datos para Sistema de Recomendación de Productos

Este proyecto representa una pipeline de datos sofisticada que tiene como objetivo construir un sistema de recomendación de productos con enfoque en prácticas de ingeniería de datos, aprendizaje de máquina y pruebas automatizadas.

## 🧱 Componentes de la Pipeline

### 1. Criação da Base de Dados

El script `criação_base_dados.py` crea una base de datos SQLite llamada `DBFIC.db`. La base de datos contiene una colección de transacciones de productos de jardinagem con datos ficticios, generados a través de la biblioteca Faker, incluyendo nombres, direcciones, precios, cantidades y otros.

### 2. Limpeza y Transformación de los Datos

El script `data_cleaning_transform.py` realiza varias operaciones de limpieza y transformación de datos, incluyendo el manejo de valores faltantes, conversión de formatos y normalización de características numéricas utilizando pandas, scikit-learn y NumPy.

### 3. Treinamento do Modelo de Recomendação

`model_training_product_recomm.py` es responsable del treinamiento de un modelo de aprendizaje de máquina para la recomendación de productos. El modelo y los encoders se serializan en archivos `.pkl` para su reutilización.

### 4. Inserção de Recomendações no Banco de Dados

El script `insert_recommendations.py` aplica el modelo entrenado para generar recomendaciones personalizadas que se insertan en la base de datos `DBFIC.db`.

### 5. Avaliação de Desempenho

El script `evaluate_perfomance_model.py` calcula métricas de desempeño relevantes para sistemas de recomendación, como precisión, recall, puntuación F1, entre otros.

### 6. Testes Automatizados

El proyecto incluye testes automatizados en los scripts `Test_model_training_product_recomm.py` y `test_data_cleaning_transform.py` para verificar la integridad de las funciones y los resultados.

### 7. Documentación

El archivo `README.md` proporciona información sobre la configuración, objetivos del proyecto, instrucciones para ejecutarlo y explicaciones sobre los componentes de la pipeline.

## ⚙️ Escalabilidade e Desempenho

El proyecto está diseñado con un enfoque en la escalabilidad y el desempeño, con la posibilidad de extenderlo a conjuntos de datos más grandes e integrarlo con plataformas de datos en la nube.

## 🚀 Conclusión

Esta pipeline es una solución robusta para la construcción de un sistema de recomendación de productos. Cubre desde la creación de la base de datos hasta la evaluación del desempeño del modelo, asegurando calidad, testabilidad y escalabilidad. Por ahora, no se han desarrollado etapas de análisis de datos, ya que el enfoque del proyecto no se centró en eso.

## 👨‍💻 Cómo Ejecutar

### Prerequisitos
Asegúrate de tener Python 3.11 instalado en tu máquina. Además, necesitarás algunas bibliotecas de Python. Puedes instalarlas utilizando pip:
`pip install pandas scikit-learn sqlite3 joblib faker numpy random`

Es posible que no todas las bibliotecas sean necesarias, por lo que se recomienda utilizar un entorno de desarrollo integrado (IDE) para abrir el proyecto.

### Paso 1: Configuración de la Base de Datos
Primero, necesitas crear y poblar la base de datos con datos ficticios. Utiliza el script `criação_base_dados.py` para hacerlo.
`python criação_base_dados.py`

### Paso 2: Limpieza, Preprocesamiento y Transformación de Datos
Después de configurar la base de datos, ejecuta el script `data_cleaning_transform.py` para limpiar y transformar los datos.
`python data_cleaning_transform.py`

### Paso 3: Entrenamiento del Modelo de Recomendación
Ahora que los datos están listos, puedes entrenar el modelo de recomendación. Ejecuta el script `model_training_product_recomm.py`.
`python model_training_product_recomm.py`

### Paso 4: Evaluación del Rendimiento del Modelo
Evalúa el rendimiento del modelo utilizando el script `evaluate_perfomance_model.py`. Esto proporcionará métricas útiles para comprender el valor real del modelo.
`python evaluate_perfomance_model.py`

### Paso 5: Inserción de Recomendaciones en la Base de Datos
Finalmente, utiliza el script `insert_recommendations.py` para insertar las recomendaciones generadas en la base de datos.
`python insert_recommendations.py`

Este paso puede ser irrelevante, ya que con las actualizaciones, se agregó esta función directamente al script de entrenamiento del modelo.

### Conclusión de la Ejecución
Después de ejecutar estos scripts en el orden especificado, tendrás un modelo de recomendación de productos entrenado y listo para usar. Las recomendaciones se almacenarán en la base de datos SQLite y se podrán acceder según sea necesario.

## Consideraciones
Quiero dejar claro que si deseas utilizar esta pipeline para estudios, debes adaptar todos los aspectos del código a tus propias condiciones, por ejemplo, el nombre de la base de datos, las rutas e incluso el SGBD utilizado para la base de datos, o incluso no utilizarlo y cambiarlo por datos en formato Excel, por ejemplo.

Además, los scripts están escritos específicamente para la tabla creada por el script inicial. Si deseas utilizar tablas diferentes, con características diferentes, deberás adaptar toda la cadena de scripts.

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.
