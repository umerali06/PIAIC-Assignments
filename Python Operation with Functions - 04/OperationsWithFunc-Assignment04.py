# Question no#01:
#Calculate your age based on the current year and your birth year?


# Solution:
print("Question no#1\n")
from datetime import datetime
def CalculateAge():
  while True:
    try:
      birth_year = int(input("Enter your birth year: "))
      # current_year = int(input("Enter the current year: "))
      current_year = datetime.now().year
      if birth_year > current_year:
        print("Invalid year. Please enter a year that is less than or equal to the current year.")
        break
      else:
        age = current_year - birth_year
        return age
    except ValueError:
      print("Invalid input. Please enter a valid year.")
      
age = CalculateAge()

print(f"Your age is {age} years.")



print("\n||-----------------Question End------------------||\n")


# Question no#2:

# Write a program that calculates the area of a rectangle using length and width variables?

# Solution:

print("Question no#2\n")
def CalculateTriangleArea():
  while True:
    try:
      length = float(input("Enter the Length: "))
      width = float(input("Enter the width: "))
      area = length * width
      return area
    except ValueError:
      print("You put the invalid Input.Try Again")

area =CalculateTriangleArea()
print(f"The Area of Rectangle is {area}")


print("\n||-----------------Question End------------------||\n")


# Question no#3:

# Write a program that calculates the area of a circle.

# Solution:

print("Question no#3\n")
def CalculateCircleArea():
  from math import pi
  while True:
    try:
      radius = float(input("Enter the radius: "))
      area = pi*(radius**2)
      return area
    except ValueError:
      print("You put the invalid Input.Try Again")

area =CalculateCircleArea()
print(f"The Area of circle is {area:.2f}")

print("\n||-----------------Question End------------------||\n")


# Question no#4:

# Write a program that calculates the area of the cube.

# Solution:
print("Question no#4\n")
def CalculateCubeArea():
  while True:
    try:
      Side = float(input("Enter the Side Length: "))
      area = 6*(Side**2)
      return area
    except ValueError:
      print("You put the invalid Input.Try Again")


area =CalculateCubeArea()
print(f"The Area of cube is {area:.2f}")
      

print("\n||-----------------Question End------------------||\n")


# Question no#5:

# Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.

# Solution:

print("Question no#5\n")
def TempConvertor():
  while True:
    try:
      temperature = float(input("Enter the Temperature: "))
      print(temperature)

      unit = input("Enter the unit Value (C/F):")
      # Fahrenheit to Celsius conversion:
      if unit.upper() == "C":
        celsius = (temperature - 32) * 5/9
        print(f"{temperature}°F is equal to {celsius:.2f}°C")
        break

      # Celsius to Fahrenheit conversion:
      elif unit.upper() == "F":
          fahrenheit = (temperature * 9/5) + 32
          print(f"{temperature}°C is equal to {fahrenheit:.2f}°F")
          break

      else:
        print("Invalid unit value. Please enter either 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
      print("You put the invalid Input.Try Again")


TempConvertor()

      
      
      
print("\n||-----------------Question End------------------||\n")



# Question no#6:

# Convert a given number of seconds into minutes and seconds using variables.

# Solution:

print("Question no#6\n")
def TimeConvertor():
  while True:
    try:
      seconds = int(input("Enter the number of seconds: "))

      minutes = seconds // 60

      seconds = seconds % 60
      
      print(f"{seconds} seconds is equal to {minutes} minutes and {seconds} seconds.")
      break
    except ValueError:
      print("You put the invalid Input.Try Again")


TimeConvertor()

      

print("\n||-----------------Question End------------------||\n")


# Question no#7:

# Write a program that calculates the percentage.?

# Solution:

print("Question no#7\n")
def PercentageCalculator():
  while True:
    try:
      obtained_marks = int(input("Enter Your Obtained Marks: "))
      # print(obtained_marks)
      total_marks = int(input("Enter the Total Marks: "))
      # print(total_marks)
      percentage = (obtained_marks/total_marks)*100
      return percentage
      


    except ValueError:
      print("You put the invalid Input.Try Again")


percentage =PercentageCalculator()
print(f"Your Percentage Marks : {percentage:.2f}%")
      

print("\n||-----------------Question End------------------||\n")


# Question no#8:

# Write a program that calculates the BMI using height (in meters) and weight (in kilograms) variables.

# Solution:

print("Question no#8\n")
def BmiCalculate():
  while True:
    try:
      # Define the height and weight variables
      height = float(input("Enter your height in meters: "))
      weight = float(input("Enter your weight in kilograms: "))

      # Calculate the BMI
      bmi = weight / (height ** 2)
      return bmi
    except ValueError:
      print("You put the invalid Input.Try Again")

bmi = BmiCalculate()
print(f"Your BMI is {bmi:.2f}")

      

print("\n||-----------------Question End------------------||\n")


# Question no#9:

# Write a program that calculates the volume of a cylinder using the formula .

# Solution:

print("Question no#9\n")

import math

def VolumeCalculate():
  while True:
    try:
      radius = float(input("Enter the radius of the cylinder: "))
      height = float(input("Enter the height of the cylinder: "))
      volume = math.pi * (radius ** 2) * height
      return volume
    except ValueError:
      print("You put the invalid Input.Try Again")


volumeCalc =VolumeCalculate()
print(f"The volume of cylinder is {volumeCalc:.2f}")
      

print("\n||-----------------Question End------------------||\n")







