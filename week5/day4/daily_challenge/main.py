import re
with open('the_stranger.txt', 'r') as f:
    file = f.read().lower()

with open('stop.txt', "r") as r:
    stop_text = r.readlines()
class Text:
    new_li = []
    def __init__(self, text):
        self.text= text
       


    def create_new_li(self):
        li =[]
        for char in self.text:
            if not char.isalpha():
                li.append(char)
        original_string = file
        characters_to_remove = li
        new_string = original_string
        for character in characters_to_remove:
            new_string = new_string.replace(character, " ")
        new_li = new_string.split()
        return new_li

    def frenquency_of_word(self, word):

        x = self.create_new_li()
        counter = x.count(word)
        if counter < 2:
            return f'The word {word} exists {counter} time in the file'
        elif counter >= 2:
            return f'The word {word} exists {counter} times in the file'
        elif counter < 1:
            return None


    def unique_words(self):
        unique_words_li = []
        x = self.create_new_li()
        for word in x:
            if x.count(word) == 1:
                unique_words_li.append(word)
        return unique_words_li

    @classmethod
    def from_file(cls, file):
        with open(file, 'r') as f:
            file = f.read()
        return Text(file)
text1 = Text(file)
print(text1.frenquency_of_word('doze'))
print(text1.unique_words())
Text.from_file('the_stranger.txt')

class TextModification(Text):
    def __init__(self, file):
        super().__init__(file)
        self.file = file

    def remove_punctuation(self):
        new_file = re.sub("[.?',-_!:;()]","", self.file)
        return new_file

    def remove_stop_words(self):
        li = []
        for char in self.file:
            li.append(char)
            for stop in stop_text:
                for word in li:
                    print(word.replace(stop, ""), end="")

    def remove_special_chars(self):
        new_file = re.sub("[.?',-_!:;()+#@&^%*/ג™¦ €”]"," ", self.file)
        return new_file
text1 = TextModification(file)
print(text1.remove_punctuation())
text1.remove_stop_words()
print(text1.remove_special_chars())
