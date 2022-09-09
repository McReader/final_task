from .Writter import Writter


class FileWritter(Writter):
    "Prints the list of feed entries to the file"

    def __init__(self, path: str):
        self.path = path

    def write(self, content: str) -> None:
        "Prints the content to the file"

        with open(f"{self.path}", 'w') as file:  # Use file to refer to the file object
            file.write(content)
