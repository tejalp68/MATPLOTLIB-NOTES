#!/usr/bin/env python
# coding: utf-8

# # Matplotlib

# In[1]:


import matplotlib.pyplot as plt


# ## linear Graph

# In[2]:


x = [1,2,3,4]
y = [10,8,5,6]
plt.plot(x,y,color ="red" ,marker="o")
plt.show()


# In[3]:


x = [1,9,3,4]
y = [10,8,5,6]
plt.plot(x,color ="red" ,marker="o")
plt.plot(y,color ="green" ,marker="o")
plt.show()


# ## BAR plot

# In[4]:


x=["Rani","Kaveri","Radhika","Darshan","Ram"]
y = [98,99,86,75,85]
c=['red','green','yellow','blue','violet']
plt.bar(x,y ,color=c)
plt.show()


# In[5]:


plt.barh(x,y,color ="#FF00FF",height=0.5)
plt.show()


# In[6]:


plt.bar(x,y,color ="#0892D0")
plt.show()


# In[7]:


plt.bar(x,y,width = 0.5)
plt.show()


# In[8]:


x = [1,2,3,4,5]
y = [10,8,5,6,23]
plt.scatter(x,y,color ="red" ,marker="+",s = 150)
plt.show()


# In[9]:


x = [1,1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
     11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y = [5, 35,12, 9, 15, 7, 18, 10, 20, 14, 25,
     22, 17, 30, 28, 24, 35, 32, 40, 38, 45]
c =[ 
    'red','black' ,'blue', 'green', 'orange', 'purple',
    'brown', 'pink', 'gray', 'olive', 'cyan',
    'magenta', 'yellow', 'black', 'teal', 'navy',
    'maroon', 'gold', 'lime', 'indigo', 'coral'
]
plt.scatter(x,y ,color=c,s=700)
plt.show()


# day 2

# In[13]:


import pandas as pd
import numpy as np
from PIL import Image

#TO READ IMAGE
fname = r'hhh.jpg'

image =Image.open(fname).convert('L')
plt.imshow(image ,cmap ="gray")
plt.show()


# In[21]:


fname = r'hhh.png'

image =Image.open(fname).convert('L')
plt.imshow(image ,cmap ="Blues")
plt.show()


# In[22]:


fname = r'hhh.png'

image =Image.open(fname).convert('L')
plt.imshow(image ,cmap ="Accent")
plt.show()


# In[24]:


fname = r'hhh.png'

image =Image.open(fname).convert('L')
plt.imshow(image ,cmap ="BrBG")
plt.show()


# In[26]:


fname = r'hhh.png'

image =Image.open(fname).convert('L')
plt.imshow(image ,cmap ="plasma")
plt.show()


# In[41]:


fname = r'rb2.jpg'

image =Image.open(fname).convert('L')
plt.imshow(image ,cmap ="rainbow")
plt.savefig('hey.jpg')
plt.show()


# In[39]:


fname = r'rb1.jpg'

image =Image.open(fname).convert('L')
plt.imshow(image ,cmap ="gray")
image.save("rb1_g.jpg")
plt.show()


# In[43]:


import matplotlib.pyplot as plt
from PIL import Image

image = Image.open("hhh.jpg").convert("L")

plt.imshow(image, cmap="gray")
plt.axis("off")    ## removes the axis that displays

# SAVE the figure
plt.savefig("hhh_gray_matplotlib.png", bbox_inches="tight", pad_inches=0)
plt.show()
## bbox_inches="tight" removes white borders
## pad_inches=0 removes padding


# In[44]:


x = [1,2,3,4]
y = [10,8,5,6]
plt.plot(x,y,color ="red" ,marker="o")
plt.bar(x,y,width = 0.5)
plt.legend()
plt.show()


# In[78]:


x = [1,2,3,4]
y = [10,8,5,6]
plt.subplot(1,2,1)
plt.plot(x,y,color ="red" ,marker="o")
plt.subplot(1,2,2)
plt.bar(x,y,width = 0.5)
plt.show()


# ## PIE CHART

# In[76]:


import matplotlib.pyplot as plt

# Values
values = [40, 25, 20, 15]

# Labels
labels = ['Python', 'Java', 'C++', 'Others']

# plt.figure()
plt.pie(values, labels=labels, autopct='%1.1f%%' )
plt.title('Programming Language Usage')
plt.legend()
plt.show()


# This shows the pie chart with 90 degree 
# that looks more efficient to understand

# In[75]:


import matplotlib.pyplot as plt

# Values
values = [40, 25, 20, 15]

# Labels
labels = ['Python', 'Java', 'C++', 'Others']

# plt.figure()
plt.pie(values, labels=labels, autopct='%1.f%%',startangle=90)  # autopct='%1.1f%%' → shows percentage with 1 decimal
plt.title('Programming Language Usage')
plt.legend()
plt.show()


# In[140]:


values = [40, 25, 20, 15]

# Labels
labels = ['Python', 'Java', 'C++', 'Others']
plt.subplot(2,2,1)
plt.pie(values, labels=labels, autopct='%1.f%%',startangle=90)  # autopct='%1.1f%%' → shows percentage with 1 decimal
plt.title('Programming Language Usage')
x = [1,2,3,4]
y = [10,8,5,6]
plt.subplot(2,2,2)
plt.plot(x,y,color ="red" ,marker="o")

plt.subplot(2,2,3)
maths = [45, 55, 65, 75, 85,150]
science = [50, 60, 70, 80, 90,190]

plt.boxplot([maths, science], tick_labels=["Maths", "Science"])
plt.ylabel("Marks")
plt.title("Marks Comparison")
plt.subplot(2,2,4)
x = [1,2,3,4]
y = [10,8,5,6]
plt.plot(x,y,color ="red" ,marker="o")
plt.bar(x,y,width = 0.5)


plt.show()


# ## HISTOGRAM

# In[110]:


import matplotlib.pyplot as plt

marks = [45, 55, 60, 70,71,74,77, 75,78,79, 80, 85, 90, 90,99,98]
labels =["marks"]

plt.hist(marks,bins =10,label=labels,edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.legend()

plt.show()


# In[94]:


import matplotlib.pyplot as plt

marks = [45, 55, 60, 70, 75, 80, 85, 90, 95]
labels =["A","B","C","D","E","F","G","H","I"]

plt.hist(marks,bins =10,label=labels,edgecolor="black",orientation='horizontal')
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.legend()

plt.show()


# In[97]:


import matplotlib.pyplot as plt

marks = [45, 55, 60, 70, 75, 80, 85, 90, 95]
labels =["A","B","C","D","E","F","G","H","I"]

plt.hist(marks,bins =10,label=labels,edgecolor="black",cumulative=True)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.legend()

plt.show()


# In[114]:


import matplotlib.pyplot as plt

marks = [45, 55, 60, 70, 75, 80, 85, 90, 95]
labels =["marks"]

plt.hist(marks,bins =10,label=labels,edgecolor="black",density=True)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.legend()

plt.show()


# In[116]:


marks = [45, 55, 60, 70, 75, 80, 85, 90, 95]
import matplotlib.pyplot as plt

plt.boxplot(marks)
plt.title("Marks Distribution")
plt.ylabel("Marks")
plt.show()


# In[117]:


## BOX plot with outliers 


# In[118]:


marks = [45, 55, 60, 70, 71, 74, 75, 80, 85, 90, 150]

plt.boxplot(marks)
plt.show()


# In[119]:


marks = [45, 55, 60, 70, 71, 74, 75, 80, 85, 90, 150]

plt.boxplot(marks ,vert =False)
plt.show()


# In[120]:


## COMPARING two box plots


# In[127]:


maths = [45, 55, 65, 75, 85]
science = [50, 60, 70, 80, 90]

plt.boxplot([maths, science], tick_labels=["Maths", "Science"])
plt.ylabel("Marks")
plt.title("Marks Comparison")
plt.show()


# In[128]:


maths = [45, 55, 65, 75, 85,150]
science = [50, 60, 70, 80, 90,190]

plt.boxplot([maths, science], tick_labels=["Maths", "Science"])
plt.ylabel("Marks")
plt.title("Marks Comparison")
plt.show()


# In[129]:


import pandas as pd

df = pd.DataFrame({
    "Maths": maths,
    "Science": science
})

df.boxplot()



# In[131]:


plt.boxplot(
    marks,
    showmeans=True,
    patch_artist=True
)
plt.show()


# In[142]:


Age=[10,19,18,20,21,22,18,]
plt.plot(Age)
plt.show()

plt.figure()   # new figure
Salary=[100,200,410,150,800]
plt.plot(Salary)
plt.show()


# In[145]:


values = [40, 25, 20, 15]

# Labels
labels = ['Python', 'Java', 'C++', 'Others']
plt.subplot(2,2,1)
plt.pie(values, labels=labels, autopct='%1.f%%',startangle=90)  # autopct='%1.1f%%' → shows percentage with 1 decimal
plt.title('Programming Language Usage')
x = [1,2,3,4]
y = [10,8,5,6]
plt.subplot(2,2,2)
plt.plot(x,y,color ="red" ,marker="o")

plt.subplot(2,2,3)
maths = [45, 55, 65, 75, 85,150]
science = [50, 60, 70, 80, 90,190]

plt.boxplot([maths, science], tick_labels=["Maths", "Science"])
plt.ylabel("Marks")
plt.title("Marks Comparison")
plt.subplot(2,2,4)
x = [1,2,3,4]
y = [10,8,5,6]
plt.plot(x,y,color ="red" ,marker="o")
plt.bar(x,y,width = 0.5)


plt.show()


# In[150]:


values = [40, 25, 20, 15]

# Labels
labels = ['Python', 'Java', 'C++', 'Others']
plt.subplot(2,2,1)
plt.pie(values, labels=labels, autopct='%1.f%%',startangle=90)  # autopct='%1.1f%%' → shows percentage with 1 decimal
plt.title('Programming Language Usage')
x = [1,2,3,4]
y = [10,8,5,6]

plt.subplot(2,2,2)
plt.plot(x,y,color ="red" ,marker="o")

plt.subplot(2,2,3)
maths = [45, 55, 65, 75, 85,150]
science = [50, 60, 70, 80, 90,190]
plt.boxplot([maths, science], tick_labels=["Maths", "Science"])
plt.ylabel("Marks")
plt.title("Marks Comparison")

plt.subplot(2,2,4)
x = [1,2,3,4]
y = [10,8,5,6]
plt.plot(x,y,color ="red" ,marker="o")
plt.bar(x,y,width = 0.5)


plt.show()


# In[ ]:




