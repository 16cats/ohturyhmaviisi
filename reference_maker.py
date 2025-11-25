class ReferenceMaker:
    def __init__(self, title, author, date):
        self.title = title
        self.author = author
        self.date = date

    def tee_json(self):
        return {
            "title": self.title,
            "author": self.author,
            "date": self.date
        }
