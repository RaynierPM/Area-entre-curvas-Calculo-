import numpy as np
from sympy import *
from sympy.plotting import plot
import matplotlib as plt
from math import *

x = symbols('a')

# f = input('Ingrese la funcion f(x) >> ')
# g = input('Ingrese la funcion g(x) >> ')

# a = int(input('limite inferior'))
# b = int(input('Limite superior'))

# # f = x**2
# # g = 2*x
# # a = 0
# # b = 3

# try:
#     f = parse_expr(f)
#     g = parse_expr(g)

#     grafica = plot(f,(x, a, b),show=false, axis_center = 'auto', ylim = (-(b-a), (b-a)))
#     grafica.append(plot(g, (x, a, b), show=false)[0])


#     grafica.show()
#     print(f)
#     print

# except:
#     print('La funcion ingresada es incorrecta')

y = symbols('x')
f = x**4 - 5


t = solve(f, x)

# for a in t:
#     int(a)



# print(t)

# removers = []
# for p in t:
#     if(im(p) != 0):
#         removers.append(p)


# for r in removers:
#     t.remove(r)

# f = parse_expr('2**x+3')

# print(str(f).replace('**', '^'))
