def is_pangram(sentence=""):
    if (len(set(list(filter(str.isalpha, sentence.lower())))) == 26):
        return True
    else:
        return False