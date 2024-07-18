import time

#Function for addition
def addition(x, y):
    print(f"\n{x} + {y} = {x + y}\n")

#Function for subtraction
def subtraction(x, y):
    print(f"\n{x} - {y} = {x - y}\n")

#Function for multiplication
def multiplication(x, y):
    print(f"\n{x} × {y} = {x * y}\n")

#Function for division
def division(x, y):
    print(f"\n{x} ÷ {y} = {x / y}\n")

#Function for even or odd
def even_odd(x):
    if x % 2 == 0:
        print(f"\n{x} is even\n")
    else:
        print(f"\n{x} is odd\n")

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

print("Welcome to Omar's Calculator (V4.0)\n\n")
print("_________________________________________")
while True:
    print("Available Operations")
    print("1 ---> Addition")
    print("2 ---> Subtraction")
    print("3 ---> Multiplication")
    print("4 ---> Division")
    print("5 ---> Even or Odd")
    print("6 ---> Factorial")
    print("7 ---> Exit")
    print("_________________________________________")
    choice = input("Enter your choice: ")
    print("_________________________________________")
    if choice in ('1', '2', '3', '4'):
        try:
          num1 = float(input("Enter first number: "))
          num2 = float(input("Enter second number: "))
          if choice == '1':
              addition(num1, num2)
          if choice == '2':
              subtraction(num1, num2)
          if choice == '3':
              multiplication(num1, num2)
          if choice == '4':
            try:
              division(num1, num2)
            except:
              print("Cannot divide by zero")
        except:
          print("Invalid Input")

    elif choice == '5':
      try:
        Digit = int(input("Enter your number that you want to identify it as even/ odd: \n\n"))
        even_odd(Digit)
      except:
        print("Invalid Input")

    elif choice == '6':
      try:
        num = int(input("Enter the number which you want the factorial of: \n\n"))
        result = factorial(num)
        print("\nThe factorial of", num, "=", result,"\n")
      except:
        print("Invalid Input")

    elif choice == '7':
        print("Thanks for using Omar's Calculator😊")
        print("_____________________________________________________")
        print("Exiting...")
        time.sleep(4)
        break
    else:
        print("Invalid Input")
