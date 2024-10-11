# 1. write a loop to print each character in the string "Python"
for char in "Python":
    print(char)

# 2. Write a loop to count the number of vowels in the string "data science".
# iterating a string
word = "data science"

#count the numbers of vowels
vowel_count = 0
for ch in word:
    if ch in "AEIOUaeiou":
        vowel_count += 1

print(f"{word} has {vowel_count} vowels.")

# 3. Write a loop to reverse the string "hello world" and print the reversed string.
string = "hello world"

reversed_string = ""

for char in string:
    reversed_string = char + reversed_string

print(reversed_string)

# 4
string = "coding"

for char in string:
    print(f"The ASCII value of '{char} is {ord(char)}")

# 5.
string = "experience"
e_count = 0
for ch in string:
    if ch in "e":
        e_count += 1

print(f"{string} has {e_count} times of the character e")

# 6.
string = "education"
vowels = "aeiouAEIOU"
modified_string = ""

for char in string:
    if char in vowels:
        modified_string += '*'
    else:
        modified_string += char

print(modified_string)

# 7.
string = "looping"

for i in range(1, len(string), 2):
    print(string[i])

# 8.
string = "swiss"\

seen = set()

for char in string:
    if char in seen:
        print(f"The first repeating character is: {char}")
        break
    else:
        seen.add(char)
else:
    print("No repeating characters found.")

# 9.
sentence = "machine learning is fun"
words = sentence.split()
capitalized_words = []

for word in words:
    capitalized_words.append(word.capitalize())

capitalized_sentence = ' '.join(capitalized_words)

print(capitalized_sentence)

# 10.

# 1. Palindrome Check
word = input("Enter palindrome: ")
print(word[::-1])
if word == word[::-1]:
    print("It is a palindrome")
else:
    print("It's not a palindrome")










