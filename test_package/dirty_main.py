def addition(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Делить на ноль нельзя!"
    return a / b


func_list = [name for (name, obj) in vars().items()
             if hasattr(obj, '__class__')
             and obj.__class__.__name__ == "function"]
