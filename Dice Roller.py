
import random
repeat = True
while repeat:
    op = int(input("1.Roll Dice\n2.Exit\nEnter operation: "))
    match(op):
        case 1:
            num = int(input("Enter the Number of Dices: "))
            def Roll_Dice(num):
                result = []
                for _ in range(num):
                    result.append(random.randint(1, 6))
                return result
            rolls = Roll_Dice(num)
            for x in rolls:
                print(x)

        case 2:
            print("Program exited")
            repeat = False

            
        
