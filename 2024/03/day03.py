import regex

def read(path: str):
    with open(path, 'r') as file:
        return file.read()

def part1():
    ctr = 0
    pattern = r"mul\(\d+,\d+\)"
    for match in regex.finditer(pattern, read('input.txt')):
        n0, n1 = [int(i) for i in match.group(0)[4:-1].split(',')]
        ctr += n0*n1
    return ctr

def part2():
    ctr = 0
    flag = True
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    matches = regex.findall(pattern, read('input.txt'))

    for match in matches:
        if match[:3] == 'mul':
            if flag:
                n0, n1 = [int(i) for i in match[4:-1].split(',')]
                ctr += n0 * n1
        elif match[:3] == 'do(': # do
            flag = True
        elif match[:3] == 'don': # dont
            flag = False

    return ctr


if __name__ == '__main__':
    print(part1())
    print(part2())
