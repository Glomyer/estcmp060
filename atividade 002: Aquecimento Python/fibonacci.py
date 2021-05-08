import turtle
import math


def plotarFibonacci(n):
    # variável para para expandir ou diminuir a escala da plotagem
    fator = 1

    a = 0
    b = 1
    quadrado1 = a
    quadrado2 = b

    x = turtle.Turtle()
    x.speed(100)
    x.pencolor("grey")

    # Desenho do primeiro quadrado
    x.forward(b * fator)
    x.left(90)
    x.forward(b * fator)
    x.left(90)
    x.forward(b * fator)
    x.left(90)
    x.forward(b * fator)

    temp = quadrado2
    quadrado2 = quadrado2 + quadrado1
    quadrado1 = temp

    for i in range(1, n):
        x.backward(quadrado1 * fator)
        x.right(90)
        x.forward(quadrado2 * fator)
        x.left(90)
        x.forward(quadrado2 * fator)
        x.left(90)
        x.forward(quadrado2 * fator)

        # próximo valor da sequência de Fibonacci
        temp = quadrado2
        quadrado2 = quadrado2 + quadrado1
        quadrado1 = temp

    # Resetando a posição da caneta para fazer o desenho da espiral
    x.pencolor("blue")
    x.penup()
    x.setposition(fator, 0)
    x.seth(0)
    x.pendown()

    # Plotagem da espiral
    print(b)
    x.left(90)
    for i in range(n):
        avanço = b * fator / 2 * math.pi
        avanço /= 90
        for j in range(90):
            x.forward(avanço)
            x.left(1)
        temp = a
        a = b
        b = temp + b
        print(b)

    turtle.done()


n = int(input('Insira o número de iterações: '))

# Plotagem do gráfico dado um número inteiro n
if n > 0:
    print("Série de Fibonacci para ", n, "elementos :")
    plotarFibonacci(n)
else:
    print("O número de iterações deve ser > 0")
