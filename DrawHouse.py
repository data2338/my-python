#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle
turtle.Screen().bgcolor("cadetblue1")

t = turtle.Turtle()
n = 200

t.pensize(2)

t.penup()
t.goto(-200,-200)
t.pendown()

# VẼ NHÀ
#vẽ tường 1
t.fillcolor("blue")
t.begin_fill()
t.forward(n) 
t.left(90)   
t.forward(n)
t.left(90)
t.forward(n) 
t.left(90)
t.forward(n)
t.left(90)
t.end_fill()

#vẽ cửa ra vào
t.fillcolor("aquamarine3")
t.goto(-135,-200)
t.begin_fill()
t.forward(70) 
t.left(90)   
t.forward(100)
t.left(90)
t.forward(70) 
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

#vẽ tường bên
t.fillcolor("gold")
t.goto(0,-200)
t.begin_fill()
t.left(30)
t.forward(120) 
t.left(60)   
t.forward(200)
t.left(120)
t.forward(120) 
t.left(60)
t.forward(200)
t.end_fill()

#Vẽ cửa sổ
t.fillcolor("firebrick1")
t.penup()
t.goto(40,-80)
t.pendown()

t.begin_fill()
t.left(120)
t.forward(40) 
t.left(60)   
t.forward(40)
t.left(120)
t.forward(40) 
t.left(60)
t.forward(40)
t.end_fill()

#vẽ mái nhà
t.penup()
t.goto(-200,0)
t.pendown()

t.fillcolor("hotpink")
t.begin_fill()
t.left(135)
t.forward(141)
t.right(90)
t.forward(141)
t.end_fill()

t.fillcolor("lightsalmon")
t.begin_fill()
t.left(75)
t.forward(120)
t.left(105)
t.forward(141)
t.left(75)
t.forward(120)
t.end_fill()

#vẽ thân cây
t.setheading(0)
t.penup()
t.goto(300,-220)
t.fillcolor("tomato4")
t.begin_fill()
t.pendown()
t.forward(50)
t.setheading(90)
t.forward(110)
t.setheading(180)
t.forward(50)
t.setheading(270)
t.forward(110)
t.end_fill()

#vẽ lá cây
t.setheading(0)
t.penup()
t.goto(250,-110)
t.fillcolor("aquamarine3")
t.begin_fill()
t.forward(150)
t.setheading(135)
t.forward(106)
t.left(90)
t.forward(106)
t.end_fill()

t.setheading(0)
t.penup()
t.goto(250,-60)
t.begin_fill()
t.forward(150)
t.setheading(135)
t.forward(106)
t.left(90)
t.forward(106)
t.end_fill()

t.setheading(0)
t.penup()
t.goto(250,-10)
t.fillcolor("aquamarine3")
t.begin_fill()
t.forward(150)
t.setheading(135)
t.forward(106)
t.left(90)
t.forward(106)
t.end_fill()


#vẽ mặt trời
t.penup()
t.goto(200,250)
t.pencolor("black")
t.pendown()
t.setheading(0)
t.forward(75)
t.backward(75)
t.left(45)
t.forward(75)
t.backward(75)
t.left(45)
t.forward(75)
t.backward(75)
t.left(45)
t.forward(75)
t.backward(75)
t.left(45)
t.forward(75)
t.backward(75)
t.left(45)
t.forward(75)
t.backward(75)
t.left(45)
t.forward(75)
t.backward(75)
t.left(45)
t.forward(75)
t.backward(75)

t.penup()
t.goto(165,250)
t.setheading(270)
t.pendown()
t.fillcolor("gold")
t.begin_fill()
t.circle(35)
t.end_fill()


turtle.done()
turtle.mainloop()


# In[ ]:





# In[ ]:




