from string import punctuation


class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open('files_3/' + file_name, encoding='utf-8') as file:
                all_words[file_name] = []
                for line in file:
                    for char_p in punctuation:
                        if char_p != '-':
                            line = line.replace(char_p, '')
                        else:
                            line = line.replace(' - ', ' ')
                    for word in line.split(' '):
                        all_words[file_name] += [word.strip()]
        return all_words

    def find(self, word):
        return {key: [x.lower() for x in value].index(word.lower())
                if (word.lower() in [x.lower() for x in value]) else 0
                for key, value in self.get_all_words().items()}

    def count(self, word):
        return {key: [x.lower() for x in value].count(word.lower())
                if (word.lower() in [x.lower() for x in value]) else 0
                for key, value in self.get_all_words().items()}


finder2 = WordsFinder('1.txt', '2.txt', '3.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('teXT'))  # 3 слово по счёту
print(finder2.count('teXt'))  # 4 слова teXT в тексте всего
