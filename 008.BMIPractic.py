weight = float(input("Please input your weight(kg):"))
height = float(input("Please input your height(m):"))

BMI = weight / (height ** 2)

print("BMI : %.2f" % BMI)

if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal Weight")
elif 25 <= BMI < 30:
    print("Overweight")
elif 30 <= BMI < 35:
    print("Obesity (Class 1)")
elif 35 <= BMI < 40:
    print("Obesity (Class 2)")
elif BMI >= 40:
    print("Morbid Obesity")
