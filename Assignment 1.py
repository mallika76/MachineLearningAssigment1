#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

# Create a random vector of size 15 with integers in the range 1-20
random_vector = np.random.randint(1, 21, 15)
print(random_vector)
print("\n")

# Reshape the array to 3 by 5
reshaped_array = random_vector.reshape(3, 5)
# Print array shape
print("shape:", reshaped_array.shape)
print("Array Shape:",reshaped_array)

# Replace the maximum value in each row with 0
for i in range(reshaped_array.shape[0]):
    reshaped_array[i, np.argmax(reshaped_array[i])] = 0
print("\n")
# Print the modified array
print("Modified array:")
print(reshaped_array)



# In[2]:


import numpy as np
x = np.array([[1, 3, 6], [6, 8, 10],[4,5,6],[1,3,2]], np.int32)
print(type(x))	
print(x.shape)
print(x.dtype)


# In[3]:


# importing numpy library
import numpy as np

# create numpy 2d-array
m= np.array([[3, -2],[1, 0]])

# finding eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(m)

# printing eigen values
print("Print the Eigenvalues of the given square array:\n",eigenvalues)

# printing eigen vectors
print("Print Right eigenvectors of the given square array:\n",eigenvectors)


# In[4]:


import numpy as np

# Given array
array = np.array([[0, 1, 2],
                  [3, 4, 5]])

# the sum of diagonal elements
dia= np.trace(array)
print("Sum of diagonal elements:", dia)


# In[5]:


import numpy as np
Array = np.array([[1, 2, 3], [4, 5, 6]])
y = Array.reshape(3,2)
print("Reshape 3x2:")
print(y)
z = Array.reshape(2,3)
print("Reshape 2x3:")
print(z)


# In[6]:


import matplotlib.pyplot as plt
# Data to plot
Programminglanguages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ["#0D70B4", "#ff7f0e", "#37c837", "#d62728", "#9467bd", "#B45C1F"]
# explode 1st slice
explode = (0.1, 0, 0, 0,0,0)  
# Plot
plt.pie(popuratity, explode=explode, labels=Programminglanguages, colors=colors,
autopct='%1.1f%%', shadow=True,startangle=120)

plt.axis('equal')
plt.show()



# In[ ]:




