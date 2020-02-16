import math
def get_number(number):
    if isinstance(number, int):
        print(" a number was passed to the function")
        
        if number % 2 == 0:
            print(' the number is even')
        else:
            print(' the number is odd')
        
        if number < 0:
            print("""the number is negative so the 
            square root is not returned""")
            return 0
        else:
            return math.sqrt(number)
    else:
        print('passed argument is not a number \
        please pass a number and try again')
        
        return 0

get_number(30)