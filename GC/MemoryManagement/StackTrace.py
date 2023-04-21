"""Example of functions being added to the stack"""

class HeapObject():
    def __init__(self, number: int) -> None:
        self.number = number

def function_1():
    pretend_number1 = HeapObject(1)
    function_2()

def function_2():
    pretend_number2 = HeapObject(2)
    function_3()

def function_3():
    x = 1 / 0

if __name__ == '__main__':
    function_1()