def part1(file_name: str):
    raw_len = 0
    txt_len = 0
    with open(file_name, 'r', encoding='utf-8') as text_file:
        lines = text_file.read()
        for line in lines.split('\n'):
            raw_len += len(line)
            txt_len += len(eval(line))
    print(f'Raw Length: {raw_len}')
    print(f'Text Length: {txt_len}')
    print(f'AOC 2022 Day 8 Part 1: {raw_len - txt_len}')


def part2(file_name: str):
    raw_len = 0
    enc_len = 0
    with open(file_name, 'r', encoding='utf-8') as text_file:
        lines = text_file.read()
        for line in lines.split('\n'):
            raw_len += len(line)
            enc_line = '"' + line.replace('\\', '\\\\').replace('"', '\\"') + '"'
            enc_len += len(enc_line)
            # print(f'Raw: {line}\tEncoded: {enc_line}')
    print(f'Raw Length: {raw_len}')
    print(f'Encoded Length: {enc_len}')
    print(f'AOC 2022 Day 8 Part 2: {enc_len - raw_len}')


if __name__ == '__main__':
    part1('../../resources/2015/inputd8-a.txt')
    part1('../../resources/2015/inputd8.txt')
    part2('../../resources/2015/inputd8-a.txt')
    part2('../../resources/2015/inputd8.txt')