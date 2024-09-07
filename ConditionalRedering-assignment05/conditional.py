# Question 1:
# Using conditional statements, check if the number is:
#  - Even or Odd.
print("Q1: (Even or Odd)")

while True:
  try:
    num = int(input("Enter a number: "))
    if(num % 2 == 0):
      print(f"Number {num} is Even")
      break
    else:
      print(f"Your Number {num} is Odd")
      break
  except ValueError:
    print("You put the invalid input, Try again")
    
print("\n_______________\n")

# Question 2:
# Using conditional statements, check if the number is:
#  - Positive, Negative, or Zero.

print("Q2: (Positive, Negative, or Zero Check)")

while True:
  try:
    num = int(input("Enter a number: "))
    if(num > 0):
      print(f"Number {num} is Positive")
      break
    elif(num<0):
      print(f"Number {num} is Negative")
      break
    else:
      print(f"Your Number {num} is equal to Zero")
      break
  except ValueError:
    print("You put the invalid input, Try again")
    
print("\n_______________\n")


# Question 3:
#  - Whether it is divisible by both 2 and 3 or anyone of them or not divisible by both check all the cases and print statement for each case.

print("Q3: (Divisible by 2, 3 or not)")

while True:
  try:
    num = int(input("Enter a number: "))
    if(num % 2 == 0 and num % 3 == 0):
      print(f"Number {num} is Divisible by both 2 & 3")
      break
    elif(num % 2 == 0):
      print(f"Number {num} is Divisible by 2")
      break
    elif(num % 3 == 0):
      print(f"Number {num} is Divisible by 3")
      break
    else:
      print(f"Your Number {num} is neither divisible by 2 nor 3")
      break
  except ValueError:
    print("You put the invalid input, Try again")
    
print("\n_______________\n")


# Question 4:
#  - Take the user age.
#   -- If the age is 18 or above:
#   -- Ask if they have a nationality of "Pakistani".
#     ---If yes, print "You are eligible to vote."
#     ---If no, print "Please obtain a valid ID to vote."

print("Q4: (Eligibility check for vote)")

while True:
  try:
    age = int(input("Enter Your Age: "))
    if(age >= 18):
      Nationality = input("Are you Pakistani or Not? (yes/No)")
      if(Nationality.lower() == "yes"):
        print("You are eligible to vote.")
        break
      else:
        print("Please obtain a valid ID to vote.")
        break
    else:
      print(f"You are under Age, not eligible for vote")
      break
  except ValueError:
    print("You put the invalid input, Try again")
    
print("\n_______________\n")

# Question 5:
#  - Write a program that takes the age of a person as input and determines whether they are a child (0-12 years), teenager (13-19 years), adult (20-59 years), or senior citizen (60 years and above)

print("Q4: (check about citizenship)")

while True:
  try:
    age = int(input("Enter Your Age: "))
    if(age >= 0 and age <= 12):
      print("You are Child.")
      break
    elif(age > 12 and age <= 19 ):
      print("You are Teenager.")
      break
    elif(age > 19 and age <= 59 ):
      print("You are Adult.")
      break
    elif(age > 59 ):
      print("You are Senior Citizen.")
      break
    else:
      print(f"You input the invalid Age")
  except ValueError:
    print("You put the invalid input, Try again")
    
print("\n_______________\n")

# Question 6:
#  - Enter a month (as a number between 1 and 12). Print the number of days in that month. Assume a non-leap year.

print("Q6:")

while True:
  try:
    month = int(input("Enter a month (1-12): "))
    if 1 <= month <= 12:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            days_in_month = 31
        elif month == 2:
            days_in_month = 28
        else:
            days_in_month = 30
        print(f"The month {month} has {days_in_month} days.")
        break
    else:
        print("Invalid month. Please enter a number between 1 and 12.")
  except ValueError:
    print("Invalid input. Please enter a valid number.")
    
    
print("\n_______________\n")

# Question 6:
#  - Check if a year is a leap year or not.
print("Q6:")
while True:
  try:
    year = int(input("Enter a year: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
        else:
            print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
    break
  except ValueError:
    print("Invalid input. Please enter a valid number.")


