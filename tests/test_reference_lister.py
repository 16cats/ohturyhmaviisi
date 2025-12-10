import unittest
import tempfile
import json
import os

from src.reference_lister import ReferenceLister


class TestReferenceLister(unittest.TestCase):

    def _create_temp_file(self, data):
        """Kirjoittaa JSON-dataa tilapäiseen tiedostoon testejä varten."""
        with tempfile.NamedTemporaryFile(
            delete=False, mode="w", encoding="utf-8"
        ) as tmp:
            json.dump(data, tmp, ensure_ascii=False)
            filename = tmp.name
        return filename

    def test_formatted_references(self):
        # Testataan että muotoiltu viite palautetaan oikeassa tekstimuodossa
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

        filename = self._create_temp_file(ref_data)
        lister = ReferenceLister(filename)

        # Tässä suoritetaan varsinainen metodi
        refs = lister.formatted_references()

        # Testataan: viitteitä on 1
        self.assertEqual(len(refs), 1)
        # Testataan: muoto on tasan oikein
        self.assertEqual(refs[0], "Minä (25.11.2025): Testiotsikko [TestKey]")

        os.remove(filename)

    def test_references_by_author(self):
        # Testataan kirjoittajan perusteella rajaaminen
        ref_data = [
            {
                "type": "@book",
                "key": "k1",
                "other fields": {"author": "Albert Einstein"}
            },
            {
                "type": "@article",
                "key": "k2",
                "other fields": {"author": "Ada Lovelace"}
            }
        ]

        filename = self._create_temp_file(ref_data)
        lister = ReferenceLister(filename)

        # Haetaan viitteet, joissa kirjoittajan nimessä esiintyy "einstein"
        results = lister.references_by_author("einstein")

        # Vain yksi viite täsmää
        self.assertEqual(len(results), 1)
        # Ja se tulee olla k1
        self.assertEqual(results[0]["key"], "k1")

        os.remove(filename)
        
    def test_references_by_year(self):
        # Testataan viitteiden rajausta julkaisuvuoden perusteella
        ref_data = [
            {
                "type": "@book",
                "key": "a1",
                "other fields": {"date": "1999"}
            },
            {
                "type": "@article",
                "key": "a2",
                "other fields": {"date": "2000"}
            },
            {
                "type": "@misc",
                "key": "a3",
                "other fields": {"date": "1999"}
            }
        ]

        filename = self._create_temp_file(ref_data)
        lister = ReferenceLister(filename)

        # Haetaan kaikki 1999
        results = lister.references_by_year("1999")

        # Tuloksia tulee 2:
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["key"], "a1")
        self.assertEqual(results[1]["key"], "a3")

        os.remove(filename)

    def test_references_by_type(self):
        # Testataan viitteiden rajausta julkaisutyypin mukaan
        ref_data = [
            {"type": "@book", "key": "b1", "other fields": {}},
            {"type": "@article", "key": "b2", "other fields": {}},
            {"type": "@book", "key": "b3", "other fields": {}}
        ]

        filename = self._create_temp_file(ref_data)
        lister = ReferenceLister(filename)

        # Haetaan BOOK
        results = lister.references_by_type("book")

        # Tuloksia tulee 2 (@book)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["key"], "b1")
        self.assertEqual(results[1]["key"], "b3")

        os.remove(filename)

    def test_format_one_empty(self):
        # Testataan tilanne, jossa viite on tyhjä {}
        filename = self._create_temp_file([{}])
        lister = ReferenceLister(filename)

        # format_one palauttaa tällöin "{}"
        result = lister.formatted_references()
        self.assertEqual(result[0], "{}")

        os.remove(filename)