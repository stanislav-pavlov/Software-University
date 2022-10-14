def emoticon_finder(text):
    emoticons = [text[i] + text[i+1] for i in range(len(text)) if text[i] == ':' and text[i+1] != ' ']
    print(*emoticons, sep = '\n')


data = input()
emoticon_finder(data)