def my_sum(x, *args):
    result = x
    for arg in args:
        result = result + arg
    return result
