import json
from pathlib import Path


class ReferenceDeleter:
    """Poistaa viitteen JSON-tiedostosta avaimen (key) perusteella."""

    def __init__(self, file: str = "data/references.json"):
        self.file = Path(file)

    def _load_all(self):
        """Lataa kaikki viitteet JSON-tiedostosta listana."""
        try:
            with self.file.open(encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_all(self, refs):
        """Kirjoittaa annetun viitelistan takaisin JSONiin."""
        self.file.parent.mkdir(parents=True, exist_ok=True)
        with self.file.open("w", encoding="utf-8") as f:
            json.dump(refs, f, ensure_ascii=False, indent=2)

    def delete_by_key(self, key: str) -> bool:
        """
        Poistaa viitteen annetun keyn perusteella.

        Palauttaa:
          True  – jos viite löytyi ja poistettiin
          False – jos viitettä ei löytynyt
        """
        refs = self._load_all()
        alku_maara = len(refs)

        refs_jalkeen = [r for r in refs if r.get("key") != key]

        if len(refs_jalkeen) == alku_maara:
            # mitään ei poistettu
            return False

        self._save_all(refs_jalkeen)
        return True
