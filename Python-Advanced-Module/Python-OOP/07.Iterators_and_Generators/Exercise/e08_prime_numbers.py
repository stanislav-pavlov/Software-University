def is_prime(num):
    if num <= 1:
        return False

    num_is_prime = True
    for i in range(2, num):
        if num % i == 0:
            num_is_prime = False
            break
    return num_is_prime


def get_primes(nums_list):
    for num in nums_list:
        if is_prime(num):
            yield num

print(list(get_primes([-2, 0, 0, 1, 1, 0])))