# function for addition
def add(x, y):
  return x + y

# function for subtraction
def subtract(x, y):
  return x - y

# function for division
def divide(x, y):
  return x / y

# function for multiplication
def multiply(x, y):
  return x * y

def main():
  print("Select operation")
  print("1. Add")
  print("2. Subtract")
  print("3. Divide")
  print("4. Multiply")
  print("0. Exit")
  while True:
    # take input from user
    choice = int(input("Enter choice (1,2,3,4, 0): "))

    # check if choice is one of the given options
    if choice == 0:
      print("Good Bye")
      break
    elif choice in ('1', '2', '3', '4'):
      try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
      except ValueError:
        print("Invalid input. Please enter a number.")
        continue

      if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
      elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
      elif choice == '3':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
      elif choice == '4':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")


      next_calculation = input("Do another calculation? (y/n): ")
      if next_calculation == "n":
        print("Shutting down. Have a good one, mate!")
        break
      elif next_calculation != "y, n":
        print("Invalid input. Maybe try again?")
        next_calculation = input("Do another calculation? (y/n): ")
      else:
        continue
    else:
      print("Invalid input. Please try again")
