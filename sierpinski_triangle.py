# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 15:05:34 2023

@author: 20pt34
"""

import turtle 

w,h = 600,400

screen = turtle.Screen()
screen.setup(w,h)
screen.screensize(4*w,4*h)
screen.bgcolor('yellow')
turtle.speed(10)

l = turtle.Turtle()
l.speed(5)
l.setpos(-w//3,-h//3)
l.color('green')

#l-system 
gens = 3
axiom = 'F'
chr1, rule_1 = 'F', 'F-G+F+G-F'
chr2, rule_2 = 'G', 'GG'
step = 8
angle = 120

def apply(axiom):
    return ''.join([rule_1 if chr==chr1 else rule_2 if chr==chr2 else chr 
                    for chr in axiom])

def get_result(gens,axiom):
    for gen in range(gens):
        axiom = apply(axiom)
    return axiom 

for gen in range(gens):
    turtle.pencolor('white')
    turtle.goto(-w// 2 + 60,h // 2 - 100)
    turtle.clear()
    turtle.write(f'generation: {gen}', align="left", font=("Arial", 60, "normal"))

    axiom = get_result(gens,axiom)
    for chr in axiom:
        if chr == chr1 or chr == chr2:
            l.forward(step)
        elif chr == '+':
            l.right(angle)
        elif chr == '-':
            l.left(angle)

    axiom = apply(axiom)

screen.exitonclick()
    


