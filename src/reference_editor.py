import json

class ReferenceEditor:

    def __init__(self, file="data/references.json"):
        self.file = file

    def load(self):
        try:
            with open(self.file, encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        return data

    def save(self, data):
        with open(self.file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def list_id_and_name(self):
        data = self.load()

        print("Anna sen viitteen id, jota haluat muokata.")

        for ref in data:
            if ("id" in ref and "key" in ref):
                print(ref["id"] + " - " + ref["key"])

    def edit_reference(self, id_input):
        data = self.load()
        found = None

        for ref in data:
            if ("id" in ref and id_input == ref["id"]):
                found = ref
                break

        if found is None:
            print("Viitettä ei löytynyt")
            return False

        print("Muokkaa haluamiasi kenttiä.\nPaina pelkkä enter, "
        "jos et halua muokata kenttää.")

        for field, value in found.items():
            if field == "id":
                continue

            if field == "other fields":
                for field2, value2 in value.items():
                    new = input(f"{field2} - [{value2}]: ")
                    if new:
                        value[field2] = new

            else:
                new = input(f"{field} - [{value}]: ")
                if new:
                    found[field] = new

        self.save(data)

        return True
