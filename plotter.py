#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install matplotlib seaborn')


# In[ ]:





# In[12]:


import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create a list to store coordinates and their corresponding file names
all_coordinates = []
file_labels = []  # Store the file names for labeling

# List of text file names and corresponding colors
file_data = [
    {"filename": r"C:\Users\bryso\Downloads\1_Data\1_Data\group5\classification\linearlySeparable\class1_train.txt", "color": "blue"},
    {"filename": r"C:\Users\bryso\Downloads\1_Data\1_Data\group5\classification\linearlySeparable\class2_train.txt", "color": "green"},
    {"filename": r"C:\Users\bryso\Downloads\1_Data\1_Data\group5\classification\linearlySeparable\class3_train.txt", "color": "red"},
]  # Add your file names and corresponding colors here

# Read coordinates from each file and append to the list
for data in file_data:
    file_name = data["filename"]
    color = data["color"]
    with open(file_name, 'r') as file:
        coordinates = [line.strip().split() for line in file]
        all_coordinates.extend(coordinates)
        file_labels.extend([os.path.splitext(file_name)[0]] * len(coordinates))  # Store file names for labeling

# Convert the coordinates to floats
all_coordinates = [(float(x), float(y)) for x, y in all_coordinates]

# Separate the coordinates into x and y lists
x_coordinates, y_coordinates = zip(*all_coordinates)

# Create a scatter plot using Seaborn with different colors for each file
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.scatterplot(x=x_coordinates, y=y_coordinates, hue=file_labels, palette=[data["color"] for data in file_data], s=100)

# Set plot labels and title
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")
plt.title("Scatter Plot of Coordinates")

# Show the legend
plt.legend(title="File Names")

# Shift the legend to the bottom of the screen
plt.legend(title="File Names", bbox_to_anchor=(0.5, -0.2), loc="upper center")

plt.savefig("linearlySeparable.jpg", format="jpg")


# Show the plot
plt.show()


# In[13]:


# Create a list to store coordinates and their corresponding file names
all_coordinates = []
file_labels = []  # Store the file names for labeling

# List of text file names and corresponding colors
file_data = [
    {"filename": r"C:\Users\bryso\Downloads\1_Data\1_Data\group5\classification\nonlinearlySeparable\class1_train.txt", "color": "blue"},
    {"filename": r"C:\Users\bryso\Downloads\1_Data\1_Data\group5\classification\nonlinearlySeparable\class2_train.txt", "color": "green"}
]  # Add your file names and corresponding colors here

# Read coordinates from each file and append to the list
for data in file_data:
    file_name = data["filename"]
    color = data["color"]
    with open(file_name, 'r') as file:
        coordinates = [line.strip().split() for line in file]
        all_coordinates.extend(coordinates)
        file_labels.extend([os.path.splitext(file_name)[0]] * len(coordinates))  # Store file names for labeling

# Convert the coordinates to floats
all_coordinates = [(float(x), float(y)) for x, y in all_coordinates]

# Separate the coordinates into x and y lists
x_coordinates, y_coordinates = zip(*all_coordinates)

# Create a scatter plot using Seaborn with different colors for each file
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.scatterplot(x=x_coordinates, y=y_coordinates, hue=file_labels, palette=[data["color"] for data in file_data], s=100)

# Set plot labels and title
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")
plt.title("Scatter Plot of Coordinates")

# Show the legend
plt.legend(title="File Names")

# Shift the legend to the bottom of the screen
plt.legend(title="File Names", bbox_to_anchor=(0.5, -0.2), loc="upper center")

plt.savefig("nonlinearlySeparable.jpg", format="jpg")


# Show the plot
plt.show()


# In[14]:


# Create a list to store coordinates and their corresponding file names
all_coordinates = []
file_labels = []  # Store the file names for labeling

# List of text file names and corresponding colors
file_data = [
    {"filename": r"C:\Users\bryso\Downloads\1_Data\1_Data\group5\classification\overlapping\class1_train.txt", "color": "blue"},
    {"filename": r"C:\Users\bryso\Downloads\1_Data\1_Data\group5\classification\overlapping\class2_train.txt", "color": "green"},
    {"filename": r"C:\Users\bryso\Downloads\1_Data\1_Data\group5\classification\overlapping\class3_train.txt", "color": "red"},
]  # Add your file names and corresponding colors here

# Read coordinates from each file and append to the list
for data in file_data:
    file_name = data["filename"]
    color = data["color"]
    with open(file_name, 'r') as file:
        coordinates = [line.strip().split() for line in file]
        all_coordinates.extend(coordinates)
        file_labels.extend([os.path.splitext(file_name)[0]] * len(coordinates))  # Store file names for labeling

# Convert the coordinates to floats
all_coordinates = [(float(x), float(y)) for x, y in all_coordinates]

# Separate the coordinates into x and y lists
x_coordinates, y_coordinates = zip(*all_coordinates)

# Create a scatter plot using Seaborn with different colors for each file
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.scatterplot(x=x_coordinates, y=y_coordinates, hue=file_labels, palette=[data["color"] for data in file_data], s=100)

# Set plot labels and title
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")
plt.title("Scatter Plot of Coordinates")

# Show the legend
plt.legend(title="File Names")

# Shift the legend to the bottom of the screen
plt.legend(title="File Names", bbox_to_anchor=(0.5, -0.2), loc="upper center")

plt.savefig("overlapping.jpg", format="jpg")


# Show the plot
plt.show()


# In[ ]:




