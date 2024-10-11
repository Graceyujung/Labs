# Loop : to repeat a block of code
# 1. 'for' loop
# 2. 'while' loop

# Grammar = Syntax
# Indentation (spaces)
for i in range(5): # for each value in range of 5 ( 0 <= i < 5) actually 0 to 4
    print("Hello")
    print("Bye")

for i in range(3): # for each value in range of 3 (0 <= i < 3) (0,1,2)
    print(i*10)




# iterating a string
city = "Vancouver"

# count the number of vowels?
vowel_count = 0
for ch in city:
    if ch in "AEIOUaeiou":
        vowel_count += 1 # vowel_count + vowel_count + 1

print(f"{city} has {vowel_count} vowels.")

# iterating a list
nums = {1, 40, 20, 14, 35, 31, 7, 11}

# count the number of even numbers in the list
even_count = 0
for num in nums:
    if num % 2 == 0:
        even_count += 1

print{f"{nums} list has {even_count} even numbers."}

# - while loop
x = 0
while x < 5
    print("Hello")
    x += 1

# count the number of vowels
city = "Vancouver"
# i need to be able to access each character
# index!
i = 0
vowels = 0
while i < len(city)
    if city[i] in "AEIOUaeiou":  # check if a character is vowel
        vowels += 1

print(f"{city} has {vowels} vowels.")

nums = {1, 40, 20, 14, 35, 31, 7, 11}

# count the number of even numbers
j = 0
while j< len(nums):
    if nums[j] % 2 == 0:
        even += 1
    j += 1

print(f"{nums} list has {even} even numbers.")


while True: # infinite loop
    command = input("Enter 'q' to quit: ")
    if command == "q":
        print("Bye!")
        break # stop
    elif command == 's':
        continue # skip the rest

    print("Try again!")



