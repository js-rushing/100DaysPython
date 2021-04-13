height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))

m_height = height * .0254
kg_weight = weight * .45359237
bmi = round(kg_weight/m_height**2)

print(f"Your BMI is {bmi}")

desired = float(input("\nEnter your desired BMI: "))

goal_weight = desired * m_height**2
lb_goal_weight = round(goal_weight/.45359237)

print(
    f"To reach your desired BMI, you would need to weigh {lb_goal_weight} pounds.")
