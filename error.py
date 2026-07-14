# for i in range(0,4):
#     try:
#         a = int(input("Enter Ist number: "))
#         b = int(input("Enter IInd number: "))

#         c = a/b
#         print(c)
#     except Exception as e:
#         print("Some Error occured")
#         print("Error is ", e)

# try: 
#     a =int(input("Enter Ist number "))
#     b = int(input("Enter IInd number"))
#     c = a/b
#     print(c)

# except ZeroDivisionError:
#     print("Zero error")
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")

# Alternative using a tuple:
try:
  num = int(input("Enter a number: "))
  result = 10 / num
except (ZeroDivisionError, ValueError) as e:
  print(f"An error occurred: {e}")