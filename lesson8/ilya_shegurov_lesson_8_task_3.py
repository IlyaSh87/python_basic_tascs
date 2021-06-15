from functools import wraps


def type_logger(prefix):
    def decorate(f):
        def wrapper(*args):
            print(prefix, f.__name__, "args", args)
            cr = f(*args)
            print(prefix, f.__name__, "result", cr)
            return cr
        return wrapper
    return decorate


@type_logger('test')
def calc_cube(x):
     return int(x**3)



num = calc_cube(5)
print(type(num))









