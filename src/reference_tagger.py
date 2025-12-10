import json
from pathlib import Path


class ReferenceTagger:
    """Lisää, muokkaa ja poistaa tageja viitteistä."""

    def __init__(self, file: str = "data/references.json"):
        self.file = Path(file)

    def _load_all(self):
        try:
            with self.file.open(encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_all(self, refs):
        self.file.parent.mkdir(parents=True, exist_ok=True)
        with self.file.open("w", encoding="utf-8") as f:
            json.dump(refs, f, ensure_ascii=False, indent=2)

    def add_tag(self, key: str, tag: str) -> bool:
        """Lisää yksittäisen tägin viitteeseen."""
        refs = self._load_all()
        found = False

        for ref in refs:
            if ref.get("key") == key:
                tags = ref.get("tags")

                if tags is None:
                    tags = []
                elif isinstance(tags, str):
                    tags = [tags]

                if tag not in tags:
                    tags.append(tag)

                ref["tags"] = tags
                found = True
                break

        if not found:
            return False

        self._save_all(refs)
        return True

    def set_tags(self, key: str, new_tags) -> bool:
        """Korvaa viitteen tagit uudella listalla (muokkaus)."""
        if isinstance(new_tags, str):
            new_tags = [t.strip() for t in new_tags.split(",") if t.strip()]

        refs = self._load_all()
        found = False

        for ref in refs:
            if ref.get("key") == key:
                ref["tags"] = new_tags
                found = True
                break

        if not found:
            return False

        self._save_all(refs)
        return True

    def clear_tags(self, key: str) -> bool:
        """Poistaa kaikki tagit viitteeltä."""
        refs = self._load_all()
        found = False

        for ref in refs:
            if ref.get("key") == key:
                if "tags" in ref:
                    del ref["tags"]
                found = True
                break

        if not found:
            return False

        self._save_all(refs)
        return True
