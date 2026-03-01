try:
    number = int(input("enter a number:"))
    print("the numer is enteres is:", number)
except ValueError as e:
    print("Exception", e)