#BMI Calculator
#BMI = weight in kilograms divided by the square of height in meters.

print("Let's calculate your Body Mass Index (BMI)\n")
weight = input("What is your weight in kilograms?\n")
height = input("What is your height in cm?\n")

height_in_meters = float(height)/100

bmi = float(weight) / (height_in_meters ** 2)

print("Here is the calculated result:\n")
print(f"Weight: {weight} kg")
print(f"Height: {height_in_meters} m")
print(f"BMI: {bmi}")

common_text = "\nBased on your BMI, you fall into the category of"

if bmi < 18.5:
    print(common_text, "underweight")
elif bmi >= 18.5 and bmi < 25:
    print(common_text, "normal weight")
else:
    print(common_text, "overweight")
