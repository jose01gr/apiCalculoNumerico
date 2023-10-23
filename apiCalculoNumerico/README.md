# CalculadoraCalculoNumerico
Esta es una aplicación de calculadora que resuelve sistemas de ecuaciones lineales, encuentra autovalores y autovectores de matrices, y realiza interpolación.
## Descripción

Esta aplicación se ha desarrollado utilizando la biblioteca `flet` y la biblioteca `numpy` de Python para realizar cálculos numéricos. Proporciona tres funciones principales:

## Requisitos
- Python 3.x
- Biblioteca Flet
- Biblioteca Numpy

## Instalación

1. Crea un entorno virtual:

   ```bash
   python3 -m venv env

2. Activa el entorno virtual:
 
   source env/bin/activate

3. Instala la librería Flet (si no está instalada):

   pip install flet

4. Ejecuta la aplicación:
   python app.py
     


## Uso

Ejecuta la aplicación Python y se abrirá una interfaz gráfica que te permitirá realizar varios tipos de cálculos numéricos:

1. **Sistema de Ecuaciones Lineales 3x3:** Permite al usuario ingresar los coeficientes de un sistema de ecuaciones lineales y resuelve las incógnitas `X`, `Y` y `Z` utilizando la eliminación gaussiana. Los resultados se muestran en la interfaz gráfica.

2. **Autovector y Autovalor:** Permite al usuario ingresar una matriz y encuentra los autovectores y autovalores correspondientes utilizando la biblioteca `numpy`. Los resultados se muestran en la interfaz gráfica.

3. **Interpolación:** Esta función permite al usuario realizar la interpolación lineal de un valor desconocido `Y` en un `X` ingresado por el usuario, dado dos pares de valores `X` e `Y`. El resultado se muestra en la interfaz gráfica.

Simplemente sigue las instrucciones en la interfaz para ingresar los datos necesarios y realizar los cálculos.

## Ejemplo

Para usar la aplicación:

1. Ejecuta la aplicación Python.

2. Elige una de las opciones disponibles, por ejemplo, "Sistema de Ecuaciones".

3. Ingresa los datos requeridos, como los coeficientes del sistema.

4. Haz clic en el botón correspondiente para realizar el cálculo.

5. Observa los resultados en la interfaz de usuario.

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.

2. Crea una rama para tu contribución: `git checkout -b mi-contribucion`

3. Realiza tus cambios y compromételos: `git commit -m "Añade una nueva característica"`

4. Envía una solicitud de extracción.
