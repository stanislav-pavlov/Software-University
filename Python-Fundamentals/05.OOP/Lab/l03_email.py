class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

line = input()

while line != "Stop":
    line_el = line.split(" ")
    sender = line_el[0]
    receiver = line_el[1]
    content = line_el[2]
    email = Email(sender, receiver, content)
    emails.append(email)

    line = input()

sent_emails_indices = list(map(int, input().split(", ")))

for x in sent_emails_indices:
    emails[x].send()

for x in emails:
    print(x.get_info())