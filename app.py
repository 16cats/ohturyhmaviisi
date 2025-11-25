from reference_maker import ReferenceMaker

class App:

    kentat = ["title", "author", "date"]

    def lisaa_viite(self):
        print("Lisää uusi viite")
        ref_type = input("Type (e.g. @book): ")
        key = input("Key: ")

        other_fields = {}

        for kentta in self.kentat:
            syote = input(f"{kentta.capitalize()}: ")
            if syote:
                other_fields[kentta] = syote

        return ReferenceMaker(ref_type, key, other_fields)
