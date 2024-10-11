
# 1. get user input/ data types (str -> float)
Weight = float(input("Enter weight in kilograms: "))
Height = float(input("Enter your height in meters: "))

# 2. calculate the bmi
BMI = Weight / (Height * Height)
BMI_categories: str = ""
# BMI_categories = ""


# 3. get the bmi category
if BMI < 18.5:
   BMI_categories = "Underweight"
#    print("Your BMI is " + str(BMI) + ". You are classified as Underweight")
elif 18.5 <= BMI < 24.9:
    BMI_categories = "Normal weight"
#    print("Your BMI is " + str(BMI) + ". You are classified as Normal weight")
elif 25 <= BMI < 29.9:
    BMI_categories = "Overweight"
#    print("Your BMI is " + str(BMI) + ". You are classified as Overweight")
elif BMI > 30:
    BMI_categories = "Obesity"
#    print("Your BMI is " + str(BMI) + ". You are classified as Obesity")

# 4. print the final message
print(f"Your BMI is {BMI}. You are classified as {BMI_categories}.")
#    print("Your BMI is " + str(BMI) + ". You are classified as Obesity")


# BMI = input("Your BMI is: ")
# BMI = float(BMI)



