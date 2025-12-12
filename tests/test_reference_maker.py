import unittest
from src.reference_maker import ReferenceMaker

class TestReferenceMaker(unittest.TestCase):
    def setUp(self):
        ReferenceMaker.next_id = 0  # reset id counter before each test
        self.maker = ReferenceMaker(
            "@book",
            "TestKey",
            {
                "title": "TestiOtsikko",
                "author": "Minä",
                "date": "2002"
            }
        )
        
    def test_konstruktori(self):
        self.assertEqual(self.maker.id, "0")
        self.assertEqual(self.maker.ref_type, "@book")
        self.assertEqual(self.maker.key, "TestKey")
        self.assertEqual(self.maker.other_fields["title"], "TestiOtsikko")
        self.assertEqual(self.maker.other_fields["author"], "Minä")
        self.assertEqual(self.maker.other_fields["date"], "2002")

    def test_tee_json(self):
        json = {
            "id": "0",
            "type": "@book",
            "key": "TestKey",
            "other fields": {
                "title": "TestiOtsikko",
                "author": "Minä",
                "date": "2002"
            }
        }

        self.assertEqual(self.maker.tee_json(), json)
