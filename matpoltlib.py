#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
x=np.arange(0,10,0.1)
y=2*x+5
plt.plot(x,y)
plt.show()


# In[15]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
x=np.arange(0,10,0.1)
y=2*x+ 5
fig=plt.figure(figsize=(10,5))
plt.plot(x,y,linewidth=2.0,linestyle=":",color="red",alpha=0.5,marker="o")
plt.title("line plot Demo")
plt.xlabel("x-axis")
plt.ylabel("y=axis")
plt.legend(["line1"],loc="best")
plt.grid(True)
plt.show()


# In[24]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
x=np.arange(0,10,0.1)

y=2*x + 5
y1=5*x +6
fig=plt.figure(figsize=(10,5))
plt.plot(x,y,linewidth=2.0,linestyle=":",color="red",alpha=0.5,marker="+")
plt.plot(x,y1,linewidth=2.0,linestyle=":",color="b",alpha=0.8,marker="x")
plt.title("line plot Demo")
plt.xlabel("x-axis")
plt.ylabel("y=axis")
plt.legend(["line1","myline"],loc="best")
plt.grid(True)
plt.show()


# In[25]:


x=np.arange(0,10,1)
y=2*x+5
y2=3*x+10
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("Graph1")
plt.subplot(1,2,2)
plt.plot(x,y2)
plt.title("Graph2")
plt.show()


# In[29]:


data={"apple":20,"mango":15,"lemon":30,"orange":10}
name=list(data.keys())
values=list(data.values())
fig=plt.figure(figsize=(10,5))
plt.bar(name,values)
plt.show()


# In[33]:


data={"apple":20,"mango":15,"lemon":30,"orange":10}
name=list(data.keys())
values=list(data.values())

fig=plt.figure(figsize=(10,5))

plt.barh(name,values)
plt.title("bar graph Demo")
plt.xlabel("fruits")
plt.ylabel("quantity")
plt.show()


# In[46]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

a=[10,20,30,40,50,60,70,80,90]
b=[5,3,2,5,6,1,4,2]
x=[1,2,3,42,3,2,1,2]

plt.scatter(a,b)
plt.scatter(a,x)
plt.show()


# In[55]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

numbers=[10,12,16,19,11,20,26,28,30,38,35,48,60,68,64,62,70,78,75,79,85,94,95]
plt.hist(numbers,bins=([0,20,40,60,80,100])
         
plt.show()


# In[3]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

total=[20,4,1,30,20,10,20,70,30,10]

order=[10,3,1,15,17,2,30,44,2,1]
discount=[30,10,20,5,10,20,50,60,20,45]
data= list([total,order,discount])
plt.boxplot(data,showmeans=True)
plt.title("box plot Demo")
plt.grid(True)
plt.show()


# In[4]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

total=[20,4,1,30,20,10,20,70,30,10]

order=[10,3,1,15,17,2,30,44,2,1]
discount=[30,10,20,5,10,20,50,60,20,45]
data= list([total,order,discount])
plt.violinplot(data,showmeans=True)
plt.title("violin plot Demo")
plt.grid(True)
plt.show()

