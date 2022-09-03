vowels = ['a', 'o', 'u', 'e', 'i']
initial_txt = input()

no_vowels_list = [ch for ch in initial_txt if ch.lower() not in vowels]

print("".join(no_vowels_list))