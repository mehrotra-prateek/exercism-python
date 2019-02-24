from datetime import datetime

def add_gigasecond(moment):
    try:
        newdate= datetime.fromtimestamp(moment.timestamp() + (10 ** 9))
        return newdate
    except Exception:
        print('Not a date')