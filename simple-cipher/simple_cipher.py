from secrets import choice
from string import ascii_lowercase as char


class Cipher:
    def __init__(self, key=None):
        self.key = key or "".join(choice(char) for i in range(100))

    def check_key(self, text):
        pass

    def encode(self, text):
        encrypted_val = ""
        for pos in range(len(text)):
            key = self.key[pos % len(self.key)]
            char_index = char.index(text[pos]) + char.index(key)
            encrypted_val += char[char_index % len(char)]
        return encrypted_val

    def decode(self, text):
        decrypted_val = ""
        for pos in range(len(text)):
            key = self.key[pos % len(self.key)]
            char_index = char.index(text[pos]) - char.index(key)
            decrypted_val += char[char_index % len(char)]
        return decrypted_val
