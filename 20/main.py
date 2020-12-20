from copy import deepcopy
from collections import defaultdict

INPUT_FILE = './input/input.txt'

class Image():
    def __init__(self, tile_number, matrix):
        self.tile_number = tile_number
        self.matrix = matrix

    def flip_image_horizontally(self):
        new_img = []
        for row in self.matrix:
            new_img.append(row[::-1])

        self.matrix = new_img

    def flip_image_vertically(self):
        self.matrix = self.matrix[::-1]

    def rotate(self):
        """
        Do not return anything, modify self.matrix in-place instead.
        https://stackoverflow.com/questions/61881822/rotate-a-matrix-by-90-degrees
        """
        top = 0
        bottom = len(self.matrix)
        total_layers = round(bottom / 2)

        for i in range(0, total_layers):
            for j in range(top, bottom - 1):
                top_left = self.matrix[top][j]
                top_right = self.matrix[j][bottom - 1]
                bottom_right = self.matrix[bottom - 1][-(j + 1)]
                bottom_left = self.matrix[- (1+j)][top]
                self.matrix[top][j] = bottom_left
                self.matrix[j][bottom-1] = top_left
                self.matrix[bottom - 1][- (j + 1)] = top_right
                self.matrix[-(1 + j)][top] = bottom_right
            top += 1
            bottom -= 1

def parse_input():
    images = {}
    current_title_image = 0
    current_image = []

    with open(INPUT_FILE) as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                # Skip empty lines
                continue
            if 'Tile' in line:
                # This represent we are going to read a new image

                # This if is to avoid adding the first empty image,
                # TODO: check if we can do this in a more pythonic way
                if current_image:
                    images[current_title_image] = Image(current_title_image, current_image)

                current_title_image = int(line.replace(':', '').split(' ')[1])
                current_image = []
            else:
                current_image.append(line)

        # last image
        if current_image:
            images[current_title_image] = Image(current_title_image, current_image)

    return images


def find_corner(images):
    pass

def find_neighbors(img, img_list):
    neighbors_list = []

    # flipped = deepcopy(img)
    # flipped.flip_image()
    img_frontiers = [img.matrix[0], img.matrix[-1], ''.join([x[0] for x in img.matrix]), ''.join([x[-1] for x in img.matrix])]
    # img_frontiers += [flipped.matrix[0], flipped.matrix[-1], ''.join([x[0] for x in flipped.matrix]), ''.join([x[-1] for x in flipped.matrix])]

    for candidate in img_list:
        if candidate == img:
            continue

        # if img.tile_number == 3079 and candidate.tile_number == 2311:
            # import pdb; pdb.set_trace()
        candidate_frontiers = [candidate.matrix[0], candidate.matrix[-1], ''.join([x[0] for x in candidate.matrix]), ''.join([x[-1] for x in candidate.matrix])]
        flipped = deepcopy(candidate)
        flipped.flip_image_vertically()
        candidate_frontiers += [flipped.matrix[0], flipped.matrix[-1], ''.join([x[0] for x in flipped.matrix]), ''.join([x[-1] for x in flipped.matrix])]
        flipped = deepcopy(candidate)
        flipped.flip_image_horizontally()
        candidate_frontiers += [flipped.matrix[0], flipped.matrix[-1], ''.join([x[0] for x in flipped.matrix]), ''.join([x[-1] for x in flipped.matrix])]

        """
        ..##.#..#.  #.#.#####.
        ##..#.....  .#..######
        #...##..#.  ..#.......
        ####.#...#  ######....
        ##.##.###.  ####.#..#.
        ##...#.###  .#...#.##.
        .#.#.#..##  #.#####.##
        ..#....#..  ..#.###...
        ###...#.#.  ..#.......
        ..###..###  ..#.###...

        ..###..###  #.#.#####.
        ###...#.#.  .#..######
        ..#....#..  ..#.......
        .#.#.#..##  ######....
        ##...#.###  ####.#..#.
        ##.##.###.  .#...#.##.
        ####.#...#  #.#####.##
        #...##..#.  ..#.###...
        ##..#.....  ..#.......
        ..##.#..#.  ..#.###...

        """

        if any([x in img_frontiers for x in candidate_frontiers]):
            neighbors_list.append(candidate.tile_number)

    return neighbors_list

def solve_1(images):
    adyacence_list = defaultdict(list)

    for tile, img_to_check in images.items():
        neighbors = find_neighbors(img_to_check, images.values())
        adyacence_list[tile] += neighbors

    return adyacence_list

if __name__ == '__main__':
    images = parse_input()
    adyacences = solve_1(images)

    n = 1
    for k, v in adyacences.items():
        if len(v) == 2:
            print(k)
            n *= k

    print(n)
