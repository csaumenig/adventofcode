YEAR = 2015
DAY = 10


def look_and_say(line: str) -> str:
    output = ''
    current_count = None
    last_int = None
    for x in line:
        current_int = int(x)
        if last_int is not None:
            if last_int == current_int:
                current_count += 1
                continue
            output += f'{current_count}{last_int}'
        last_int = current_int
        current_count = 1
    output += f'{current_count}{last_int}'
    return output


def part1(file_name: str,
          num_iters: int):
    with open(file_name, 'r') as f:
        lines = f.read()
        for line in lines.split('\n'):
            output = line
            for i in range(num_iters):
                output = look_and_say(output)
            print(f'AOC {YEAR} Day {DAY} Part 1: Run {num_iters} times: {line} -> {output} [{len(output)}]')


if __name__ == '__main__':
    part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt', 1)
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt', 40)
    part1(f'../../resources/{YEAR}/inputd{DAY}.txt', 50)
