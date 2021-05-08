import turtle


def desenharArvore(tamanho, nivel):
    turtle.speed('fastest')
    turtle.rt(-90)
    turtle.setposition(0, -100)

    desenharCurva(tamanho, nivel)


def desenharCurva(tamanho, nivel):
    if nivel > 0:
        turtle.colormode(255)
        angulo = 25

        turtle.pencolor(0, 255 // nivel, 0)
        turtle.fd(tamanho)
        turtle.rt(angulo)

        # chamada recursiva para desenhar a subárvore direita
        desenharCurva(0.8 * tamanho, nivel - 1)

        turtle.pencolor(0, 255 // nivel, 0)
        turtle.lt(2 * angulo)

        # chamada recursiva para desenhar a subárvore esquerda
        desenharCurva(0.8 * tamanho, nivel - 1)

        turtle.pencolor(0, 255 // nivel, 0)
        turtle.rt(angulo)
        turtle.fd(-tamanho)


# Árvore de tamanho 100 e nível 10
desenharArvore(100, 10)
