#!/usr/bin/env python
# coding: utf-8

# In[4]:


import turtle
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
pen = turtle.Turtle()
pen.pensize(2)
r = 100
hdg = 0

while hdg <= 360:
    pen.setheading(hdg)
    pen.pencolor(random.choice(colors))
    for i in range(2):
        pen.circle(r,90)
        pen.circle(r/2,90)
    hdg += 15
    

turtle.done()
turtle.mainloop()


# In[ ]:





# In[ ]:




