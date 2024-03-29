# Repositorio para la asignatura Sociofisica 2023-1
Este repositorio contendrá los codigos de las tareas para la asignatura Sociofisica, que constituyen el portafolio de la asignatura

Tarea 1: Voter Model
-------------------------
El código desarrollado para esta tarea tiene las dependencias:
* Numpy
* Matplotlib
* os
* time
#### Uso:
* Ejecutar primera celda para importar las librerías
* Ejecutar la celda que define la función
* Correr la función con los parámetros deseados:
    * Parámetro 1: Tamaño del sistema
    * Parámetro 2: Número de iteraciones
    * Parámetro 3: Semilla aleatoria a utilizar 
    * Parámetro 4: Número de simulaciones que se realizarán
    * Parámetro 5: Carpeta a crear con las simulaciones, debe encerrarse en comillas, de la forma 'Nombre_carpeta'

Los resultados de las simulaciones realizadas quedan en la carpeta "Simulacion/'Nombre_carpeta'/xxxx/", donde "xxxx" es el número de la simulación, cada una de estas contiene la imagen de resumen pedida y un registro de la información relevante.

Tarea 2: Majority Rule Model
------------------------------
El código desarrollado para esta tarea tiene las dependencias:
* Numpy
* Matplotlib
* os
#### Uso:
* Ejecutar ambas celdas que definen las funciones
* Correr la función Plotter con los parámetros deseados:
    * Parámetro 1: Carpeta donde se guardarán los resultados, debe encerrarse en comillas, de la forma 'Nombre_carpeta'
    * Parámetro 2: Número de grupos
    * Resto de parametros: la probabilidad de participación en los distintos grupos, debe cumplirse que
    $\sum_{i=1}^{L}a_i=1$

Tarea 3: Modelo de Deffuant
-------------------------
El código desarrollado para esta tarea tiene las dependencias:
* Numpy
* Matplotlib
* os
* time
#### Uso:
* Ejecutar primera celda para importar las librerías
* Ejecutar la celda que define la función
* Correr la función plotter con los parámetros deseados:
    * Parámetro 1: Numero de agentes
    * Parámetro 2: Número de pasos temporales
    * Parámetro 3: Numero de emparejamientos por paso temporal
    * Parámetro 4: Valor del Umbral
    * Parámetro 5: Parámetro de convergencia
    * Parámetro 6: Nombre de carpeta donde guardar los resultados, debe encerrarse en comillas, de la forma 'Nombre_carpeta'

Tarea 4: Modelo del Umbral (Granovetter)
------------------------------
El código desarrollado para esta tarea tiene las dependencias:
* Numpy
* Matplotlib
* os
#### Uso:
* Ejecutar primera celda para importar las librerías
* Ejecutar las celdas que definen la funciones
* Correr la función simul con los parámetros deseados:
    * Parámetro 1: Distribución que se utilizará (normal o uniforme)
    * Parámetro 2: Nombre de carpeta donde guardar los resultados, debe encerrarse en comillas, de la forma 'Nombre_carpeta'
    * Parámetro 3 (Opcional): Media a utilizar
    * Parámetro 4 (Opcional): Desviación estandar a utilizar