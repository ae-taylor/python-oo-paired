import random


class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file_path):
        self.file_path = file_path
        self.words = open(f"{file_path}", "r").read()
        self.word_list = self.words.split("\n")
        print(len(self.word_list), "words read")

    def random(self):
        return random.choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words in a file with hash tags
    or empty new lines"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.word_list = [word for word in self.word_list
                          if not word.startswith("#") and word]
