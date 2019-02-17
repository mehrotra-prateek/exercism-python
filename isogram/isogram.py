def is_isogram(string=""):
    if type(string) is not str:
        raise Exception('Not a string')
    else:
        string = list(filter(str.isalpha, string.lower()))
        return len(set(string)) == len(string)




