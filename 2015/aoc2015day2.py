def step1(input_str: str):
    box_dimensions = [tuple(x.split('x')) for x in input_str.split('\n')]
    box_areas = []
    for x in box_dimensions:
        box_areas.append(tuple(x[0]*x[1], x[1]*x[2], x[0]*x[2]))


if __name__ == '__main__':
    with open('resources/inputd2.txt', 'r') as f:
         test_input = f.read()


