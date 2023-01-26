def vowel_filter(function):
    vowels = 'eyuioa'

    def wrapper():
        result = function()
        vowels_only = []
        for letter in result:
            if letter in vowels:
                vowels_only.append(letter)
        return vowels_only
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
