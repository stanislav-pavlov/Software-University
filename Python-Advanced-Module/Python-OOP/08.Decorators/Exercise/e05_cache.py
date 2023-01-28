def cache(func_ref):
    memo = {}

    def wrapper(num):
        if num in memo:
            return memo[num]
        exec_func = func_ref(num)
        memo[num] = exec_func
        return exec_func
    wrapper.log = memo
    return wrapper




@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
