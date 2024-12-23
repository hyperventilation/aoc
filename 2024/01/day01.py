from collections import Counter


def read():
    with open('input.txt', 'r') as file:
        return zip(*((int(num0), int(num1)) for num0, num1 in (line.split() for line in file))) # илья колдун

def part1(numbers0, numbers1):
    return sum(abs(x-y) for x, y in zip(sorted(numbers0), sorted(numbers1)))

def calc_sim_score(numbers0, numbers1):
    count = Counter(numbers1)
    return sum(num * count[num] for num in numbers0)

if __name__ == '__main__':
    a0, a1 = read()
    print('part1', part1(a0, a1))
    print('part2', calc_sim_score(a0, a1))
