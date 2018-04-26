def parameters_listing(*args, **kwargs):
    listenning = 'The arguments are:\n\t['

    for idx, arg in enumerate(args):
        if idx > 0:
            listenning += f', {arg}'
        else:
            listenning += f'{arg}'

    listenning += ']\n\nAnd the argument dictionary is:\n\t{'

    items = list(kwargs.items())
    items.sort()
    for idx, (k, w) in enumerate(items):
        if idx > 0:
            listenning += f', {k} : {w}'
        else:
            listenning += f'{k} : {w}'

    listenning +='}'

    return listenning


x1 = 1
x2 = 2
w1 = 'w1'
w2 = 'w2'
print(parameters_listing(x1, x2, k1=w1, k2=w2))


def tagger(tag):
    def tag_decorator(func):
        def func_wrapper(*args, **kwargs):
            return f'{tag}\n{func(*args, **kwargs)}\n{tag}'

        return func_wrapper

    return tag_decorator


@tagger('!!!!!!!!!!!!!!!!!!!!!!!!        DECORATOR       !!!!!!!!!!!!!!!!!!!!!!!!!!')
def parameters_listing2(*args, **kwargs):
    return parameters_listing(*args, **kwargs)


print(parameters_listing2(x1, x2, k1=w1, k2=w2))