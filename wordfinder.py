import random


class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file_path):
        word_file = open(file_path, "r")
        self.word_list = self.parse_file(word_file)
        print(len(self.word_list), "words read")

    def parse_file(self, word_file):
        """Removes whitespace/new line from a file"""
        return [word.strip() for word in word_file]

    def random(self):
        """Picks a random word from a list of words"""
        return random.choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words in a file with hash tags
    or empty new lines"""

    def parse_file(self, word_file):
        """Removes #, new lines, and spaces from a file"""
        return [word.strip() for word in word_file
                if not word.startswith("#") and word.strip()]
