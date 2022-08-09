# Librerias

from art import text2art as art;
from time import sleep
from os import system as cmd
from matplotlib.pyplot import fill_between;
from sympy import *;
from math import *
from numpy import *
from sympy import diff as df


def cls():
    cmd('cls')

def message(text = ''):
    print(art(text, '#'))

def carga(gerundio):
    cls()
    for t in range(0,4):
        print(gerundio)
        gerundio += '.'
        sleep(.25)
        cls()

def leer(dato, tipo = 'flt'):
    while(true):
        valor = input(f'Ingrese {dato} >> ')
        try:
            if(tipo == 'flt'):
                valor = float(eval(valor))
            elif(tipo == 'func'):
                valor = parse_expr(valor)
            
            return valor
        except:
            if (tipo == 'flt'):
                print('Lo que ingreso no es un numero...')
            elif(tipo == 'func'):
                print('La funcion que ingreso no es valida')

            if (input('Ingrese una X para cancelar >> ').lower() == 'x'):
                return None


                
                


def instrucciones():
    
    cls()
    message("¡Instrucciones!")

    print(f"""Bienvenido a las instrucciones de la aplicacion.
Como introduccion las funciones:
*** La variable siempre sera representada por el simbolo X, en caso de usar cualquier otra letra provocara un error.

*** Al elevar un numero se usaran los simbolos **, por ejemplo: X² sera representado por X**2

*** Al multiplicar un numero se usara el simbolo de *, por ejemplo: 2X sera representado por 2*X

*** Representar los radicales de la siguiente manera: x**1/a; Siendo 'a' el indice del radical

*** Para representar al pi, escribalo com 'pi' literalmente

*** Tabla de funciones trigonometricas:
    seno     = sin(x)   ///  cosecante = csc(x)
    cosenos  = cos(x)   ///  secante   = sec(x)
    tangente = tan(x)   ///  cotante   = cot(x)

    Trigonometricas inversas:
    arc-seno     = asin(x)  /// arc-cosecante  = acsc(x)
    arc-coseno   = acos(x)  /// arc-secante    = asec(x)
    arc-tangente = atan(x)  /// arc-cotangente = acot(x)

""")
    input('Presiona enter tecla para continuar >>')


def areaEntreCurvas():
    while(true):
        cls()
        
        print('============Area entre curvas============')
        x = symbols('x')

        f = leer('la función f(x)=', 'func')
        if (f == None): break

        g = leer('la función g(x)=', 'func')
        if (g == None): break

        a = leer('el primer limite de integacion')
        if (a == None): break

        b = leer('el segundo limite de integacion')
        if (b == None): break

        if (a > b):
            aux = b #Variable auxiliar, en caso de que a sea mayor b se intercambian los limites de integracions
            b = a
            a = aux

        # =================================Area de integracion=====================================================  #
        try:
            puntos = solve(f-g, x)
        except:
            print('El algoritmo no tiene la capacidad para procesar esta')
            input('Presione enter para volver al menu >> ')
            break

        print(puntos)
        input()


        # for m in puntos:
        #     print(complex(m).imag)
        
        # input()
        # return


        #Elimintar los numeros imaginarios
        ims = []
        for punto in puntos:
            if (complex(punto).imag != 0):
                ims.append(punto)



        for i in ims:
            puntos.remove(i)   


        
        # Organizar el arreglo con los puntos en los que ocurre un cambio 
        

        for punto in puntos:
            if (punto <= a or punto >= b):
                puntos.remove(punto)


        # Agrego los limites de integracion para que sean parte de la comparacion
        puntos.append(a)
        puntos.append(b)

        puntos.sort()


        # Con este for puedo remover los puntos de en los que las funciones se chocan entre ellas pero que no estan dentro de los limites de integracion


        areaEntreCurva = 0 #Variable que contendra el resultado final

        for punto in puntos:
            f_pos = 0
            g_pos = 0

            if (puntos.index(punto) == len(puntos) -1):
                break
            
            i = punto
            
            while (i <= puntos[puntos.index(punto) + 1]):
                f_pos += f.subs(x, i)
                g_pos += g.subs(x, i)

                i += .1
            
            
            try:
                if (f_pos > g_pos):
                    areaEntreCurva += integrate(f-g, (x, punto, puntos[puntos.index(punto) + 1]))
                else:
                    areaEntreCurva += integrate(g-f, (x, punto, puntos[puntos.index(punto) + 1]))
            except:
                print('La funcion que ha ingresado no es valida o no pudo ser evaluada, por lo tanto lo devolveremos al menu')
                input('Presione un boton para continuar >> ')
                carga("Volviendo al menu")
                return


        cls()
        message('¡Resultado!')
        print(f"""El area entre las funciones f(x)={str(f).replace('**', '^')} y g(x)={str(g).replace('**', '^')}
En el intervalo: [{a} - {b}]""")
        respuesta = eval(str(areaEntreCurva))
        if (not isnan(respuesta)):
            print(f'el area entre las curvas es: {eval(str(areaEntreCurva)) } unidades²')
        else:
            print(f'La integral de la funcion es divergente')

        if (input('Presione (S) si quiere ver el grafico >> ').lower() == 's'):
            x_array = linspace(a, b, int((b-a)*100))
            grafico = plot(f, g, (x, a, b), show=False, fill = {'x': x_array, 'y1': lambdify(x, f)(x_array), 'color': 'orange', 'y2': lambdify(x, g)(x_array)}, ylim = (0, b-a))

            grafico.show()
            cls()
        else:
            break

        input('Presione enter para volver al menu >> ')
        break

    carga('Volviendo al menu')


def longitudArco():
    cls()
    x = symbols("x");

    expresion = leer('la funcion f=', 'func')
    a = leer('el primer limite')
    b = leer('el segundo limite')

    p1 = plot(expresion, (x,a,b), show=False);
    
    expresion = df(expresion, x);

    expresion = expresion**2;

    expresion = (1 + expresion)**(1/2);

    expresion = integrate(expresion,(x, float(a),float(b)))
    print('La longitud del arco es: ')
    print(round(float(expresion),1))
    print('')

    print('----------= Nota: Una vez vea la grafica, cierre la ventana de la misma para continuar =----------')
    input('La grafica de la funcion es: (Presione enter) >> ')
    p1.show()

    input('Presione enter para volver al menu >> ')
    carga('Volviendo al menu')







def init():
    while(true):
        cls()
        
        message('¡Bienvenido!')
        
        print(f"""Bienvenido al menu de inicio: 
(Seleccione las opciones ingresando el numero/letra de esta)

1) Hallar el area entre curvas
2) Hallar la longitud de arco

9) Instrucciones

x) Salir
""")
        opcion = input(f'Ingrese la opcion que quiere: ').lower()
        if(opcion == 'x'):
            cls()
            message('Adios...')
            print('Gracias por usar la aplicacion!')
            carga('saliendo')
            break
        elif (opcion == '9'):
            instrucciones()
        elif (opcion == '1'):
            areaEntreCurvas()
        elif (opcion == '2'):
            longitudArco()
        else:
            print('Seleccione una opcion valida')
            input('Presione entre para continuar >> ')