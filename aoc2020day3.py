def count_trees(input_str: str,
                slope: tuple):
    terrain_map = input_str.split('\n')
    x_pos = 0
    y_pos = 0
    tree_count = 0

    while y_pos < len(terrain_map):
        spot_type = get_spot_type(terrain_map, x_pos, y_pos)
        if spot_type == '#':
            tree_count = tree_count + 1
        x_pos = x_pos + slope[0]
        y_pos = y_pos + slope[1]
    print('For slope R{} D{}, the Tree Count is: {}'.format(slope[0], slope[1], tree_count))
    return tree_count


def multiply_tree_counts(input_str: str,
                         slopes: list):
    slope_counts = []
    for this_slope in slopes:
        slope_counts.append(count_trees(input_str, this_slope))

    from numpy import prod
    product = prod(slope_counts)
    print('The product of all the tree counts is: {}'.format(product))


def get_spot_type(terrain_map: list,
                  x_pos: int,
                  y_pos: int):
    this_line = terrain_map[y_pos]
    this_index = x_pos % len(this_line)
    this_spot = this_line[this_index]
    return this_spot


if __name__ == '__main__':
    with open('resources/inputd3.txt', 'r') as f:
        test_input = f.read()

    print('Part1: ')
    count_trees(test_input, (3, 1))
    print('')
    print('')
    print('Part2: ')
    multiply_tree_counts(test_input, [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ])
