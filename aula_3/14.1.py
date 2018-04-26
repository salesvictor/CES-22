def merge_a(x, y):
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(x) or yi >= len(y):
            return result

        if x[xi] < y[yi]:
            xi += 1

        if y[yi] < x[xi]:
            yi += 1

        if x[xi] == y[yi]:
            result.append(x[xi])
            xi += 1
            yi += 1


def merge_b(x, y):
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(x):
            return result

        if yi >= len(y):
            result.extend(x[xi:])
            return result

        if x[xi] < y[yi]:
            result.append(x[xi])
            xi += 1

        if y[yi] < x[xi]:
            yi += 1

        if x[xi] == y[yi]:
            xi += 1
            yi += 1


def merge_c(x, y):
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(x):
            result.extend(y[yi:])
            return result

        if yi >= len(y):
            return result

        if x[xi] < y[yi]:
            result.append(y[yi])
            xi += 1

        if y[yi] < x[xi]:
            yi += 1

        if x[xi] == y[yi]:
            xi += 1
            yi += 1


def merge_d(x, y):
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(x):
            result.append(y[yi])
            return result

        if yi >= len(y):
            result.extend(x[xi:])
            return result

        if x[xi] < y[yi]:
            result.append(x[xi])
            xi += 1

        if y[yi] < x[xi]:
            result.append(y[yi])
            yi += 1

        if x[xi] == y[yi]:
            xi += 1
            yi += 1


def merge_e(x, y):
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(x):
            return result

        if yi >= len(y):
            result.extend(x[xi:])
            return result

        if x[xi] < y[yi]:
            result.append(x[xi])
            xi += 1

        if y[yi] < x[xi]:
            yi += 1

        if x[xi] == y[yi]:
            xi += 1
            yi += 1
    return result


print(merge_a([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7, 9]))
print(merge_b([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7, 9]))
print(merge_c([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7, 9]))
print(merge_d([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7, 9]))
print(merge_e([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7, 9]))
