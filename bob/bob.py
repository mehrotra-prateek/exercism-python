def response(hey_bob):
    str=hey_bob.strip()
    if str == "":
        return "Fine. Be that way!"
    elif str.isupper() and hey_bob[-1] == "?":
        return "Calm down, I know what I'm doing!"
    elif str.isupper():
        return "Whoa, chill out!"
    elif str[-1] == "?":
        return "Sure."
    else:
        return "Whatever."