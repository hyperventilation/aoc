def read():
    with open('input.txt', 'r') as file:
        return [[int(i) for i in line.split()] for line in file]

def is_monotonic(sequence):
    trend = None
    for i in range(1, len(sequence)):
        diff = sequence[i] - sequence[i - 1]
        if not 1 <= abs(diff) <= 3:
            return False
        if trend is None:
            trend = diff > 0
        elif trend != (diff > 0):
            return False
    return True

def is_valid_sequence_with_removal(sequence):
    if is_monotonic(sequence):
        return True
    for i in range(len(sequence)):
        if is_monotonic(sequence[:i] + sequence[i+1:]):
            return True
    return False

def part1():
    return sum(1 for sequence in read() if is_monotonic(sequence))

def part2():
    return sum(1 for sequence in read() if is_valid_sequence_with_removal(sequence))

if __name__ == '__main__':
    print(part1())
    print(part2())


