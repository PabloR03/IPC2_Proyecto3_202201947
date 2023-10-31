class Mensaje:
    def __init__(self, text, date, user, hashtag):
        self.text = text
        self.date = date
        self.user = user
        self.hashtag = hashtag
    
    def dump(self):
        return {
            "text": self.text,
            "date": self.date,
            "user": self.user,
            "hashtag": self.hashtag
        }