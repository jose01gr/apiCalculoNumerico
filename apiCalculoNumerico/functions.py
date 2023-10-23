
from flet import app
from flet_fastapi import FastAPI
import sympy as sp
from sympy import Symbol
from sympy import series
from sympy import *

app = FastAPI()

# Aproxima una función con un polinomio de Taylor de grado 2
def aproximar(x: float, a: float, b: float, c: float):

    # Creamos una variable simbólica
    x_sym = Symbol("x")

    # Definimos la función
    funcion = a * x_sym ** 2 + b * x_sym + c

    # Calculamos el polinomio de Taylor
    polinomio = series(funcion, x_sym, x).as_poly()

    # Devolvemos el valor del polinomio en x
    return polinomio.evalf(x)

# Resuelve una ecuacion de una variable
def resolver_ecuacion(ecuacion: str):
    # Convertimos la ecuación a una expresión simbólica
    expr = sp.sympify(ecuacion)

    # Resolvemos la ecuación
    soluciones = sp.solve(expr)

    # Devolvemos la solución
    if soluciones is None:
        return None
    else:
        return list(soluciones.values())

# Diferencia una función en un punto dado  
def diferenciar(funcion: str, x: float):

    # Convertimos la función a una expresión simbólica
    expr = sp.sympify(funcion)

    # Diferenciamos la expresión
    derivada = sp.diff(expr, x)

    # Devolvemos la derivada
    return derivada.evalf(subs={x: x})

# Integra una función en un intervalo dado
def integrar(funcion: str, a: float, b: float):

    # Convertimos la función a una expresión simbólica
    expr = sp.sympify(funcion)

    # Integramos la expresión
    integral = sp.integrate(expr, (a, b))

    # Devolvemos la integral
    return integral.evalf()


# API
@app.post("/aproximar")
def aproximar(x: float, a: float, b: float, c: float):
    """Aproxima una función con un polinomio de segundo grado."""
    return aproximar(x, a, b, c)

@app.post("/resolver")
def resolver(ecuacion: str):
    """Resuelve una ecuación de una variable."""
    return resolver_ecuacion(ecuacion)

@app.post("/diferenciar")
def diferenciar(funcion: str, x: float):
    """Diferencia una función en un punto dado."""
    return diferenciar(funcion, x)

@app.post("/integrar")
def integrar(funcion: str, a: float, b: float):
    """Integra una función en un intervalo dado."""
    return integrar(funcion, a, b)
