import turtle


def desenharTriangulo(x, y):
    tortuga.pencolor("red")
    tortuga.penup()
    # para fazer o desenho no ponto (x, y) clicado pelo mouse
    tortuga.goto(x, y)
    tortuga.pendown()

    for i in range(3):
        tortuga.backward(100)
        tortuga.right(120)
        tortuga.backward(100)


wn = turtle.Screen()
tortuga = turtle.Turtle()

# ao clicar, chamamos a função de desenhar o triângulo, passando as coordenadas do clique como parâmetro
turtle.onscreenclick(desenharTriangulo, 1)
turtle.listen()

# segurar a tela
turtle.done()
