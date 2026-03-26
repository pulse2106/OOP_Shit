def divide(x, y):
    print("I am in divide")
    #raise TypeError(" Invalid input")
    return x / y
 
def calculate(a, b):
    print("I am in calculate")
    try:
        result = divide(a, b)
        print(f"Result: {result}")

    except ZeroDivisionError: ### handle known exception
        print("You can't divide a number by zero!")

    except TypeError:
         print("invalid value type. please provide integer")

    except Exception as err: ### rest of exceptions handles here
        print("Opps ... error ",err)

    else:
        print("division is OK") ### this code block will be call if NO excption
    finally:
        print("I am the finally block")### this block will be call in both cases
        print("do the clean-ups here")

calculate(10, 2)

calculate(10, 0)
