#!/usr/bin/env python
# coding: utf-8

# In[4]:


import turtle
pen = turtle.Turtle()

pen.pensize(1)
max_rad = int(input("Nhập khoảng cách: "))
d = 0

while True:
    d += 0.5
    pen.forward(d)
    pen.right(30)
    if pen.distance(0,0) >= max_rad:
        break

# Cách 2: xoắn ốc mềm mại hơn         
#while True:
#    pen.circle(d, 45)
#    d += 2
#    if d >= max_rad:
#        break        
        
turtle.done()
turtle.mainloop()

