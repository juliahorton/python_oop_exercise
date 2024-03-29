"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder():
    """
    
    Attributes
    ------------------

    file_path (str): absolute or relative path to a file on disk that contains words as strings, one word per line, to be used as a dictionary

    Doctests
    ------------------

    >>> file_path = "file.txt"

    >>> my_words  = "asymptotic\nBayesian\ncalodemon\ndemisemitone\nextracanonical"
    
    >>> def make_file(file_path):
            file = open(file_path, "w")
            file.write(my_words)
            file.close()

    >>> make_file(file_path)
    
    >>> wf = WordFinder(file_path)
    5 words read

    >>> wf.path == file_path
    True

    >>> wf.num_words == 5
    True

    >>> [word for word in wf.words] == my_words.splitlines()
    True

    >>> [word for word in wf.words].count(wf.random()) == 1
    True

    >>> [word for word in wf.words].count("awkward") == 1
    False

    >>> [word for word in wf.words].count("awkward") == 0
    True

    """

    def __init__(self, file_path):
        """Create class instance with list of words extracted from file at designated path"""
        self.path = file_path
        self.words = self.get_words()
        self.num_words = len(self.words)
        print(f"{self.num_words} words read")

    def get_words(self):
        """Read file and assign attribute containing list of words in dictionary"""
        dictionary = open(self.path, "r")
        words = []
        for word in dictionary:
            words.append(word.rstrip())
        dictionary.close()
        return words

    def random(self):
        """Return random word from dictionary"""
        return choice(self.words)

class SpecialWordFinder(WordFinder):
    """Subclass of WordFinder that is able to handle files with blank lines and comments that start with '#'"""

    def __init__(self, file_path):
        super().__init__(file_path)
        
    def get_words(self):
        """Read file and assign attribute containing list of words in dictionary, excluding blank lines and comments"""
        dictionary = open(self.path, "r")
        words = []
        for word in dictionary:
            if word[0].isalpha():
                words.append(word.rstrip())
        dictionary.close()
        return words