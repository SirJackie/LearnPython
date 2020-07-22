a = int(input("Please enter your age:"))

if a <= 6:
    print("Kid")
elif 6 <= a < 10:
    print("Pupil")
elif 10 <= a < 18:
    print("Teenager")
elif a >= 18:
    print("Adult")
else:
    print("Error!")


