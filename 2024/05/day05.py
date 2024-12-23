from collections import defaultdict, deque

def read(path):
    with open(path, 'r') as file:
        return file.readlines()

def handle(input):
    rules = []
    updates = []
    are_rules = True
    for line in input:
        line = line.strip()
        if line == '':
            are_rules = False
            continue

        if are_rules:
            x, _, y = line.partition('|')
            rules.append((int(x), int(y)))
        else:
            updates.append([int(i) for i in line.split(',')])
    return rules, updates

def p1(rules, update: list[int]):
    rule_dict = {}
    for x, y in rules:
        if x not in rule_dict:
            rule_dict[x] = []
        rule_dict[x].append(y)

    for x in update:
        if x in rule_dict:
            for y in rule_dict[x]:
                if y in update and update.index(x) > update.index(y):
                    return False
    return True

def sort_updates(rules, update):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    update_set = set(update)

    for node in update:
        in_degree[node] = 0

    for rule in rules:
        x, y = rule
        if x in update_set and y in update_set:
            graph[x].append(y)
            in_degree[y] += 1

    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []

    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update

if __name__ == '__main__':
    rules, updates = handle(read('input.txt'))
    counter = [0,0]
    for update in updates:
        if p1(rules, update): # p1
            counter[0] += update[len(update)//2]
        else: # p2
            new_update = sort_updates(rules, update)
            counter[1] += new_update[len(new_update)//2]
    print(counter)