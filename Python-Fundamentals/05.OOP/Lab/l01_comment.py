class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


#new_comment = Comment("stuni7o", "Bannat si")

comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)
