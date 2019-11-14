from datetime import datetime


def add(moment):
    try:
        return datetime.fromtimestamp(moment.timestamp() + (10 ** 9))
    except Exception:
        print('Not a date')
