class vowels:
    vowel_chars = 'eyuoai'

    def __init__(self, text):
        self.text = text
        self.idx = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        while self.idx < len(self.text):
            if self.text[self.idx].lower() not in vowels.vowel_chars:
                self.idx += 1
                continue

            char_to_return = self.text[self.idx]
            self.idx += 1
            return char_to_return

        raise StopIteration



my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
