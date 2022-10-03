def enrcryption(initial_txt):
    encrypted_txt = ''.join([chr(ord(character)+3) for character in initial_txt])
    print(encrypted_txt)


line = input()
enrcryption(line)