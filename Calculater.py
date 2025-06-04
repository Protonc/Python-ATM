
def calculate(n1, o, n2):
    if o == "*" :
        return n1 * n2
    
    elif o == "/":
        try: 
            return n1 / n2
        except ZeroDivisionError:
            return "U cant divide a number by 0"

    elif o == "+":
        return n1 + n2
    
    elif o == "-":
        return n1 - n2
    
    elif o == "**":
        return n1 ** n2




while True:
    n1 = int(input("Enter no 1: "))
    o = input("enter operation from +, -, /, *, **: ")
    n2 = int(input("Enter no 2: "))
    print(calculate(n1,o,n2))



