#!/usr/bin/env python
# coding: utf-8

# In[1]:


a= 10 
name= "victor"
salary= 102.33
print(a)
print(name)
print(salary)


# In[3]:


a=10 
b=20
c=30
a=b=c=10
print(a)
print(b)
print(c)


# In[7]:


x=20
y=30
z=40
x,y,z=20,30,40
print(y,z)


# In[8]:


a=b=c=10
z,y,x=30,40,50
print(x,a)


# In[9]:


A=630
a=10
print(a)
print(A)


# In[12]:


NAME="JHONE" #dubble quotes
print(NAME)
name1='killer' #single quotes
print(name1)


# In[13]:


multiline=""" string
string1
string2 """
print(multiline)


# In[14]:


text="hello-world"
print(text)


# In[18]:


val=10
val1= "none"
print(val)
print(val1)


# In[19]:


a=10 #multiple *
a*=10
print(a)


# In[20]:


var=20 # add
var+=80
print(var)


# In[21]:


var=120
var-=20
print(var)


# In[22]:


a=10<10 and 2>1   #false and true= fasle
print(a)


# In[23]:


7|5 #binary form 1,2,4,8,16,32


# In[24]:


7&5


# In[25]:


10>>2


# In[26]:


10<<2 #10100 :40


# In[27]:


10<<3 #1010000:80


# In[31]:


pets=["dog","cat","wolf"]
"lion" in pets


# In[32]:


"wolf" in pets


# In[33]:


"me" in "appoinment"


# In[34]:


a=10
name="jail"
salay=2003.3
print(type(a))
print(type(name))
print(type(salary))


# In[46]:


var1="hello-world"
var2="python class"
print(var1[0])
print(var1[:5])
print(var2[:7])
print(var1[-1])
print(var2[-5:])


# In[47]:


str="attachment"
str.find("me")


# In[49]:


str="attachment"
str.find("n")


# In[50]:


str="replacment"
str.replace("ment","")


# In[51]:


str="attachment"
str.replace("attach","t")


# In[61]:


str='world' , 'world1' , 'world2'
str.split(',')


# In[64]:


str5=["world" , "world1" , "world2"]
str5.split["world"]


# In[66]:


str="python"
str.count("y")


# In[69]:


str1="krrishjack"
str1.count("r")


# In[71]:


str1.upper()


# In[73]:


str1=str1.upper()
str1.count("R")


# In[74]:


str="python"
max(str)


# In[76]:


str1="jack"
min(str1)


# In[78]:


mygroup=("a","b","c","d")
mygroup+=("f",)
print(mygroup)


# In[80]:


group=('a', 'b', 'c', 'd', 'f')
group*3


# In[81]:


group=('a', 'b', 'c', 'd', 'f')
group[2]


# In[92]:


group1=('a', 'b', 'c', 'd', 'f')
group1[1:3]


# In[95]:


mylist=["a",1,3.450,"python"]
mylist+=["d"]
print(mylist)


# In[96]:


mylist=['a', 1, 3.45, 'python', 'd']
mylist2=["kill",20]
mylist+=mylist2
print(mylist)


# In[97]:


mylist=['a', 1, 3.45, 'python', 'd']
mylist*2


# In[98]:


mylist=['a', 1, 3.45, 'python', 'd'] #+1 forlist
mylist[1:4]


# In[100]:


mylist=['a', 1, 3.45, 'python', 'd']
mylist.append("j")
print(mylist)


# In[102]:


mylist=['a', 1, 3.45, 'python', 'd']
mylist.extend(["ki","ka"])
print(mylist)


# In[104]:


mylist=['a', 1, 3.45, 'python', 'd']
mylist.insert(4,"don")
print(mylist)


# In[106]:


mydict={1:'jhon',2:'bob',3:'alex'}
print(mydict)


# In[107]:


mydict={1: 'jhon', 2: 'bob', 3: 'alex'}
mydict[1]


# In[108]:


mydict={1: 'jhon', 2: 'bob', 3: 'alex'}
len(mydict)


# In[109]:


mydict={1: 'jhon', 2: 'bob', 3: 'alex'}
mydict.keys()


# In[110]:


mydick={1: 'jhon', 2: 'bob', 3: 'alex'}
mydict.values()


# In[112]:


myset={1,2,3}
print(myset)


# In[113]:


mys1={1, 2, "c"}
mys2={1,"b","c"}
mys1 | mys2 #all common will be out


# In[114]:


mys1={1, 2, "c"}
mys2={1,"b","c"}
mys1&mys2 #only common will be out 


# In[115]:


mys1={1, 2, "c"}
mys2={1,"b","c"}
mys1 - mys2  #give only value which is uniqe and first set


# In[116]:


mys1={1, 5, "c"}
mys2={1,"b","c"}
mys1 - mys2


# In[117]:


fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)


# In[14]:


x=lambda a:a+10
print(x(5))


# In[16]:


x=lambda a:a+10
print(x(10))

