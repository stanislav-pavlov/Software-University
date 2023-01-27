def logged(func_ref):
    def wrapper(*args):
        executed_func = func_ref(*args)
        result = f"you called {func_ref.__name__}{args}\nit returned {executed_func}"
        return result

    return wrapper




@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))
