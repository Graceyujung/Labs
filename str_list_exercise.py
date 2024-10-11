# List Exercises

# 1. List Creation and Access
l = [1,2,3,4,5]
print("Third element: ", l[2])

# 2. List Manipulation
l. append(6)
print(l)
l. pop(1)
print(l)

# 3. List Slicing
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numbers[:5])
print(numbers[7:])

print(numbers[::2]) #[0:len(numbers):2]

# 4. List Operations
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(my_list))

max_value = max(my_list)
min_value = min(my_list)
print("Maximum value:", max_value)
print("Minimum value:", min_value)

# 5. List Comprehension
squares = [i**2 for i in range(1, 11)] #i*i
print(squares)

# 6. Nested Lists
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list)
print(list[1][1])

# String Exercises

# 1. String Creation and Access
string = "Hello, World!"
print("First Character: ", string[0])
print("Last Character: ", string[-1])

# 2. String Slicing
string2 = "Python Programming"
print(string2[:6])
print(string2[7:])

# 3. String Method
string3 = "hello, world!"
print(string3.upper())

string4 = "Hello, World!"
updated_string = string4.replace("World", "Python")
print("Updated String: ", updated_string)

# 4. String Concatenation
string5 = ["Hello", "World"]
print(" ".join(string5))
# print("Hello" + " " + "World")

# 5. String Splitting
fruits = "apple,banana,cherry"
split_fruits = fruits.split(",")
print(split_fruits)

# 6. String Formatting
name = "Grace"
age = 26

result = f"My name is {name} and I am {age} years old"
print(result)

# 7. String Reversal
username = input("Enter your name: ")
print(username[::-1]) # reverse a string/list

# Bonus Exercises
# 1. Palindrome Check
word = input("Enter palindrome: ")
print(word[::-1])
if word == word[::-1]:
    print("It is a palindrome")
else:
    print("It's not a palindrome")

# 2. List to String Conversion
chars = ['P', 'y', 't', 'h', 'o', 'n']
print("".join(chars))

