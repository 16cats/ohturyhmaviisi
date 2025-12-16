import unittest
from unittest.mock import patch
from io import StringIO
from src.reference_editor import ReferenceEditor

class TestReferenceEditor(unittest.TestCase):
    def setUp(self):
        self.editor = ReferenceEditor()
        self.data = [
            {
                "id": "0",
                "type": "Koira",
                "key": "Avain",
                "other fields": {
                "title": "Otsikko",
                "author": "Kirjailija",
                "date": "15.12.2025"
                }
            },
            {
                "id": "1",
                "type": "Kissa",
                "key": "Avain2",
                "other fields": {
                "title": "Otsikko2",
                "author": "Kirjailija2",
                "date": "16.12.2025"
                }
            }
        ]

        def test_save(data):
            self.data = data

        self.editor.load = lambda: self.data
        self.editor.save = test_save

    def test_list_id_and_name(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.editor.list_id_and_name()
            output = mock_stdout.getvalue()

        expected_output = "Anna sen viitteen id, jota haluat muokata.\n0 - Avain\n1 - Avain2\n"
        self.assertEqual(output, expected_output)


    @patch("builtins.input", side_effect=["@book", "", "Uusi Otsikko", "", ""])
    def test_edit_reference(self, mock_input): # pylint: disable=unused-argument
        self.editor.edit_reference("0")
        self.assertEqual(self.data[0]["id"], "0")
        self.assertEqual(self.data[0]["type"], "@book")
        self.assertEqual(self.data[0]["key"], "Avain")
        self.assertEqual(self.data[0]["other fields"]["title"], "Uusi Otsikko")

    def test_bad_id(self):
        output = self.editor.edit_reference("3")
        self.assertEqual(output, False)