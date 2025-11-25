from reference_maker import ReferenceMaker

class App:
    def lisaa_viite(self):
        print("Lisää uusi viite")
        title = input("Title: ")
        author = input("Author: ")
        date = input("Date: ")

        return ReferenceMaker(title, author, date)
