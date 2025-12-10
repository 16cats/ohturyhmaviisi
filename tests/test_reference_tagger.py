# tests/test_reference_tagger.py

import json
from src.reference_tagger import ReferenceTagger


def _write_refs(tmp_path, refs):
    path = tmp_path / "refs.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump(refs, f, ensure_ascii=False, indent=2)
    return path


def _read_refs(path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def test_add_tag_to_reference(tmp_path):
    refs = [
        {"key": "K1", "type": "@book", "other fields": {"title": "T1"}},
    ]
    path = _write_refs(tmp_path, refs)
    tagger = ReferenceTagger(file=str(path))

    ok = tagger.add_tag("K1", "palaa tähän lähteeseen")

    assert ok is True
    updated = _read_refs(path)
    assert updated[0].get("tags") == ["palaa tähän lähteeseen"]


def test_add_tag_does_not_duplicate(tmp_path):
    refs = [
        {
            "key": "K1",
            "type": "@book",
            "other fields": {"title": "T1"},
            "tags": ["palaa tähän lähteeseen"],
        },
    ]
    path = _write_refs(tmp_path, refs)
    tagger = ReferenceTagger(file=str(path))

    ok = tagger.add_tag("K1", "palaa tähän lähteeseen")

    assert ok is True
    updated = _read_refs(path)
    assert updated[0].get("tags") == ["palaa tähän lähteeseen"]


def test_add_tag_returns_false_if_key_not_found(tmp_path):
    refs = [
        {"key": "K1", "type": "@book", "other fields": {"title": "T1"}},
    ]
    path = _write_refs(tmp_path, refs)
    tagger = ReferenceTagger(file=str(path))

    ok = tagger.add_tag("K2", "joku tägi")

    assert ok is False
    updated = _read_refs(path)
    assert updated == refs


def test_set_tags_replaces_existing_tags(tmp_path):
    refs = [
        {
            "key": "K1",
            "type": "@book",
            "other fields": {"title": "T1"},
            "tags": ["vanha", "epätarkka"],
        },
    ]
    path = _write_refs(tmp_path, refs)
    tagger = ReferenceTagger(file=str(path))

    ok = tagger.set_tags("K1", "tärkeä, palaa tähän lähteeseen")

    assert ok is True
    updated = _read_refs(path)
    assert updated[0].get("tags") == ["tärkeä", "palaa tähän lähteeseen"]


def test_clear_tags_removes_tag_field(tmp_path):
    refs = [
        {
            "key": "K1",
            "type": "@book",
            "other fields": {"title": "T1"},
            "tags": ["jokin tägi"],
        },
    ]
    path = _write_refs(tmp_path, refs)
    tagger = ReferenceTagger(file=str(path))

    ok = tagger.clear_tags("K1")

    assert ok is True
    updated = _read_refs(path)
    assert "tags" not in updated[0]


def test_clear_tags_returns_false_if_key_not_found(tmp_path):
    refs = [
        {"key": "K1", "type": "@book", "other fields": {"title": "T1"}},
    ]
    path = _write_refs(tmp_path, refs)
    tagger = ReferenceTagger(file=str(path))

    ok = tagger.clear_tags("K2")

    assert ok is False
    updated = _read_refs(path)
    assert updated == refs
