import unittest
from unittest.mock import patch
from app import App

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App()

    @patch("builtins.input", side_effect=["@book", "TestiKey", "Otsikko", "Tekijä", "25.11.2025"])
    def test_lisaa_viite(self, mock_input): # pylint: disable=unused-argument
        viite = self.app.lisaa_viite()

        self.assertEqual(viite.ref_type, "@book")
        self.assertEqual(viite.key, "TestiKey")
        self.assertEqual(viite.other_fields["title"], "Otsikko")
        self.assertEqual(viite.other_fields["author"], "Tekijä")
        self.assertEqual(viite.other_fields["date"], "25.11.2025")
