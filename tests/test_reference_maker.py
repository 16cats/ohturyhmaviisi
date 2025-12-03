import unittest
from src.reference_maker import ReferenceMaker

class TestReferenceMaker(unittest.TestCase):
    def setUp(self):
        ref_type = "@book"
        key = "TestKey"
        other_fields = {
            "title": "TestiOtsikko",
            "author": "Minä",
            "date": "25.11.2025"
        }

        self.maker = ReferenceMaker(ref_type, key, other_fields)

    def test_konstruktori(self):
        self.assertEqual(self.maker.id, 1)
        self.assertEqual(self.maker.ref_type, "@book")
        self.assertEqual(self.maker.key, "TestKey")
        self.assertEqual(self.maker.other_fields["title"], "TestiOtsikko")
        self.assertEqual(self.maker.other_fields["author"], "Minä")
        self.assertEqual(self.maker.other_fields["date"], "25.11.2025")

    def test_tee_json(self):
        json = {
            "type": "@book",
            "key": "TestKey",
            "other fields": {
                "title": "TestiOtsikko",
                "author": "Minä",
                "date": "25.11.2025"
            }
        }

        self.assertEqual(self.maker.tee_json(), json)
