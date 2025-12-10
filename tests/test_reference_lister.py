import unittest
import tempfile
import json
import os

from src.reference_lister import ReferenceLister


class TestReferenceLister(unittest.TestCase):

    def test_formatted_references(self):
        # Data samassa muodossa kuin ReferenceSaver kirjoittaa
        ref_data = [
            {
                "type": "@book",
                "key": "TestKey",
                "other fields": {
                    "title": "Testiotsikko",
                    "author": "Minä",
                    "date": "25.11.2025"
                }
            }
        ]

        # Luodaan väliaikainen tiedosto ja kirjoitetaan JSON sinne
        with tempfile.NamedTemporaryFile(
            delete=False, mode="w", encoding="utf-8"
        ) as tmp:
            json.dump(ref_data, tmp, ensure_ascii=False)
            filename = tmp.name

        try:
            # Käytetään ReferenceListeriä tämän tiedoston kanssa
            lister = ReferenceLister(filename)
            refs = lister.formatted_references()

            # 1) Löytyy yksi viite
            self.assertEqual(len(refs), 1)

            # 2) Muoto on oikea
            self.assertEqual(
                refs[0],
                "Minä (25.11.2025): Testiotsikko [TestKey]"
            )
        finally:
            # Siivotaan väliaikainen tiedosto pois
            os.remove(filename)
