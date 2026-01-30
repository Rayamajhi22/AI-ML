#NummPY Example
import numpy as np

arr = np.array([10,20,30,40])
print("Array:",arr)
print("Mean:",np.mean(arr))
print("sum:",np.sum(arr))

#Pandas Example
import pandas as pd
data = {
    "Name": ["A","B","C"],
    "Marks": [80,70,90]
}
df = pd. DataFrame(data)
print(df)
print("\nDescription:\n",df.describe())



#Matplotlib example
import matplotlib.pyplot as plt

marks = [80,70,90,85,60]
plt.plot(marks)
plt.title("Student Marks Trend")
plt.xlabel("Student Index")
plt.ylabel("Marks")
plt.show()