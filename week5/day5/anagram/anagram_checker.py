

class AnagramChecker:
    def __init__(self):
        with open("anagram.txt", 'r') as f:
            self.words_li = f.readlines()
            self.new_li = [word.strip() for word in self.words_li]

    def is_valid_word(self, word):
        if word.upper() in self.new_li:
            return True
        else:
            return False


    def get_anagrams(self, word):
        if self.is_valid_word(word):
            anagram_li = []
            for char in self.new_li:
                if len(char) == len(word):
                    if sorted(char) == sorted(word.upper()):
                        anagram_li.append(char)
            return anagram_li

