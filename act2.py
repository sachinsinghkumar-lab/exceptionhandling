try:
    num1,num2 = eval(input("enter 2 numbers seperated by comma :")
    )
    result = num1/num2
    print("resut is :", result)

except ZeroDivisionError:
    print("division by zero")
except SyntaxError:
    print("comma is missing!!!")
except :
    print("Wrong input...")
else:
    print("no exception")

finally:
    print("this will execute no matter what")

