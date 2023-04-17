"""Example of functions being added to the stack"""

def function_1():
    function_2()

def function_2():
    function_3()

def function_3():
    x = 1 / 0

if __name__ == '__main__':
    function_1()