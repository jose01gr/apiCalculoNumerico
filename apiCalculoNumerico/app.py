import flet as ft
from flet import AppBar, ElevatedButton, Page, Text, View, TextStyle,FontWeight
import requests


# Se crea la pagina donde se va a desarrollar la aplicacion
def main(page: Page):

    #titulo de la pagina
    page.title = "Calculadora de Ecuaciones"

    #text field de la ecuacion
    e1=ft.TextField(label="",width=100,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    ex = ft.Text("Ecuacion: ",color="#1a2e41",size=20,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD))
    
    #text del Resultado
    eR1 = ft.Text("X=",color="#1a2e41",size=20,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD))
    

    #text fields de la funcion
    elemento1=ft.TextField(label="x",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    elemento2=ft.TextField(label="a",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    elemento3=ft.TextField(label="b",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    elemento4=ft.TextField(label="c",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    
    #text de la respuesta
    respuesta1 = ft.Text("Valor = ",color="#1a2e41",size=14,font_family="Consolas")
    


    #text fields de las funciones y sus puntos
    ec = ft.Text("Ecuacion: ",color="#1a2e41",size=20,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD))
    e2 =ft.TextField(label="",width=100,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    x =ft.TextField(label="x ",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    b =ft.TextField(label="b ",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    c =ft.TextField(label="c ",width=50,height=40,bgcolor ="#A4B7CF",color ="#1a2e41")
    
    #resultado de la operacion
    resultado=ft.Text("Resultado= ",color="#1a2e41",size=14,font_family="Consolas")

    # funcion para el cambio de ventanas
    def route_change(e):
        ventanaMenu()  
        if page.route == "/ecuaciones":
            ventanaEcuacion()
           
        elif page.route == "/aproximacion":
            ventanaAproximacion()
           

        elif page.route == "/Diferenciacion":
            ventanaDiferenciacion()
        page.update()
    
    # menu para elegir la ventana que se quiere
    def ventanaMenu():
        page.views.clear()
        page.views.append(
            
            View(
                "/",
                [
                    AppBar(title=Text("CALCULO NUMERICO",color="#1a2e41",size=35,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD)),center_title=True,bgcolor="#D9D9D9",toolbar_height=80),
                     
        ft.Column(
            [    
                 ft.ElevatedButton(text="RESOLUCION DE UNA ECUACION DE UNA VARIABLE",bgcolor ="#1a2e41" ,color = "#D9D9D9", height=100,width=400,on_click=lambda _: page.go("/ecuaciones")),
                 ft.ElevatedButton(text="APROXIMACION DE FUNCIONES",bgcolor ="#1a2e41" , color = "#D9D9D9",height=100,width=400, on_click=lambda x: page.go("/aproximacion")),
                 ft.ElevatedButton(text="DIFERENCIACION E INTEGRACION DE FUNCIONES",bgcolor ="#1a2e41" , color = "#D9D9D9",height=100,width=400, on_click= lambda x: page.go("/Diferenciacion"))
            ],spacing=50
            
        )  
    
                ],
            vertical_alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,bgcolor="#9BA5B7"
            )
            
        )

    # ventana de la resolucion de ecuacion de una variable
    def ventanaEcuacion():
        page.views.append(
                View(
                    "/ecuaciones",
                    [
                        AppBar(title=Text("Calculo Numerico: Resolucion de ecuaciones de una variable",color="#1a2e41",size=35,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD)),center_title=True,bgcolor="#D9D9D9",toolbar_height=80),
                        ft.Row([
                            ElevatedButton("Volver",color="#D9D9D9",bgcolor="#1a2e41", on_click=lambda _: page.go("/")),
                            ft.Container(Text("Resolucion de ecuaciones",color="#D9D9D9",font_family="Consolas",size=15),bgcolor="#1A2E41",border_radius = 10,width=300,height=80,alignment=ft.alignment.center)
                            
                    ],spacing=382)
,
                        ft.Column([
                            
                            
                            
                            ft.Container(
                                ft.Column([
                                    ft.Row([ft.Text("Ingrese la ecuacion a resolver",color="#1a2e41",font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD)) ],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ex, e1],spacing=10,alignment=ft.MainAxisAlignment.CENTER),
                                    ft.ElevatedButton(text="RESOLVER ECUACION",bgcolor ="#1a2e41" ,color = "#D9D9D9", height=40,width=400,on_click= resolverEcuacion),
                                    ft.ElevatedButton(text="LIMPIAR",bgcolor ="#4C6B94" ,color = "#D9D9D9", height=40,width=200,on_click=limpiar),
                                    
                                ],spacing=15,
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER),
                            alignment = ft.alignment.center,
                            width=400,
                            height=350,
                            bgcolor="#788BA7",
                            border_radius = 10,
                            padding=20
                        ),
                        ft.Container(
                            ft.Column([
                                    ft.Row([ft.Text("Resultados",color="#1a2e41",size=20,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD)) ],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([eR1],spacing=30,alignment=ft.MainAxisAlignment.CENTER),
                                    
                                ],spacing=15),
                            width=400,
                            height=135,
                            bgcolor="#A5B5C9",
                            border_radius=10,
                            padding = 20
                        )
                    ])
                    

                    ],bgcolor="#9BA5B7", vertical_alignment = ft.MainAxisAlignment.CENTER,
                     horizontal_alignment = ft.CrossAxisAlignment.CENTER
                )
            )
    # ventana de la solucion de la aproximacion
    def ventanaAproximacion():
        page.views.append(
                View(
                    "/aproximacion",
                    [
                        AppBar(title=Text("Calculo Numerico: Aproximacion de funciones",color="#1a2e41",size=35,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD)),center_title=True,bgcolor="#D9D9D9",toolbar_height=80),
                        ft.Row([
                            ElevatedButton("Volver",color="#D9D9D9",bgcolor="#1a2e41", on_click=lambda _: page.go("/")),
                            ft.Container(Text("Solucion de Aproximacion",color="#D9D9D9",font_family="Consolas",size=15),bgcolor="#1A2E41",border_radius = 10,width=300,height=80,alignment=ft.alignment.center)
                            
                    ],spacing=382)
,
                        ft.Column([
                            
                            
                            
                            ft.Container(
                                ft.Column([
                                    ft.Row([ft.Text("Ingrese los elementos de la funcion",color="#1a2e41",size=14,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD)) ],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([elemento1, elemento2],spacing=20,alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([elemento3, elemento4],spacing=20,alignment=ft.MainAxisAlignment.CENTER),
                                    ft.ElevatedButton(text="RESOLVER APROXIMACION",bgcolor ="#1a2e41" ,color = "#D9D9D9", height=40,width=400,on_click=resolverAprox),
                                    ft.ElevatedButton(text="LIMPIAR",bgcolor ="#4C6B94" ,color = "#D9D9D9", height=40,width=200,on_click=limpiar),
                                    
                                ],spacing=15,horizontal_alignment = ft.CrossAxisAlignment.CENTER),
                            alignment = ft.alignment.center,
                            width=400,
                            height=350,
                            bgcolor="#788BA7",
                            border_radius = 10,
                            padding = 15,
                        ),
                        ft.Container(
                            ft.Column([
                                    ft.Row([ft.Text("Resultados",color="#1a2e41",size=20,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD)) ],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([respuesta1])
                                ],spacing=10),
                            width=400,
                            height=135,
                            bgcolor="#A5B5C9",
                            border_radius=10,
                            padding =15
                        )
                    ])
                    

                    ],bgcolor="#9BA5B7", vertical_alignment = ft.MainAxisAlignment.CENTER,
                     horizontal_alignment = ft.CrossAxisAlignment.CENTER
                )
            )
    # ventana de la solucion de la diferenciacion e Integracion
    def ventanaDiferenciacion():
        page.views.append(
                View(
                    "/Diferenciacion",
                    [
                        AppBar(title=Text("Calculo Numerico: Diferenciacion e Integracion",color="#1a2e41",size=35,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD)),center_title=True,bgcolor="#D9D9D9",toolbar_height=80),
                        ft.Row([
                            ElevatedButton("Volver",color="#D9D9D9",bgcolor="#1a2e41",on_click=lambda _: page.go("/")),
                            ft.Container(Text("Solucion: ",color="#D9D9D9",font_family="Consolas",size=15),bgcolor="#1A2E41",border_radius = 10,width=300,height=80,alignment=ft.alignment.center)
                            
                    ],spacing=382)
,
                        ft.Column([
                            
                            
                            
                            ft.Container(
                                
                                ft.Column([
                                    ft.Row([ft.Text("Ingrese la ecuacion y los valores",color="#1a2e41",size=16,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD)) ],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ec,e2],spacing=20,alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([x,b,c],spacing=20,alignment=ft.MainAxisAlignment.CENTER),
                                    ft.ElevatedButton(text="RESOLVER DIFERENCIACION",bgcolor ="#1a2e41" ,color = "#D9D9D9", height=40,width=400,on_click=resolverDiferenciacion),
                                    ft.ElevatedButton(text="RESOLVER INTEGRACION",bgcolor ="#1a2e41" ,color = "#D9D9D9", height=40,width=400,on_click=resolverIntegracion),
                                    ft.ElevatedButton(text="LIMPIAR",bgcolor ="#4C6B94" ,color = "#D9D9D9", height=40,width=200,on_click=limpiar),
                                ],spacing=15,horizontal_alignment = ft.CrossAxisAlignment.CENTER),
                                width=400,
                                height=350,
                                bgcolor="#788BA7",
                                border_radius = 10,
                                padding=20,
                 
                                
                                
                            
                        ),
                        ft.Container(
                            ft.Column([
                                ft.Row([ft.Text("Resultados:",color="#1a2e41",size=20,font_family="Consolas",style=TextStyle(weight=FontWeight.BOLD)) ],alignment=ft.MainAxisAlignment.CENTER),
                                ft.Row([resultado],alignment=ft.MainAxisAlignment.CENTER),
                            ],spacing=20),
                            width=400,
                            height=135,
                            bgcolor="#A5B5C9",
                            border_radius=10,
                            padding=20,
                        )
                    ])
                    

                    ],bgcolor="#9BA5B7", vertical_alignment = ft.MainAxisAlignment.CENTER,
                     horizontal_alignment = ft.CrossAxisAlignment.CENTER
                )
            )

    # hace el cambio de vista de ventana
    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # funcion que llama a las respuestas del backend mediante la API para la solucion de la ecuacion de una variable
    def resolverEcuacion():
            # Enviamos una solicitud POST a la API
            response = requests.post("http://localhost:8000/resolver", json={"ecuacion": e1.value})
            # Obtenemos la respuesta
            soluciones = response.json()
            
            # Mostramos la solución
            eR1.value = 'X= ' + str(soluciones)

    # funcion que llama a las respuestas del backend mediante la API para la solucion de la aproximacion
    def resolverAprox():
        # Enviamos una solicitud POST a la API
        response = requests.post("http://localhost:8000/aproximar", json={"x": int(elemento1.value) , "a": int(elemento2), "b": int(elemento3), "c": int(elemento4)})

        # Obtenemos la respuesta
        aproximacion = response.json()
        
        # Mostramos la solucion
        respuesta1.value = 'Valor = ' + str(aproximacion)
    
    # funcion que llama a las respuestas del backend mediante la API para la resolucion de la diferenciacion
    def resolverDiferenciacion():
        # Enviamos una solicitud POST a la API
        response = requests.post("http://localhost:8000/diferenciar", json={"funcion": e2.value, "x": x.value})

        # Obtenemos la respuesta
        derivada = response.json()
        
        resultado = "Resultado= " + str(derivada)
    
    # funcion que llama a las respuestas del backend mediante la API para la soluci de la integracion
    def resolverIntegracion():
        # Enviamos una solicitud POST a la API
        response = requests.post("http://localhost:8000/integrar", json={"funcion": e2.value, "a": b.value, "b": c.value})

        # Obtenemos la respuesta
        integral = response.json()
        
        resultado = "Resultado= " + str(integral)
    
    # funcion para limpiar los campos de texto
    def limpiar(e):
        e1.value = ""
        eR1.value = ""

        elemento1.value = ""
        elemento2.value = ""
        elemento3.value = ""
        elemento4.value = ""
        respuesta1.value = ""

        x.value = ""
        e2.value = ""
        b.value = ""
        c.value = ""
        resultado.value = ""


        page.update()

        

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)


if __name__ == "__main__":

    ft.app(main)
