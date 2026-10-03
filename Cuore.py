import math
import turtle

# Imposta la finestra di disegno
window = turtle.Screen()
window.setup(800, 600)
window.bgcolor("black")

# Crea la tartaruga
t = turtle.Turtle()
t.speed(0)
t.color("red")
t.pensize(2)


# Funzioni matematiche per le coordinate del cuore
def heart_x(k):
  return 15 * math.sin(k) ** 3


def heart_y(k):
  return (
      12 * math.cos(k)
      - 5 * math.cos(2 * k)
      - 2 * math.cos(3 * k)
      - math.cos(4 * k)
  )


# Solleva la penna e posizionati all'inizio
t.up()
for i in range(600):
  # Scala l'angolo e calcola le coordinate
  k = i / 10
  x = heart_x(k) * 15
  y = heart_y(k) * 15

  if i == 0:
    t.goto(x, y)
    t.down()
  else:
    t.goto(x, y)

t.hideturtle()
turtle.done()