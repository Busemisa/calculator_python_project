
#calculator made as an example
def Plus(a, b):
    return a + b

def Multiplication(a, b):
    return a * b

def Extraction(a, b):
    return a - b

def Divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed."

def Modding(a, b):
    if b != 0:
        return a % b
    else:
        return "Division by zero is not allowed."

print("1) Plus\n2) Multiplication\n3) Extraction\n4) Divide\n5) Modding\n")

#The operations and numbers to be performed were received from the user
sayi = int(input("Please enter a number: "))
sayi1 = float(input("please enter a number: "))
sayi2 = float(input("please enter a number "))

if sayi == 1:
    print("Result: ", Plus(sayi1, sayi2))
elif sayi == 2:
    print("Result: ", Multiplication(sayi1, sayi2))
elif sayi == 3:
    print("Result: ", Extraction(sayi1, sayi2))
elif sayi == 4:
    print("Result: ", Divide(sayi1, sayi2))
elif sayi == 5:
    print("Result: ", Modding(sayi1, sayi2))
else:
    print("Please enter a valid number")



