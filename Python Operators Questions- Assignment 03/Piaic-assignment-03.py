# Question no#01:
#Calculate your age based on the current year and your birth year?

# Solution:

from datetime import datetime

currentYear = datetime.now().year
# print(currentYear)
birthYear = int(input("Enter your birth year: "))
# print(birthYear)
age = currentYear - birthYear
# print(age)
print(f"Your Age is: {age}")



print("\n||-----------------Question End------------------||\n")



# Question no#2:

# Write a program that calculates the area of a rectangle using length and width variables?

# Solution:

length = float(input("Enter the length of the rectangle: "))
# print(length)
width = float(input("Enter the width of the rectangle: "))
# print(width)
area = length * width
# print(area)
print(f"The area of the rectangle is: {area}")


print("\n||-----------------Question End------------------||\n")


# Question no#3:

# Write a program that calculates the area of a circle.

# Solution:

from math import pi

radius = float(input("Enter the Radius of the Circle: "))
# print(radius)
area = pi*(radius**2)
# print(area)
print(f"The area of the circle is: {area:.2f}")


print("\n||-----------------Question End------------------||\n")


# Question no#4:

# Write a program that calculates the area of the cube.

# Solution:

side = float(input("Enter the Side Length: "))
# print(side)
area = 6 * (side**2)
# print(area)
print(f"The area of the cube is: {area:.2f}")



print("\n||-----------------Question End------------------||\n")



# Question no#5:

# Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.

# Solution:

temperature = float(input("Enter the Temperature: "))
print(temperature)

unit = input("Enter the unit Value (C/F):")
# Fahrenheit to Celsius conversion:
if unit.upper() == "C":
  celsius = (temperature - 32) * 5/9
  print(f"{temperature}°F is equal to {celsius:.2f}°C")

# Celsius to Fahrenheit conversion:
elif unit.upper() == "F":
    fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {fahrenheit:.2f}°F")

else:
  print("Invalid unit value. Please enter either 'C' for Celsius or 'F' for Fahrenheit.")
  
  

print("\n||-----------------Question End------------------||\n")



# Question no#6:

# Convert a given number of seconds into minutes and seconds using variables.

# Solution:

seconds = int(input("Enter the number of seconds: "))

minutes = seconds // 60

seconds = seconds % 60

print(f"{seconds} seconds is equal to {minutes} minutes and {seconds} seconds.")



print("\n||-----------------Question End------------------||\n")




# Question no#7:

# Write a program that calculates the percentage.?

# Solution:

obtained_marks = int(input("Enter Your Obtained Marks: "))
# print(obtained_marks)
total_marks = int(input("Enter the Total Marks: "))
# print(total_marks)
percentage = (obtained_marks/total_marks)*100
# print(percentage)
print(f"Your Percentage Marks : {percentage}%")



print("\n||-----------------Question End------------------||\n")



# Question no#8:

# Write a program that calculates the BMI using height (in meters) and weight (in kilograms) variables.

# Solution:

# Define the height and weight variables
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate the BMI
bmi = weight / (height ** 2)

# Print the BMI
print("Your BMI is:", bmi)

# Determine the BMI category
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You are normal weight.")
elif bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")
    
    
    
    

print("\n||-----------------Question End------------------||\n")




# Question no#9:

# Write a program that calculates the volume of a cylinder using the formula .

# Solution:

import math

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
volume = math.pi * (radius ** 2) * height



print("\n||-----------------Question End------------------||\n")

