a = float(input("Enter the temperature to convert: "))
op = int(input("Enter conversion criteria:\n1.Fahrenheit to Celcius\n2.celcius to Kelvin\n3.Kelvin to celcius\n4.Celcius to Fahreheit\n"))
if(op == 1):
    result = (a-32) * 5/9;
    print(f"Result: {result:.2f}C")
elif(op == 2):
    result = a+273.15
    print(f"Result: {result:.2f}K")
elif(op == 3):
    result = a-273.15
    print(f"Result: {result:.2f}C")
elif(op == 4):
    result = (a*9/5) +32
    print(f"Result: {result:.2f}F")
else:
    print("Invalid Operation")