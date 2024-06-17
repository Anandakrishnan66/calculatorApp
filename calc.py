print("\nadd\nsub\ndiv\nmul")
val=input("Enter the choice: ")


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b

while (True):
    match val:
        case "add":
            a=int(input("Enter the first number"))
            b=int(input("Enter the second number"))
            print(add(a,b))
            val = input("Enter the choice: ")
        case "sub":
            a = int(input("Enter the first number"))
            b = int(input("Enter the second number"))
            print(sub(a,b))
            val = input("Enter the choice: ")
        case "div":
            a = int(input("Enter the first number"))
            b = int(input("Enter the second number"))
            print(div(a,b))
            val = input("Enter the choice: ")

        case "mul":
            a = int(input("Enter the first number"))
            b = int(input("Enter the second number"))
            print(mul(a,b))
            val = input("Enter the choice: ")
        case "stop":
            print("Exiting....")

            break




