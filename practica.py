from sympy import *;
def funcion():

    x,y = symbols("x,y");

    expresion = input('Escriba la funcion: ');
    a = input('Escriba el primer limite: ')
    b = input('Escriba el segundo limite: ')

    p1 = plot(expresion, (x,a,b), show=False);

    expresion = diff(expresion, x);

    expresion = expresion**2;

    expresion = (1 +expresion)**(1/2);

    expresion = integrate(expresion,(x, float(a),float(b)))
    print('La longitud del arco es: ')
    print(round(float(expresion),1))
    print('')

    print('Y su grafica es: ')
    p1.show()

funcion()









