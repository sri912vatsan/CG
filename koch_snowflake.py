# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:18:27 2023

@author: 20pt34
"""

import turtle 

#shape = ("turtle")
#speed(0)


def koch_snowflake(t,iterations,length,shorten,angle):
    
    if iterations==0:
        t.forward(length)
    else:
        iterations = iterations-1
        length = length/shorten 
        
        koch_snowflake(t,iterations,length,shorten,angle)
        t.left(angle)
        koch_snowflake(t,iterations,length,shorten,angle)
        
        t.right(angle*2)
        koch_snowflake(t, iterations, length, shorten, angle)
        
        t.left(angle)
        koch_snowflake(t,iterations,length,shorten,angle)
        
t = turtle.Turtle()
t.hideturtle()
t.speed(10)

t.color('Green')
t.begin_fill()
for i in range(3):
  koch_snowflake(t, 3, 200, 3, 60)
  t.right(120)
t.end_fill()
  
turtle.mainloop()
    
    
    
    