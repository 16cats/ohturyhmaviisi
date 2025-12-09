# tests/test_reference_deleter.py

import json
from src.reference_deleter import ReferenceDeleter


def _write_refs(tmp_path, refs):
    path = tmp_path / "refs.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump(refs, f, ensure_ascii=False, indent=2)
    return path


def _read_refs(path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def test_delete_existing_reference(tmp_path):
    refs = [
        {"key": "A1", "type": "@book", "other fields": {"title": "T1"}},
        {"key": "B2", "type": "@article", "other fields": {"title": "T2"}},
    ]
    path = _write_refs(tmp_path, refs)

    deleter = ReferenceDeleter(file=str(path))

    ok = deleter.delete_by_key("A1")

    assert ok is True

    left = _read_refs(path)
    assert len(left) == 1
    assert left[0]["key"] == "B2"


def test_delete_non_existing_reference_returns_false_and_keeps_data(tmp_path):
    refs = [
        {"key": "A1", "type": "@book", "other fields": {"title": "T1"}},
    ]
    path = _write_refs(tmp_path, refs)

    deleter = ReferenceDeleter(file=str(path))

    ok = deleter.delete_by_key("ZZZ")

    assert ok is False
    left = _read_refs(path)
    assert left == refs
