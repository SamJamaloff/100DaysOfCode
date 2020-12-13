# bmi update file for specifying user weight status using bmi index

height_square = float(input("Please enter your height in m: "))**2
weight = float(input("Please enter you weight in kg: "))
bmi = weight/height_square
if bmi < 18.5:
    print(f"underweight {bmi}")
elif bmi <= 25:
    print(f"normal weight {bmi}")
elif bmi <= 30:
    print(f"overweight {bmi}")
elif bmi <= 35:
    print(f"Obese {bmi}")
else:
    print(f"clinically obese {bmi}")