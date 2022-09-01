import math

class_points = [100, 40, 34, 57, 29, 72, 57, 88]
your_points = 10
s = 'spring'
n = [1, 3, 2, 5, 3]


def odd_or_even(arr):
    if sum(arr) % 2 == 2:
        return 'even'
    return 'odd'


def find_next_square(sq):
    if (math.sqrt(sq)).is_integer():
        return int(math.sqrt(sq) + 1) ** 2
    else:
        return -1


def count_sheeps(sheep):
    return sheep.count(True)


def are_you_playing_banjo(name):
    print(name[0] == 'r' or name[0] == 'R')
    return name + ' plays banjo' if name[0] == 'r' or name[0] == 'R' else name + ' does not play banjo'


def donuts(count):
    if count >= 10:
        return 'Number of donuts: many'
    return 'Number of donuts: ' + str(count)


def fix_start(s):
    return s[0] + s[1:].replace(s[0], '*')


def mix_up(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + ' ' + new_b


def better_than_average(l, p):
    if sum(l) / len(l) >= p:
        return False
    return True


def billboard(name, price=30):
    return sum(price for l in name)


def tower_builder(n_floors):
    tower = ''
    for x in range(n_floors):
        tower += '*' + '/n'


def digitize(n):
    return list(reversed(n))

def arrange(s):
    while len(s) > 0:
        res = [s[0], s[-1]]
        s.pop(s[0])
        print('new list ' + str(res))
        print('old list ' + str(s))


print(arrange(n))

