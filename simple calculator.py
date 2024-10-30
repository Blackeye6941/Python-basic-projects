while(True):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    op = int(input("Enter the operation to be done:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n"));
    if(op == 1):
        result = a+b
        print(f"The result: {result}")
    elif(op == 2):
        result = a-b
        print(f"The result: {result}")
    elif(op == 3):
        result = a*b
        print(f"The result: {result}")
    elif(op == 4):
        if(b == 0):
            print("Division by zero not possible");
        else:
            result = a/b
            print(f"The result: {result}")
    else:
        print("Invalid Operation!!")

