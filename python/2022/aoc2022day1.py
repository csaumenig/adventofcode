def part1(file_name: str):
    most_cals = 0
    this_cals = 0

    with open(file_name, 'r') as f:
        lines = f.read()
        for line in lines.split('\n'):
            if line.strip() == '':
                if this_cals > most_cals:
                    most_cals = this_cals
                this_cals = 0
            else:
                this_cals += int(line)

    if this_cals > most_cals:
        most_cals = this_cals
    print(f'AOC 2022 Day 1 Part 1: {most_cals}')


def part2(file_name: str):
    elf_cals = {}
    cals = 0
    elf_num = 1
    with open(file_name, 'r') as f:
        lines = f.read()
        for line in lines.split('\n'):
            if line.strip() == '':
                elf_cals.update({elf_num: cals})
                elf_num += 1
                cals = 0
            else:
                cals += int(line)
    sorted_elf_cals = {k: v for k, v in sorted(elf_cals.items(), key=lambda item: item[1], reverse=True)}

    count = 1
    total = 0
    for k, v in sorted_elf_cals.items():
        if count > 3:
            break
        total += v
        count += 1
    print(f'AOC 2022 Day 1 Part 2: {total}')


if __name__ == '__main__':
    part1('../../resources/2022/inputd1.txt')
    part2('../../resources/2022/inputd1.txt')
