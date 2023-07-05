# ⚔️ Desafíos Enfrentados

## Creación de Datos:
Inicialmente, la idea era crear una base de datos muy simple en un archivo txt, pero inmediatamente me di cuenta de que eso dificultaría mucho el proceso.
El primer cambio fue crear datos sobre libros en formato Excel, con pocas columnas como fecha de publicación, autor, etc...

Sin embargo, al pasar a las siguientes etapas, me encontré con varios problemas, y el principal fue la falta de complejidad en estos datos. Básicamente, aplicar las cosas que quería aplicar en el futuro no tendría sentido porque no había nada que extraer de ellos.
#### 🏁 Finalmente, después de dedicar más tiempo, creé una base de datos, nada compleja pero ya en formato de base de datos, una tabla con columnas, 1000 nombres de clientes utilizando una biblioteca que genera datos ficticios. Esta tabla tenía 1000 filas con 8 columnas. Inmediatamente se abrieron muchas posibilidades.

## 🧹 Limpieza de Datos, Preprocesamiento y Transformación
Inicialmente, todo funcionaba sin problemas, pero esta etapa depende mucho de la siguiente. Al desarrollar los modelos de entrenamiento, me di cuenta de necesidades adicionales de complejidad. Por ejemplo, al ejecutar el modelo, el formato inicial de los datos hacía que el proceso fuera muy lento, ¡muy lento de verdad!

Después de algún tiempo de romperme la cabeza, llegué a algunas conclusiones. Modifiqué los valores de la columna `sex` a binario, lo cual mejoró considerablemente la velocidad de entrenamiento del modelo. Además, codifiqué las columnas `customer_name` y `product`, lo cual facilitó enormemente el uso de métodos de aprendizaje automático.

Utilizando el método de k-means, apliqué clustering a los datos, lo que simplificó aún más los procesos futuros. Para obtener más información, puedes investigar sobre el método de k-means y la agrupación de datos.

Hubo muchas otras adaptaciones que resultaron en un aumento significativo en la velocidad de entrenamiento. Monitoreé el aumento de velocidad y los números fueron sorprendentes.
#### Tiempo de Ejecución Inicial: 48 min 50 s
#### Tiempo de Ejecución Final: 22.56 s
#### Reducción total del tiempo en un 99.2% y aumento de 128x en la velocidad

## 🤖 Entrenamiento del Modelo para Recomendación de Productos
Sorprendentemente, esta etapa fue una de las más tranquilas. Todas las implicaciones necesarias para garantizar una ejecución sin problemas se aplicaron en la etapa anterior. Me encontré con algunos problemas de sintaxis e indentación, pero se resolvieron rápidamente. Uno de los desafíos a los que me enfrenté fue con una biblioteca llamada `surprise`, ya que no pude utilizarla de la mejor manera y tuve problemas de compatibilidad, así que volví a utilizar `scikit-learn`. Esta etapa pasó por muchos cambios, pero el más significativo fue descomponer los scripts en microfunciones para facilitar la implementación del Desarrollo Dirigido por Pruebas (TDD, por sus siglas en inglés).

Descomponer el script en microfunciones fue uno de los mayores desafíos.

## ✔️ Evaluación del Desempeño del Modelo
No tuve problemas con este script. Me gustaron mucho las aplicaciones utilizadas, y se volvió mucho más fácil después de ejecutar el script del modelo. Las consideraciones para esta etapa se centran más en los resultados en sí.

#### Comparando las métricas:

#### Primera Evaluación (Modelo 1):

#### MSE: 103.782312548213  MAE: 27.321351528391  R-cuadrado (R2): -1.2131267381625
#### Para comprender mejor, investiga los 3 métodos: MSE, MAE, R2. Sin embargo, la primera evaluación indicaba que el modelo era HORRIBLE.
#### Segunda Evaluación:
#### MSE: 23.85376567930002  MAE: 3.605650000000001  R-cuadrado (R2): 0.7809557859075236

##### En la segunda evaluación, tanto el MSE como el MAE disminuyeron significativamente en comparación con la primera evaluación. MSE es una métrica que mide el error cuadrático medio, por lo que un valor menor es mejor. MAE es una métrica que mide el error absoluto medio, y también es deseable un valor menor.

##### Además, el valor de R-cuadrado (R2) aumentó en la segunda evaluación. R2 es una métrica que indica la proporción de la varianza en los datos objetivo capturada por el modelo. Un valor más cercano a 1 se considera un buen ajuste del modelo a los datos.
