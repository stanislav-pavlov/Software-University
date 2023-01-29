def store_results(func_ref):
    def wrapper(*args):
        executed_func = func_ref(*args)
        result = f"Function '{func_ref.__name__}' was called. Result: {executed_func}"
        with open('./results.txt', 'a') as file:
            file.write(f"Function '{func_ref.__name__}' was called. Result: {executed_func}")
            file.write('\n')

        return result

    return wrapper




@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

print(add(2, 2))
print(mult(6, 4))
