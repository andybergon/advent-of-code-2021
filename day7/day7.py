import sys


def load(filename):
    with open(filename) as f:
        line = f.readline()
        return [int(n) for n in line.split(',')]


def min_max(l):
    return min(l), max(l)


def get_cost_1(l, pos):
    return sum(abs(pos - e) for e in l)


def get_cost_2(l, pos):
    return sum(triangular_number(abs(pos - e)) for e in l)


def triangular_number(n):
    return n * (n + 1) // 2


def get_min_cost(l, cost_f):
    min, max = min_max(l)
    min_cost = sys.maxsize
    for i in range(min, max + 1):
        cost = cost_f(l, i)
        if cost < min_cost:
            min_cost = cost
    return min_cost


def part_one(filename):
    l = load(filename)
    cost = get_min_cost(l, get_cost_1)
    print(cost)


def part_two(filename):
    l = load(filename)
    cost = get_min_cost(l, get_cost_2)
    print(cost)


# part_one('day7.txt')  # 356179 # 8 min
part_two('day7.txt')  # 99788435 # 4 min
