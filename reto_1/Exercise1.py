from .exeptions_functions import OutRangeError
        
#This function operate two numbers according to a chosen option
def calculator(a, b, op):
    try:
        if(op == 1):
            return a+b
        elif(op == 2):
            return a-b
        elif(op == 3):
            return a*b
        return a/b
    except ZeroDivisionError:
        return "Invalid opperation (a/0)"

#Options of menu
op_1:str = "1.addition"
op_2:str = "2.subtraction"
op_3:str = "3.multiplication"
op_4:str = "4.division"

#This function validates that the chosen option is within the range 
def validation_options():
    while True:
        print(f"{op_1}\n{op_2}\n{op_3}\n{op_4}")
        try:
            op:int = int(input("Enter your option: "))
            OutRangeError.check_out_range(1, op, 4)
            break
        except ValueError:
            print("Invalidated value")
        except OutRangeError as e:
            print(e)
    return op

#Program
def run():
    option:int = validation_options()
    while True:
        try:
            num1:int = int(input("Enter a number: "))
            num2:int = int(input("Enter another number: "))
            break
        except ValueError:
            print("Invalidated value")

    result:float = calculator(num1, num2, option)
    print(f"The result: {result}")