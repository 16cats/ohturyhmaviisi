import json
from pathlib import Path
from src.bibtex_exporter import BibtexExporter



def setup_test_data(tmp_file="data/test_references.json"):
    """Luo testidatan BibTeX-exportteria varten."""
    Path("data").mkdir(exist_ok=True)

    test_data = [
        {
            "type": "@book",
            "key": "TestBook01",
            "other fields": {
                "author": "Test Author",
                "title": "Testing Book Export",
                "date": "2020"
            }
        },
        {
            "type": "@article",
            "key": "TestArt02",
            "other fields": {
                "author": "Another Tester",
                "title": "Unit Testing BibTeX Generation",
                "date": "2023"
            }
        }
    ]

    with open(tmp_file, "w", encoding="utf-8") as f:
        json.dump(test_data, f, ensure_ascii=False, indent=2)

    return tmp_file


def read_file(path):
    """Lue tiedoston sisältö tekstinä."""
    if not Path(path).exists():
        return None
    return Path(path).read_text(encoding="utf-8")


def test_bibtex_export():
    print("== TEST: BibTeX exporter ==")

    # 1. Luo testidata
    json_path = setup_test_data()

    # 2. Luo exportteri (ohjataan se testitiedostoihin)
    exporter = BibtexExporter(
        json_file=json_path,
        bibtex_file="data/test_output.bib"
    )

    # 3. Aja export
    exporter.export()

    # 4. Lue tuotettu bib-tiedosto
    output = read_file("data/test_output.bib")

    if output is None:
        print("FAILED: BibTeX-tiedostoa ei luotu.")
        return

    print("\n--- Tuotettu BibTeX-tiedosto ---")
    print(output)
    print("--------------------------------\n")

    # 5. Tarkistetaan odotettu sisältö
    if "@book{TestBook01" in output and "@article{TestArt02" in output:
        print("SUCCESS: BibTeX-export sisältää molemmat merkinnät.")
    else:
        print("FAILED: BibTeX-export ei sisältänyt kaikkia merkintöjä.")


if __name__ == "__main__":
    test_bibtex_export()
