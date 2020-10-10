# Calculating BMI 
# When weight and height are provided
#
weight=float(input("enter your weight (kg): "))
height=float(input("enter your height (cm): "))/100
bmi=weight/(height**2)
print(bmi)
if bmi<=18.8:
    print("you are thin! Eat more:)")
elif bmi>=18.5 and bmi<=24.9:
    print("you are normal:)")
elif bmi>=25 and bmi<=29.9:
    print("You should diet!")
else:
    print("You are obese! Be carreful!")
