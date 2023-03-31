# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:04:46 2023

@author: 20pt34
"""

import turtle
import sys

MAX_ITER = 100
def mand(c):
	z = 0
	n = 0
	while abs(z) <= 2 and n < MAX_ITER:
		z = z*z + c
		n = n + 1
	return n

# Plot window
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

screen = turtle.Screen()
(WIDTH,HEIGHT) = screen.screensize()

turtle.colormode(255)
turtle.tracer(0, 0)
turtle.speed("fastest") # fastest

for x in range(0,WIDTH):
	for y in range(0,HEIGHT):
		c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
		IM_START + (y / HEIGHT) * (IM_END - IM_START))
		# Compute the number of iterations
		m = mand(c)
		# The color depends on the number of iterations
		color = 255 - int(m * 255 / MAX_ITER)
		# Plot the point
		t = turtle.Turtle()
		t.penup()
		t.setpos(x,y)
		t.pencolor((color,color,color))
		t.dot()
	if x%50==0:
		print("x is ",x, "needs to be 400 keep waiting")

turtle.update()
	
turtle.done()