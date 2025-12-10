import json
import os


class ReferenceMaker:
    next_id = 0
    # os.path.dirname(__file__) => src => .. => data => references.json
    CONFIG_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "references.json")

    @classmethod
    def load_next_id(cls):
        # load last id from json
        if os.path.exists(cls.CONFIG_FILE):
            try:
                with open(cls.CONFIG_FILE, 'r') as f:
                    data = json.load(f)
                    if isinstance(data, list) and len(data) > 0:
                        # find the highest possible id and add 1
                        max_id = max(int(ref["id"]) for ref in data if "id" in ref)
                        cls.next_id = max_id + 1
            except (json.JSONDecodeError, ValueError):
                cls.next_id = 0

    def __init__(self, ref_type, key, other_fields):
        self.id = str(ReferenceMaker.next_id)  # id as string
        ReferenceMaker.next_id += 1
        self.ref_type = ref_type
        self.key = key # user-defined unique key
        
        self.other_fields = other_fields

    def tee_json(self):
        return {
            "id": self.id,
            "type": self.ref_type,
            "key": self.key,
            "other fields": self.other_fields
        }
    
    