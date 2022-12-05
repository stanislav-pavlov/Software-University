class ValueCannotBeNegative(Exception):
    """Value is below zero"""
    pass


N = 5

for _ in range(N):
    num = int(input())
    if num < 0:
        raise ValueCannotBeNegative
