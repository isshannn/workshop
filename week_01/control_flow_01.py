import sys

def check_operator_input(argument):
    if argument:                        
        # 1(F) : T nand T || c(T): T nand F
        if(not( isinstance(argument,str) and argument.isdecimal() ) ):
            print("Invalid input - Please enter a number betweem 1 and 4") 
            return None
        else:
            argument = int(argument)
            if (argument > 0 and argument < 5):
                return enter_values(argument)     
            else:
                print("Please Enter value between 1 to 4")
                return None
    print("NONE value passed")
    exit(0)
    return None 

def check_operand_input(argument):
    if argument:
        # any_digit(F): t nand t || any_charc(T): T nand F
        if(not( isinstance(argument,str) and argument[0].isdigit() )):
            print("Invalid Input ",argument[0]," please enter a number")
            return None
        else:
            argument = float(argument)
            if (argument >= sys.float_info.max or argument <= sys.float_info.min):
                print("Evaluation out of computational range")
                return None
            print("Valid Input")
            return argument
    print("NONE value passed")
    return None

def enter_values(argument):
    print("Enter the values of a and b")
    a = input()
    a = check_operand_input(a)
    b = input()
    b = check_operand_input(b)   
    match argument:
        case 1: return a+b
        case 2: return a-b
        case 3: return a*b
        case 4: return a/b
        case default: return "Invalid choice"

print("1: Addition")
print("2: Substraction")
print("3: Multiplication")
print("4: Division")
print("Enter your choice: ")

c = input()
c = check_operator_input(c)
print(c)

