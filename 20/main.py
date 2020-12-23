from copy import deepcopy
from collections import defaultdict

INPUT_FILE = './input/example.txt'


class Image():
    def __init__(self, tile_number, matrix):
        self.tile_number = tile_number
        self.matrix = matrix

        # This represents the 4 possible neighbors of 1 image
        self.up = None
        self.down = None
        self.left = None
        self.right = None

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
                current_image.append(list(line))

        # last image
        if current_image:
            images[current_title_image] = Image(current_title_image, current_image)

    return images


def check_is_neighbor(image, candidate):
    is_neighbor = False

    if image.matrix[0] == candidate.matrix[-1]:
        image.up = candidate
        candidate.down = image
        is_neighbor = True
    elif image.matrix[-1] == candidate.matrix[0]:
        image.down = candidate
        candidate.up = image
        is_neighbor = True
    elif [x[-1] for x in candidate.matrix] == [x[0] for x in candidate.matrix]:
        image.right = candidate
        candidate.left = image
        is_neighbor = True
    elif [x[0] for x in candidate.matrix] == [x[-1] for x in candidate.matrix]:
        image.left = candidate
        candidate.right = image
        is_neighbor = True

    return is_neighbor

def find_neighbors(img, img_list):
    neighbors_list = list()
        
    if img.tile_number == 1489:
        import pdb; pdb.set_trace()

    for tile, candidate in img_list.items():
        if candidate == img:
            continue

        if img.tile_number == 1171 and candidate == 1489:
            import pdb; pdb.set_trace()


        # Comprobar si la imagen encaja directamente con el candidato
        if check_is_neighbor(img, candidate):
            neighbors_list.append(candidate)
            continue

        # comprobar si la imagen encaja con el candidato rotado 90, 180, 270 grados
        rotated = deepcopy(candidate)
        for i in range(3):
            rotated.rotate()
            is_neighbor = check_is_neighbor(img, rotated)
            if is_neighbor:
                neighbors_list.append(rotated)
                img_list[tile] = rotated
                break
        else:

            # comporobar si la imagen encaja con el candidato invertido izq dcha
            flipped = deepcopy(candidate)
            flipped.flip_image_horizontally()
            if check_is_neighbor(img, flipped):
                neighbors_list.append(flipped)
                img_list[tile] = flipped
                continue

            # comprobar si la imagen encaja con el candidato invertido arriba abajo
            flipped = deepcopy(candidate)
            flipped.flip_image_vertically()
            if check_is_neighbor(img, flipped):
                neighbors_list.append(flipped)
                img_list[tile] = flipped
                continue

    return neighbors_list

def solve_1(images):
    adyacence_list = defaultdict(list)

    for tile, img_to_check in images.items():
        neighbors = find_neighbors(img_to_check, images)
        adyacence_list[tile] += neighbors

    import pdb; pdb.set_trace()
    return adyacence_list

if __name__ == '__main__':
    images = parse_input()
    adyacences = solve_1(images)

    n = 1
    for k, v in adyacences.items():
        if len(v) == 2:
            n *= k

    print(n)
