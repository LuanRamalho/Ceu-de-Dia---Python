import turtle

def draw_sky():
    # Configurações da tela
    screen = turtle.Screen()
    screen.bgcolor("skyblue")  # Cor do céu

def draw_sun():
    sun = turtle.Turtle()
    sun.penup()
    sun.goto(0, -100)  # Posiciona o sol
    sun.pendown()
    
    # Desenha o sol
    sun.color("yellow")
    sun.begin_fill()
    sun.circle(100)  # Raio do sol
    sun.end_fill()

def main():
    draw_sky()  # Desenha o céu
    draw_sun()  # Desenha o sol
    
    turtle.done()  # Finaliza o desenho

if __name__ == "__main__":
    main()
