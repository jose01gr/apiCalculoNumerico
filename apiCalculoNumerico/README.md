# CalculadoraCalculoNumerico
Esta es una aplicación de Calculo Numérico que te permite realizar diversas operaciones, incluyendo la resolución de ecuaciones de una variable, la aproximación de funciones y la diferenciación e integración de funciones.


## Requisitos
- Python 3.x
- Biblioteca Flet
- Biblioteca Symmpy

## Instalación

-Clona este repositorio en tu máquina local:
   git clone https://github.com/tu-usuario/calculadora-calculo-numerico.git

-Navega a la carpeta del proyecto:
   cd calculadora-calculo-numerico

-Instala las dependencias requeridas:
   pip install -r requirements.txt
Esto iniciará la aplicación y abrirá una interfaz gráfica en tu navegador.


## Funcionalidades

La aplicación ofrece las siguientes funcionalidades:

1. **Resolución de Ecuaciones de una Variable:** Permite ingresar una ecuación y resuelve las soluciones para `x`.

2. **Aproximación de Funciones:** Puedes ingresar elementos de una función y la aplicación aproximará la función con un polinomio de segundo grado.

3. **Diferenciación e Integración de Funciones:** Permite ingresar una función, un valor y un intervalo, y la aplicación calculará la derivada en un punto y realizará la integración en un intervalo.

## API

La aplicación incluye una API que se utiliza para realizar los cálculos subyacentes. Puedes acceder a la API a través de los siguientes puntos finales:

- `POST /aproximar`: Aproxima una función con un polinomio de segundo grado.

- `POST /resolver`: Resuelve una ecuación de una variable.

- `POST /diferenciar`: Diferencia una función en un punto dado.

- `POST /integrar`: Integra una función en un intervalo dado.
