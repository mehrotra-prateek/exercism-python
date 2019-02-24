from datetime import datetime

def add_gigasecond(moment):
    try:
        return datetime.fromtimestamp(moment.timestamp() + (10 ** 9))
    except Exception:
        print('Not a date')