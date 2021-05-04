def list(x):
    try:
        return sum(x)/len(x)
    except TypeError:
        return "TypeError"
    except ZeroDivisionError:
        return "Emptylist"
        