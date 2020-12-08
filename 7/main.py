import re

INPUT_FILE = './input/input.txt'
COLOR_REGEX = '(\w+ \w+) bags contain'

class Node(object):
    def __init__(self, color, contains={}):
        self.color = color
        self.contains = contains
        self.cardinalities = {}


def build_rules_graph(rules):
    index = {}
    # Contruimos un grafo con la informacion de las mochilas
    for r in rules:
        if 'no other bags' in r:
            node = Node(re.match(COLOR_REGEX, r).group(1))
            index[node.color] = node
        else:
            childrens = {}
            cardinalities = {}
            for match in re.findall("(?P<cardinality>(\d) (\w+ \w+) bags?)", r.split('contain')[1]):
                cardinalities[match[2]] = int(match[1])
                if match[2] in index:
                    childrens[match[2]] = index[match[2]]
                else:
                    node = Node(match[2], {})
                    childrens[match[2]] = node
                    index[match[2]] = node

            color = re.match(COLOR_REGEX, r).group(1)
            if color in index:
                index[color].contains.update(childrens)
                index[color].cardinalities.update(cardinalities)
            else:
                index[color] = Node(color, childrens)
                index[color].cardinalities.update(cardinalities)

    return index


def can_contain_color(node, color):
    if color in node.contains:
        return {node.color}
    else:
        if node.contains:
            for child in node.contains.values():
                if can_contain_color(child, color):
                    return {node.color}

        return {}

def count_bags_inside(node):
    if node.contains == {}:
        return 0
    else:
        inside = 0
        for color, cardinality in node.cardinalities.items():
            inside += cardinality + cardinality*count_bags_inside(node.contains[color])

        return inside


def solve_1(nodes_index):
    valids = set()
    for bag in nodes_index.values():
        valids.update(can_contain_color(bag, 'shiny gold'))

    return len(valids)


def solve_2(nodes_index):
    return count_bags_inside(nodes_index['shiny gold'])


if __name__ == '__main__':
    with open(INPUT_FILE) as input:
        rules = input.readlines()

    nodes_index = build_rules_graph(rules)
    bags = solve_1(nodes_index)
    print("Number of bags that can contain a shiny gold bag is: ", bags)

    bags = solve_2(nodes_index)
    print("Number of bags that shiny gold must contain is: ", bags)
