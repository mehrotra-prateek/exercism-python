def is_pangram(sentence=""):
    try:
        if (len(set(list(filter(str.isalpha, sentence.lower())))) == 26):
            return True 
        else:
            return False
    except Exception:
        print("Not a Sentence")