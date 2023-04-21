"""Examples of using multiple decorators on a function"""

def decorator1(func):
    def wrapper(*args, **kwargs):
        print('Decorator 1 before function call')
        result = func(*args, **kwargs)
        print('Decorator 1 after function call')
        return result
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print('Decorator 2 before function call')
        result = func(*args, **kwargs)
        print('Decorator 2 after function call')
        return result
    return wrapper

def decorator3(func):
    def wrapper(*args, **kwargs):
        print('Decorator 3 before function call')
        result = func(*args, **kwargs)
        print('Decorator 3 after function call')
        return result
    return wrapper

@decorator1
@decorator2
@decorator3
def my_function(x, y):
    print(f'My function called with x={x}, y={y}')
    return x + y

result = my_function(3, 4)
print(result)