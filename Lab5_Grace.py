
# Exercise 1

import matplotlib.pyplot as plt

# data
x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1, 4, 9, 16, 25, 36]

#plot the data
plt.plot(x,y)

#add labels
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# add a title
plt.title("Plot of X vs Y")

# show the plot
plt.show()

# Exercise 2

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1, 4, 9, 16, 25, 36]

# change the color and style
plt.plot(x, y, color='green', linestyle='--', marker='o')

# add a grid
plt.grid(True)
plt.title("Customized Plots")

plt.show()

# Exercise 3

import matplotlib.pyplot as plt

# Create a bar plot to visualize categories and values.

categories = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']
values = [10, 15, 7, 12, 5]

plt.bar(categories, values, color='pink')
plt.xlabel("Fruits")
plt.ylabel("Values")
plt.title("Bar chart of Fruit and Their Values")

plt.show()

# Exercise 4

import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 1, 500) # 500 data points from a normal distribution

plt.hist(data, bins=20, edgecolor='black', color='skyblue', alpha=0.7)
plt.title('500 data points from a normal distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Exercise 5

import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50) # 50 random x-values between 0 and 1
y = np.random.rand(50) # 50 random y-values between 0 and 1

# scatter plot
plt.scatter(x,y, color='green', alpha=0.7)
plt.title('Scatter Plot of Random Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

# Exercise 6

import matplotlib.pyplot as plt
import numpy as np

# Line Plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Bar Plot
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]

# Histogram
data = np.random.randn(1000)

# Scatter Plot
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)

# Create a figure with 2x2 subplots.
fig, axs = plt.subplots(2, 2)

# Line plot (Top Left)
axs[0,0].plot(x, y, marker='o', color='b')
axs[0,0].set_title('Line Plot')
axs[0,0].set_xlabel('X-axis')
axs[0,0].set_ylabel('Y-axis')
axs[0,0].grid(True)

# Bar Plot (Top Right)
axs[0,1].bar(categories, values, color='yellow', edgecolor='black', alpha=0.7)
axs[0,1].set_title('Bar Plot')
axs[0,1].set_xlabel('Categories')
axs[0,1].set_ylabel('Values')

# Histogram (Bottom Left)
axs[1,0].hist(data, bins=20, color='green', edgecolor='black', alpha=0.7)
axs[1,0].set_title('Histogram')
axs[1,0].set_xlabel('Value')
axs[1,0].set_ylabel('Frequency')

# Scatter Plot (Bottom Right)
axs[1,1].scatter(x_scatter, y_scatter, color='purple', alpha=0.7)
axs[1,1].set_title('Scatter Plot')
axs[1,1].set_xlabel('X-axis')
axs[1,1].set_ylabel('Y-axis')
axs[1,1].grid(True)

# Adjust layout
plt.tight_layout()
plt.show()

# Exercise 7
import matplotlib.pyplot as plt

categories = ['Marketing', 'Development', 'Sales', 'Support']
values = [20, 35, 25, 20]

plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart')
plt.legend(categories, title="Departments", loc='lower left')
plt.tight_layout()
plt.show()

# Exercise 8
import matplotlib.pyplot as plt
import numpy as np

categories = ['Group 1', 'Group 2', 'Group 3']
value1 = [5, 7, 3]
value2 = [6, 8, 4]
value3 = [4, 3, 5]

plt.bar(categories, value1, label='Value Set 1', color='b')
plt.bar(categories, value2, bottom=value1, label='Value Set 2', color='g')
plt.bar(categories, value3, bottom=np.array(value1) + np.array(value2), label='Value Set 3', color='r')

# Adding labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Stacked Bar Plot')

# Add a legend
plt.legend(title='Value Sets')

# Show the plot
plt.tight_layout()
plt.show()

# Exercise 9
import matplotlib.pyplot as plt
import numpy as np

dataset1 = np.random.normal(60, 10, 100) # 100 data points around mean 60
dataset2 = np.random.normal(70, 15, 100) # 100 data points around mean 70
dataset3 = np.random.normal(80, 5, 100) # 100 data points around mean 80

plt.boxplot([dataset1, dataset2, dataset3], labels=['Dataset 1', 'Dataset 2', 'Dataset 3'])

# Adding labels and title
plt.xlabel('Datasets')
plt.ylabel('Values')
plt.title('Box Plot of Datasets')

# Show the plot
plt.tight_layout()
plt.show()

# Exercise 10
import matplotlib.pyplot as plt

x = range(0, 20)
y = [value ** 2 for value in x]

plt.plot(x, y, marker='o')

# Adding labels and title
plt.xlabel('x values')
plt.ylabel('y values (squared)')
plt.title('y = x^2')

# Annotate the highest and lowest points
max_point = (x[-1], y[-1])  # Highest point (last point in this case)
min_point = (x[0], y[0])    # Lowest point (first point)

# Add annotations
plt.annotate(f'Highest: {max_point}', xy=max_point, xytext=(max_point[0]-7, max_point[1]-30),
             arrowprops=dict(facecolor='green', shrink=0.2), fontsize=8)
plt.annotate(f'Lowest: {min_point}', xy=min_point, xytext=(min_point[0]+3, min_point[1]+50),
             arrowprops=dict(facecolor='red', shrink=0.2), fontsize=8)

# Show the plot
plt.tight_layout()
plt.show()

