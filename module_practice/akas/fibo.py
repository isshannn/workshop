# Fibonacci numbers module
def fib(n):
    a, b = 0, 1
    if (is_input_valid(n)):
        while a < n:
            print(a, end=' ' )
            a, b = b, a+b
        print()

def fib2(n): # Return Fibonacci series upto n 
    if (is_input_valid(n)):
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a+b
        return result

def is_input_valid(x):
    if(isinstance(x, str)):
        print("String Values are not allowed. Enter a positive integer")
        return False
    if x < 0:
        print("Negative Numbers are not allowed!")
        return False
    return True

if __name__ == "__main__":
    import sys
    print("You are in main of ")
    fib(int(sys.argv[1]))
