import re

INPUT_FILE = './input/input.txt'
COLOR_REGEX = '(\w+ \w+) bags contain'

class Node(object):
    def __init__(self, color, contains={}, is_contained_in={}):
        self.color = color
        self.contains = contains
        self.is_contained_in = is_contained_in

def can_contain_color(node, color):
    if color in node.contains:
        return {node.color}
    else:
        if node.contains:
            for child in node.contains.values():
                if can_contain_color(child, color):
                    return {node.color}

        return {}

def build_rules_graph(rules):
    nodes_index = {}
    # Contruimos un grafo con la informacion de las mochilas
    for r in rules:
        if 'no other bags' in r:
            node = Node(re.match(COLOR_REGEX, r).group(1))
            nodes_index[node.color] = node
        else:
            childrens = {}
            for match in re.findall("(\d (\w+ \w+) bags?)", r.split('contain')[1]):
                if match[1] in nodes_index:
                    childrens[match[1]] = nodes_index[match[1]]
                else:
                    node = Node(match[1], {})
                    childrens[match[1]] = node
                    nodes_index[match[1]] = node

            color = re.match(COLOR_REGEX, r).group(1)
            if color in nodes_index:
                nodes_index[color].contains.update(childrens)
            else:
                nodes_index[color] = Node(color, childrens)

    return nodes_index

def solve_1(rules):
    nodes_index = build_rules_graph(rules)

    valids = set()
    for bag in nodes_index.values():
        valids.update(can_contain_color(bag, 'shiny gold'))

    return len(valids)


if __name__ == '__main__':
    with open(INPUT_FILE) as input:
        rules = input.readlines()

    bags = solve_1(rules)
    print("Number of bags that can contain a shiny gold bag is: ", bags)
