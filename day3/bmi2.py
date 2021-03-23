height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))

m_height = height * .0254
kg_weight = weight * .45359237
bmi = kg_weight/m_height**2
bmi_rounded = round(bmi)

taxonomy = ""
if (bmi >= 35):
    taxonomy = "clinically obese"
elif (bmi >= 30):
    taxonomy = "obese"
elif (bmi >= 25):
    taxonomy = "overweight"
elif (bmi >= 18.5):
    taxonomy = "a normal weight"
else:
    taxonomy = "underweight"

print(f"Your BMI is {bmi_rounded}.  You are {taxonomy}.")

desired = float(input("\nEnter your desired BMI: "))

goal_weight = desired * m_height**2
lb_goal_weight = round(goal_weight/.45359237)

print(
    f"To reach your desired BMI, you would need to weigh {lb_goal_weight} pounds.")
