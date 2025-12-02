import json


class ReferenceLister:
    """Lukee viitteet JSON-tiedostosta ja tulostaa ne
    ihmisen luettavassa muodossa.
    """

    def __init__(self, file="data/references.json"):
        self.file = file

    def _load_raw(self):
        """Palauttaa listan raakaviitteitä JSONista."""
        try:
            with open(self.file, encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def formatted_references(self):
        """Palauttaa listan valmiita merkkijonoja tulostusta varten."""
        refs = []

        for ref in self._load_raw():
            id_ = ref.get("id", "")
            key = ref.get("key", "")
            fields = ref.get("other fields", {}) or {}

            author = fields.get("author", "")
            date = fields.get("date", "")
            title = fields.get("title", "")

            # Rakenna merkkijono ihan käsin, EI joinilla
            line = ""
            if id_ != "":
                line += f" [ID:{id_}]"
            if author:
                line += author
            if date:
                line += f" ({date})"
            if title:
                line += f": {title}"
            if key:
                line += f" [{key}]"

            line = line.strip()
            if not line:
                line = str(ref)

            refs.append(line)

        return refs

    def print_references(self):
        """Tulostaa viitteet kuten käyttöliittymässä."""
        print("References:")
        for line in self.formatted_references():
            print(f"- {line}")
        print("Reference listing done.")
