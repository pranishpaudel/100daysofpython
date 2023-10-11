import time

def decorator_function(function):

    def wrapper_func():
        time.sleep(2)
        function()

    return wrapper_func


@decorator_function
def return_hello():
    print("HEELO!!!!!!!")


