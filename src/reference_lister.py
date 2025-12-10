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

    def format_one(self, ref):
        key = ref.get("key", "")
        fields = ref.get("other fields", {}) or {}

        author = fields.get("author", "")
        date = fields.get("date", "")
        title = fields.get("title", "")
        tags = ref.get("tags", [])

        line = ""
        if author:
            line += author
        if date:
            line += f" ({date})"
        if title:
            line += f": {title}"
        if key:
            line += f" [{key}]"

        # LISÄYS: näytetään tagit lopussa
        if tags:
            if isinstance(tags, list):
                tags_text = ", ".join(tags)
            else:
                tags_text = str(tags)
            line += f" (tagit: {tags_text})"

        line = line.strip()
        if not line:
            line = str(ref)
        return line



    def formatted_references(self):
        return [self.format_one(ref) for ref in self._load_raw()]

    def print_references(self):
        print("Viitteet:")
        for line in self.formatted_references():
            print(f"- {line}")
        print("Viitteiden listaus valmis.")

    def references_by_author(self, author_query):
        result = []
        for ref in self._load_raw():
            author = ref.get("other fields", {}).get("author", "") or ""
            if author_query.lower() in author.lower():
                result.append(ref)
        return result

    def references_by_year(self, year):
        result = []
        for ref in self._load_raw():
            date = ref.get("other fields", {}).get("date", "") or ""
            if date == year:
                result.append(ref)
        return result

    def print_by_author(self, author):
        print(f"Viitteet – rajattu kirjoittajan mukaan: {author}")
        for ref in self.references_by_author(author):
            print(f"- {self.format_one(ref)}")
        print("Listaus valmis.")

    def print_by_year(self, year):
        print(f"Viitteet – rajattu vuodelle: {year}")
        for ref in self.references_by_year(year):
            print(f"- {self.format_one(ref)}")
        print("Listaus valmis.")

    def references_by_type(self, type_query):
        result = []
        for ref in self._load_raw():
            ref_type = ref.get("type", "")
            if type_query.lower() in ref_type.lower():
                result.append(ref)
        return result

    def print_by_type(self, type_query):
        print(f"Viitteet – rajattu julkaisutyypin mukaan: {type_query}")
        for ref in self.references_by_type(type_query):
            print(f"- {self.format_one(ref)}")
        print("Listaus valmis.")