#BMI Calculator
#BMI = weight in kilograms divided by the square of height in meters.

print("Let's calculate your Body Mass Index (BMI)\n")

def cast_to_float(text):
    while True:
        user_input = input(text)
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please provide a correct numeric value.")
            continue

weight = cast_to_float("What is your weight in kilograms?\n")
height = cast_to_float("What is your height in cm?\n")

height_in_meters = float(height)/100

bmi = float(weight) / (height_in_meters ** 2)

print("Here is the calculated result:\n")
print(f"Weight: {round(weight, 2)} kg")
print(f"Height: {round(height_in_meters, 2)} m")
print(f"BMI: {round(bmi, 2)}")

common_text = "\nBased on your BMI, you fall into the category of"

if bmi < 18.5:
    print(common_text, "Underweight")
elif 18.5 <= bmi < 25:
    print(common_text, "Normal weight")
elif 25 <= bmi < 30:
    print(common_text, "Overweight")
elif 30 <= bmi < 35:
    print(common_text, "Obesity Class I")
elif 35 <= bmi < 40:
    print(common_text, "Obesity Class II")
else:
    print(common_text, "Obesity Class III")