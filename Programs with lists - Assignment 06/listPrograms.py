# 1. *Create a function* that takes an array, an index, and a value as parameters. Inside the function, use the insert method to insert the value at the specified index in the array. Return the modified array.

print("Q:1")
def insert_value(arr, index, value):
  arr.insert(index, value)
  return arr

while True:
  try:
    arr = input("Enter the Array (space-separated values): ").split()
    arr = [int(x) for x in arr]
    index = int(input("Enter the Index: "))
    value = int(input("Enter the Value: "))
    result = insert_value(arr,index, value)
    print("Modified Array:", result)
    break
  except ValueError as e:
    print("Invalid input. Please enter a valid array.")
    print("Error: ", e)
    continue
  
print("_____________________")



# 2. *Implement a simple shopping cart program* using an array. Create functions to add items, remove items, and update quantities using array methods. Print the cart's contents after each operation.

print("\nQ:2")

def shopping_cart():
  cart = []
  while True:
    print("\nShopping Cart:")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Update Quantity")
    print("4. View Cart")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    try:
      if choice == 1:
        item = input("Enter the Item: ")
        quantity = int(input("Enter the Quantity: "))
        cart.append((item, quantity))
        print("Item added to cart!")
      elif choice == 2:
        item = input("Enter the Item to Remove: ")
        for i in range(len(cart)):
          if cart[i][0] == item:
            cart.pop(i)
            print("Item removed from cart!")
            break
        else:
          print("Item not found in cart!")
      elif choice == 3:
        item = input("Enter the Item to Update: ")
        for i in range(len(cart)):
          if cart[i][0] == item:
            quantity = int(input("Enter the New Quantity: "))
            cart[i] = (item, quantity)
            print("Item quantity updated!")
            break
        else:
          print("Item not found in cart!")
      elif choice == 4:
        print("\nShopping Cart:")
        for item, quantity in cart:
          print(f"{item}: {quantity}")
      elif choice == 5:
        print("Exiting shopping cart...")
        break
      else:
        print("Invalid choice. Please try again!")
    except ValueError as e:
      print("Invalid input. Please enter a valid value.")
      print("Error: ", e)
      continue

shopping_cart()


print("_____________________")     


# 3. *Write a program* that uses a while loop to print the first 25 integers.

print("\nQ:3\n")

def Print_DigLoop():
  i = 1
  while i <= 25:
    print(i)
    i += 1
    
Print_DigLoop()

print("_____________________")

# 4. *Write a program* that uses a while loop to print the first 10 even numbers.

print("\nQ:4")

def Print_EvenLoop():
  i = 2
  while i <= 20:
    print(i)
    i += 2
    
Print_EvenLoop()

print("___________________")

# 5. *Create a function* that takes a positive integer as a parameter and uses a while loop to calculate and return the factorial of that number.

print("\nQ:5")

def factorial(n):
  try:
    if n < 0:
      raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    i = 1
    while i <= n:
      result *= i
      i += 1
    return result
  except ValueError as e:
    print("Error: ", e)
    return None

while True:
  try:
    n = int(input("Enter a positive integer: "))
    result = factorial(n)
    if result is not None:
      print("Factorial:", result)
      break
  except ValueError as e:
    print("Invalid input. Please enter a positive integer.")
    print("Error: ", e)
    continue
  

print("_____________________")

# 6. *Write a program* that has an array of numbers; if the number is negative, it should remove the negative number from the array.

print("\nQ:6")

def remove_negative():
  try:
    return [x for x in arr if x >= 0]
  except TypeError as e:
    print("Error: ", e)
    return None
  
while True:
  try:
    arr = input("Enter the Array (space-separated values): ").split()
    arr = [int(x) for x in arr]
    result = remove_negative()
    if result is not None:
      print("Modified Array:", result)
      break
  except ValueError as e:
    print("Invalid input. Please enter a valid array.")
    print("Error: ", e)
    continue
  

print("____________________")

# 7. *Create a function* that takes an array of numbers as a parameter. Use a while loop to calculate and return the sum of all the numbers in the array.


print("\nQ:7")

def sum_array(arr):
  try:
    sum = 0
    i = 0
    while i < len(arr):
      sum += arr[i]
      i += 1
    return sum
  except TypeError as e:
    print("Error: ", e)
    return None

while True:
  try:
    arr = input("Enter the Array (space-separated values): ").split()
    arr = [int(x) for x in arr]
    result = sum_array(arr)
    if result is not None:
      print("Sum of array:", result)
      break
  except ValueError as e:
    print("Invalid input. Please enter a valid array.")
    print("Error: ", e)
    continue
  
print("_________________")


# 8. *Implement a program* that takes a list of temperatures in Celsius as input from the user. Convert each temperature to Fahrenheit using the formula F = (C * 9/5) + 32 and store the converted temperatures in an array. Use a while loop to perform the conversion for each temperature.

print("\nQ:8")

def celsius_to_fahrenheit(celsius):
  try:
    return (celsius * 9/5) + 32
  except TypeError as e:
    print("Error: ", e)
    return None

while True:
  try:
    temps = input("Enter the temperatures in Celsius (space-separated values): ").split()
    temps = [float(x) for x in temps]
    fahrenheit_temps = []
    i = 0
    while i < len(temps):
      fahrenheit_temps.append(celsius_to_fahrenheit(temps[i]))
      i += 1
    print("Temperatures in Fahrenheit:", fahrenheit_temps)
    break
  except ValueError as e:
    print("Invalid input.")
    print("Error: ",e)
    
    
  print("________________________")

# 9. Write a program to remove all the odd numbers from an array.

print("\nQ:9")

def remove_odd_numbers(arr):
  try:
    return [x for x in arr if x % 2 == 0]
  except TypeError as e:
    print("Error: ", e)
    return None

while True:
  try:
    arr = input("Enter the Array (space-separated values): ").split()
    arr = [int(x) for x in arr]
    result = remove_odd_numbers(arr)
    if result is not None:
      print("Array without odd numbers:", result)
      break
  except ValueError as e:
    print("Invalid input. Please enter a valid array.")
    print("Error: ", e)
    continue