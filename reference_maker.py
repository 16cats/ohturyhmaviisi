class ReferenceMaker:
    def __init__(self, ref_type, key, other_fields):
        self.ref_type = ref_type
        self.key = key
        self.other_fields = other_fields

    def tee_json(self):
        return {
            "type": self.ref_type,
            "key": self.key,
            "other fields": self.other_fields
        }
