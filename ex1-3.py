print('Please enter your weight (kg):')
weight = float(input())

print('Please enter your height (m):')
height = float(input())

BMI = weight / (height * height)

print('Your BMI is: ' , BMI )

if BMI <= 18.5 :
    print('You are Underweight')
elif (18.5 < BMI <= 24.9):
    print('You are Normal')
elif (25 < BMI <= 29.9):
    print('You are Overweight')
elif (30 < BMI <= 34.9):
    print('You are Obse')
else:
    print('You are Extremly obese')