
import random
import math


def calcular_area(a, b, c, d, cantidad):

    puntos_elipse = 0
    puntos_interseccion = 0

    for i in range(cantidad):

        x = random.uniform(-a, a)
        y = random.uniform(-b, b)

        resultado_elipse = (x**2 / a**2) + (y**2 / b**2)
        resultado_hiperbola = (x**2 / c**2) - (y**2 / d**2)

        if resultado_elipse <= 1:

            puntos_elipse += 1

            if resultado_hiperbola >= 1:
                puntos_interseccion += 1

    area_elipse = math.pi * a * b

    if puntos_elipse > 0:
        area_interseccion = (puntos_interseccion / puntos_elipse) * area_elipse
    else:
        area_interseccion = 0

    print("\n--- RESULTADOS ---")
    print("Cantidad de puntos generados:", cantidad)
    print("Puntos dentro de la elipse:", puntos_elipse)
    print("Puntos en la interseccion:", puntos_interseccion)
    print("Area de la elipse:", round(area_elipse, 2))
    print("Area aproximada de la interseccion:", round(area_interseccion, 2))


def main():

    print("--- METODO DE MONTECARLO ---")

    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    d = float(input("Ingrese el valor de d: "))

    cantidad = int(input("Ingrese la cantidad de puntos: "))

    if a > 0 and b > 0 and c > 0 and d > 0 and cantidad > 0:

        calcular_area(a, b, c, d, cantidad)

    else:
        print("Ingrese valores mayores que cero.")


main()
