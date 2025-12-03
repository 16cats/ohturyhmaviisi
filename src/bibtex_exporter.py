import json
from pathlib import Path


class BibtexExporter:
    """Lukee viitteet JSON-tiedostosta ja kirjoittaa niistä BibTeX-tiedoston."""

    def __init__(self,
                 json_file: str = "data/references.json",
                 bibtex_file: str = "data/references.bib"):
        self.json_path = Path(json_file)
        self.bibtex_path = Path(bibtex_file)

    def _load_raw(self):
        """Lukee raakaviitteet JSON-tiedostosta."""
        try:
            with self.json_path.open(encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _one_entry_to_bibtex(self, ref: dict) -> str:
        """Muuttaa yhden viitteen BibTeX-merkinnäksi."""

        # tyyppi, esim. "@book" -> "book"
        ref_type_raw = ref.get("type", "@article") or "@article"
        ref_type = ref_type_raw.lstrip("@")  # poista mahdollinen @-merkki

        key = ref.get("key", "nokey")

        fields = ref.get("other fields", {}) or {}
        author = fields.get("author")
        title = fields.get("title")
        date = fields.get("date")  # käytetään year-kenttänä

        lines = [f"@{ref_type}{{{key},"]

        # Lisätään kentät vain jos niillä on arvo
        if author:
            lines.append(f"  author = {{{author}}},")
        if title:
            lines.append(f"  title = {{{title}}},")
        if date:
            lines.append(f"  year = {{{date}}},")

        # Poistetaan viimeisen rivin pilkku jos tarpeen
        if lines[-1].endswith(","):
            lines[-1] = lines[-1][:-1]

        lines.append("}")
        return "\n".join(lines)

    def export(self):
        """Generoi BibTeX-tiedoston kaikista viitteistä."""
        refs = self._load_raw()

        if not refs:
            print("Ei viitteitä, BibTeX-tiedostoa ei luotu.")
            return

        entries = [self._one_entry_to_bibtex(ref) for ref in refs]
        content = "\n\n".join(entries) + "\n"

        # Käytetään ihan suoraviivaista polkua tähän projektiin:
        output_dir = Path("data")
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / "references.bib"

        with output_path.open("w", encoding="utf-8") as f:
            f.write(content)

        # Tulostetaan varmuuden vuoksi myös absoluuttinen polku
        print(f"BibTeX-tiedosto generoitu: {output_path}")
        print(f"(Täydellinen polku: {output_path.resolve()})")

