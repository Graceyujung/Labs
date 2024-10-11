# conditional statements (if-else statements)
# user input (keyboard input)
# : input(prompt) -> print the prompt, take the user input and return as str
# input always prints string

score =  input("Enter your score: ")
score = int(score)

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# if score >= 90:
#     print("A")
# if score >= 80:
#     print("B")
# if score >= 70:
#     print("C")
# else:
#     print("F")
