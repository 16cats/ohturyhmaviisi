import json

class ReferenceSaver:
    def __init__(self, file="data/references.json"):
        self.file = file

    def tallenna(self, viite):
        try:
            with open(self.file, encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(viite.tee_json())

        with open(self.file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)