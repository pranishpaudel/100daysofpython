# inputs = eval(input())
# # TODO: Create the logging_decorator() function 👇
# def logging_decorator(function):
#   def wrapper(*args):
#     called_func= f"a_function({*args})"
#     insa= function(args[0],args[1],args[2])
#     return f"You called {called_func} \n Its value was {insa}"
#   return wrapper


# # TODO: Use the decorator 👇
# @logging_decorator
# def a_function(a, b, c):
#   return a * b * c


# a_function(inputs[0], inputs[1], inputs[2])


inputs = eval(input())

# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        called_func = f"{function(*args)}"
        insa = function(*args)
        return f"You called {called_func} \n Its value was {insa}"
    return wrapper

# TODO: Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
    return a * b * c

# Call the decorated function using the provided inputs
result = a_function(*inputs)
print(result)
