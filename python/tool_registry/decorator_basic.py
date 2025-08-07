def My_Decorator(func):

    def wrapper(*args,**kwargs):

        result =func(*args, **kwargs)

        return result
    return wrapper






@My_Decorator
def multiply(a, b):
    return a * b


print(multiply(5, 7))