def even_parameters(func_ref):
    def is_even_num(x):
        if isinstance(x, int) and x % 2 == 0:
            return True

    def wrapper(*args):
        for argument in args:
            if not is_even_num(argument):
                result = "Please use only even numbers!"
                return result
        return func_ref(*args)
    return wrapper




@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))
