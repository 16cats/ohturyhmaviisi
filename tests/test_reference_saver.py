import unittest
import tempfile
import json
from reference_saver import ReferenceSaver
from reference_maker import ReferenceMaker

class TestReferenceSaver(unittest.TestCase):

    def test_save(self):
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            filename = tmp.name

        saver = ReferenceSaver(filename)

        ref_type = "@book"
        key = "TestKey"
        other_fields = {
            "title": "TestiOtsikko",
            "author": "Minä",
            "date": "25.11.2025"
        }

        viite = ReferenceMaker(ref_type, key, other_fields)

        saver.tallenna(viite)

        with open(filename, encoding="utf-8") as file:
            data = json.load(file)

        self.assertEqual(data[0]["type"], "@book")
        self.assertEqual(data[0]["key"], "TestKey")
        self.assertEqual(data[0]["other fields"]["title"], "TestiOtsikko")
        self.assertEqual(data[0]["other fields"]["author"], "Minä")
        self.assertEqual(data[0]["other fields"]["date"], "25.11.2025")
