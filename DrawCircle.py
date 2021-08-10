#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle

#đặt kích thước viền cho hình tròn là 5
turtle.pensize (5)
 
#đặt màu sắc cho viền hình tròn là màu đỏ
turtle.pencolor ("red")

#đặt màu nền cho hình tròn là màu xanh
turtle.fillcolor ("blue")
turtle.begin_fill()

#đặt bán kính của hình tròn là 100
turtle.circle (100)
turtle.end_fill()
turtle.done

turtle.mainloop()


# In[1]:


import turtle

#đặt kích thước viền cho hình tròn là 5
turtle.pensize(5)

#đặt màu sắc cho viền hình tròn là màu xanh
turtle.pencolor("blue")

#đặt màu nền cho hình tròn là màu đỏ
turtle.fillcolor("red")
turtle.begin_fill()

#đặt bán kính của hình tròn là 150
turtle.circle (150)
turtle.end_fill()
turtle.done

turtle.mainloop()


# In[3]:


import turtle

#đặt kích thước viền cho hình tròn là 5
turtle.pensize(5)

#đặt màu sắc cho viền hình tròn là màu đỏ
turtle.pencolor ("red")

#tuỳ chỉnh điểm bắt đầu vẽ hình tròn
turtle.Turtle().goto(-40, 120)
#đặt màu nền cho hình tròn là màu đỏ
turtle.fillcolor ("red")
turtle.begin_fill()

#đặt bán kính của hình tròn là 150
turtle.circle (150)
turtle.end_fill()

turtle.mainloop()

