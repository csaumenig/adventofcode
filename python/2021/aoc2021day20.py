YEAR = 2021
DAY = 20


def part1(file_name_str: str) -> None:
    enhance_algorithm, image = read_file(file_name_str)
    print(f'Algorithm = {enhance_algorithm}')
    step = 0
    lit_pixels = count_lit_pixels(step, image)
    for step in range(1, 3):
        image = enhance_image(enhance_algorithm, image)
        lit_pixels = count_lit_pixels(step, image)
    print(f'Day {DAY} Part 1: After {step} steps, Number of Lit Pixels = {lit_pixels}')


def part2(file_name_str: str) -> None:
    enhance_algorithm, image = read_file(file_name_str)
    print(f'Day {DAY} Part 2: ANSWER')


def read_file(file_name_str: str) -> tuple[str, dict[tuple[int, int], str]]:
    enhance_algorithm = ''
    grid: dict[tuple[int, int], str] = {}
    r = 0
    lines = [line.strip() for line in open(file_name_str, 'r').readlines()]
    for line in lines:
        if line != '':
            if enhance_algorithm == '':
                enhance_algorithm = line
            else:
                c = 0
                for char in line:
                    grid.update({(r, c): char})
                    c += 1
                r += 1
    return enhance_algorithm, grid


def count_lit_pixels(step: int,
                     image: dict[tuple[int, int], str]) -> int:
    print(f'Step = {step}')
    print(f'Image = {image}')
    lit_pixels = sum([1 if v == '#' else 0 for v in image.values()])
    print(f'Lit Pixels = {lit_pixels}')
    return lit_pixels


def enhance_image(algorithm: str,
                  image: dict[tuple[int, int], str]) -> dict[tuple[int, int], str]:
    rows = max

    for row in range(0, )


    return image

if __name__ == '__main__':
    file_name = f'../../resources/{YEAR}/inputd{DAY}a.txt'
    part1(file_name)
    part2(file_name)

    # file_name = f'../../resources/{YEAR}/inputd{DAY}.txt'
    # part1(file_name)
    # part2(file_name)
