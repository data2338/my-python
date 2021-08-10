#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle 
t = turtle.Turtle()
 
m = 300;
n = 250;
 
# vẽ cạnh đầu tiên
t.forward(m) # đi thẳng với m đơn vị
t.left(90)   # quay một góc 90 độ
 
# vẽ cạnh thứ hai
t.forward(n) # đi thẳng với n đơn vị
t.left(90)   # quay một góc 90 độ
 
# vẽ cạnh thứ ba
t.forward(m) # đi thẳng với m đơn vị
t.left(90)   # quay một góc 90 độ
 
# vẽ cạnh thứ tư
t.forward(n) # đi thẳng với n đơn vị
t.left(90)   # quay một góc 90 độ

turtle.mainloop()


# In[ ]:




