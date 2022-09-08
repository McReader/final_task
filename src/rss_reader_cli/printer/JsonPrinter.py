import json


class JsonPrinter:
    def print(self, entries: list) -> None:
        print(json.dumps(entries, indent=2))
