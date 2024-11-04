""" 
Day 25 - Planetary Motion Simulator
"""

import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title = "Planetary Motion Simulator"


def draw_planet(color, radius, angle):
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(color)
    planet.penup()
    planet.goto(radius * math.cos(angle), radius * math.sin(angle))
    planet.pendown()
    return planet


sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(3)
sun.penup()
sun.goto(0, 0)
sun.pendown()

planets = [
    {"color": "orange", "radius": 100, "speed": 0.02},
    {"color": "yellow", "radius": 150, "speed": 0.015},
    {"color": "blue", "radius": 200, "speed": 0.01},
]

planet_turtles = []
for planet in planets:
    angle = 0
    planet_turtle = draw_planet(planet["color"], planet["radius"], angle)
    planet_turtle.angle = angle
    planet_turtle.radius = planet["radius"]
    planet_turtle.speed = planet["speed"]
    planet_turtles.append(planet_turtle)

while True:
    for planet_turtle in planet_turtles:
        planet_turtle.angle += planet_turtle.speed
        x = planet_turtle.radius * math.cos(planet_turtle.angle)
        y = planet_turtle.radius * math.sin(planet_turtle.angle)
        planet_turtle.goto(x, y)

turtle.done()
