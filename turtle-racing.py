# use the mac terminal to run this file: python3 turtle-racing.py, running it here will not work properly

import turtle
import random
import time

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "cyan", "black"]

def get_number_of_turtles():
  turtles = 0
  while True:
    turtles = input("Enter the number of turtles (2-10): ")
    if turtles.isdigit():
      turtles = int(turtles)
      if 2 <= turtles <= 10:
        return turtles
      else:
        print("Please enter a number between 2 and 10.")
    else:
      print("Invalid input. Please enter a valid number.")

def race(colors):
  turtles = create_turtles(colors)

  while True:
    for racer in turtles:
      distance = random.randrange(1, 10)
      racer.forward(distance)

      x,y = racer.pos()
      if y >= HEIGHT//2 - 20:
        return colors[turtles.index(racer)]

def create_turtles(colors):
  turtle_list = []
  spacingx = WIDTH // (len(colors) + 1)
  for i, color in enumerate(colors):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.left(90)
    new_turtle.penup()
    new_turtle.setpos(-WIDTH//2 + (i+1)*spacingx, -HEIGHT//2 + 20)
    new_turtle.pendown()
    turtle_list.append(new_turtle)
  return turtle_list

def init_turtle():
  screen = turtle.Screen()
  screen.setup(WIDTH, HEIGHT)
  screen.title("Turtle Racing")

turtles = get_number_of_turtles()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:turtles]
winner = race(colors)
print(f"The winner is the {winner} turtle!")
time.sleep(5)