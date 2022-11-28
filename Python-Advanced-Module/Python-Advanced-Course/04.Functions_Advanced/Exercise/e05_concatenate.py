def concatenate(*args, **kwargs):
    updated_str = ''.join(args)

    for key, value in kwargs.items():
        if key in updated_str:
            updated_str = updated_str.replace(key, value)

    return updated_str


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))