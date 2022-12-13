def add_songs(*args):
    songs_dict = {}

    for pair in args:
        song_name = pair[0]
        lyrics = pair[1]
        if song_name not in songs_dict:
            songs_dict[song_name] = lyrics
        else:
            songs_dict[song_name] += lyrics

    result = ''
    for key, value in songs_dict.items():
        if value:
            lyric_sheet = '\n'.join(value)
            result += f'- {key}\n{lyric_sheet}\n'
        else:
            result += f'- {key}\n'

    return result


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
