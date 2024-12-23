def read(path):
    with open(path, 'r') as file:
        return [l.strip() for l in file.readlines()]

def p1(grid, target):
    rows, cols = len(grid), len(grid[0])
    occurrences = []

    # horizontal
    for row in range(rows):
        for col in range(cols - len(target) + 1):
            if ''.join(grid[row][col:col+len(target)]) == target:
                occurrences.append((row, col))

    # vert
    for row in range(rows - len(target) + 1):
        for col in range(cols):
            if ''.join([grid[row+i][col] for i in range(len(target))]) == target:
                occurrences.append((row, col))

    # top-left -> bottom-right
    for row in range(rows - len(target) + 1):
        for col in range(cols - len(target) + 1):
            if ''.join([grid[row+i][col+i] for i in range(len(target))]) == target:
                occurrences.append((row, col))

    # bottom-left -> top-right
    for row in range(len(target)-1, rows):
        for col in range(cols - len(target) + 1):
            if ''.join([grid[row-i][col+i] for i in range(len(target))]) == target:
                occurrences.append((row-len(target)+1, col))

    return occurrences


def p2(grid):
    counter = 0
    rows, cols = len(grid), len(grid[0])
    for row in range(rows-2):
        for col in range(cols-2):
            if grid[row+1][col+1] == 'A' and ((grid[row][col] == 'S' and grid[row+2][col+2] == 'M') and (grid[row+2][col] == 'S' and grid[row][col+2] == 'M') or (grid[row][col] == 'M' and grid[row+2][col+2] == 'S') and (grid[row+2][col] == 'M' and grid[row][col+2] == 'S') or (grid[row][col] == 'M' and grid[row+2][col+2] == 'S') and (grid[row+2][col] == 'S' and grid[row][col+2] == 'M') or (grid[row][col] == 'S' and grid[row+2][col+2] == 'M') and (grid[row+2][col] == 'M' and grid[row][col+2] == 'S')):
                    counter +=1
    return counter




if __name__ == '__main__':
    print(len(p1(read('input.txt'), "XMAS")) + len(p1(read('input.txt'), "SAMX")))
    print(p2(read('input.txt')))