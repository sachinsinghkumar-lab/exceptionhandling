while True:
try:
num = int(input("Enter number:"))
if num < 0:
print("Bye")
break
result : 50/0
print("Result : ", result)
except ZeroDivisionError:
print("Division by zero error")
except ValueError:
print("Enter valid number")
finally:
print("Program ends.....")
