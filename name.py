def input_name(x,y):
    try:
        return x + " " + y
    except TypeError:
        return "TypeError"
        