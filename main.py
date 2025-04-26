import hashlib


class NemesisTranslator:
    def __init__(self, words: dict=None):
        if words is None:
            words = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I',
                     'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R',
                     's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', '0': '0',
                     '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
        self.words = words
        self.sha = hashlib.sha256()

    def translate(self, original: str) -> str:
        translated = {} # DB
        if original not in translated:
            self.sha.update(original.encode('utf-8'))
            encoded = [self.words[str(character)] for character in self.sha.hexdigest()[:10]]
            translated[original] = ''.join(encoded)
            return ''.join(encoded)
        return translated[original]


if __name__ == '__main__':
    t = NemesisTranslator()
    print(t.translate('asdf'))
