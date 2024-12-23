import itertools

def calculate_result(numbers, operators, part):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif part == 2 and operators[i] == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def is_equation_possible(test_value, numbers, part):
    operators = ['+', '*']
    if part == 2: operators.append('||')
    for op_combination in itertools.product(operators, repeat=(len(numbers) - 1)):
        if calculate_result(numbers, op_combination, part) == test_value:
            return True
    return False

def read():
    equations = []
    with open('input.txt') as f:
        for line in f:
            n, nums = line.split(':')
            nums = [int(i) for i in nums[1:].split(' ')]
            equations.append((int(n), nums))
    return equations

if __name__ == "__main__":
    equations = read()
    total_calibration_result = 0
    for test_value, numbers in equations:
        if is_equation_possible(test_value, numbers, 1):
            total_calibration_result += test_value

    print("part1:", total_calibration_result)

    total_calibration_result = 0

    for test_value, numbers in equations:
        if is_equation_possible(test_value, numbers, 2):
            total_calibration_result += test_value

    print("part2:", total_calibration_result)

