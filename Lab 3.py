from random import random

import numpy as np

# Task 1
# List of numbers from 1 to 30
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19,
           20, 21, 22, 23, 24, 25, 26, 27,
           28, 29, 30]

# Convert the list to a Numpy array
np_numbers = np.array(numbers)

# Print the array and its shape
print(np_numbers)
print(np_numbers.shape)

# Access and print the element at index 10
print(np_numbers[10])
print()

# Task 2
numbers_2d = ([1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25],
           [26, 27, 28, 29, 30])

np_numbers_2d = np.array(numbers_2d)

print(np_numbers_2d)
print(np_numbers_2d.shape)
print(np_numbers_2d[3, 4])
print()

# Task 3
third_row = np_numbers_2d[2, :]
print(third_row)
print()

first_two_rows_and_last_three_columns = np_numbers_2d[:2, -3:]
print(first_two_rows_and_last_three_columns)
print()

# Task 4
# Generate a 1D array of 15 random integers between 10 and 100

random_integers = np.random.randint(10, 100, size=15)

# Print the array
print(random_integers)

print()
# Find and print the maximum and minimum values
max_value = np.max(random_integers)
min_value = np.min(random_integers)

print("Maximum value is", max_value)
print("Minimum value is", min_value)
print()

# Task 5
# Generate a 2D array of (4,4) between 0 and 50
random_integers_2d = np.random.randint(0, 50, size=(4,4))

# Print the array and find the sum
print(random_integers_2d)

print()

total_sum = np.sum(random_integers_2d)
print("Sum is", total_sum)
print()

# Task 6
# 2D array of random integers (5,5) between 1 and 20
random_int_2d = np.random.randint(1, 20, size=(5,5))
print(random_int_2d)

print()

random_int_2d[1, :] = 0
print(random_int_2d)

print()
# Replace all values greater than 10 with the value 99
random_int_2d[random_int_2d > 10] = 99
print(random_int_2d)
print()

# Task 7
# Create two 1D arrays of length 5 with random integers between 1 and 10
random_first_array = np.random.randint(1, 10, size=5)
random_second_array = np.random.randint(1, 10, size=5)

print(random_first_array)
print(random_second_array)


# addition, subtraction, multiplication on two arrays
print("Addition: ", random_first_array + random_second_array)
print("Subtraction: ", random_first_array - random_second_array)
print("Multiplication: ", random_first_array * random_second_array)
print()

# Task 8
values_task8 = np.array([2, 4, 6, 8])
print(values_task8)

# 2D array of shape (3,4) between 1 and 5
random_task8 = np.random.randint(1, 5, size=(3,4))
print(random_task8)

print()
# Add 1D array to each row of 2D array using broadcasting
result = values_task8 + random_task8
print(result)
print()

# Task 9
random_task9 = np.random.randint(1, 100, size=20)
print(random_task9)

print("Greater than 50: ", random_task9[random_task9 > 50])
print()

random_task9[random_task9 < 30] = -1
print("Modified array: ", random_task9)
print()

# Task 10
random_task10 = np.random.randint(1, 50, size=12)
print(random_task10)
random_task10_2d = random_task10.reshape((3,4))
print(random_task10_2d)

print()
transposed_array = np.transpose(random_task10_2d)
print(transposed_array)
