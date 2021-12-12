display = ['', '', '', '', '', '', '', '', '', '']
display[1] = 'CF'

display[7] = 'ACF'

display[4] = 'BCDF'

display[2] = 'ACDEG'
display[3] = 'ACDFG'
display[5] = 'ABDFG'

display[0] = 'ABCEFG'
display[9] = 'ABCDFG'
display[6] = 'ABDEFG'

display[8] = 'ABCDEFG'


solve_it = {
    'a': 'C',
    'b': 'F',
    'c': 'G',
    'd': 'A',
    'e': 'B',
    'f': 'D',
    'g': 'E'
}

# ab dab eafb cdfbe gcdfa fbcad cefabd cdfgeb cagedb acedgfb |
# cdfeb fcadb cdfeb cdbaf
# 5 3 5 3
# ab -> CF => (ab ~ CF)
# abd -> ACF => (d = A)
# abef -> BCDF => (ef ~ BD)
# cdf -> ADG => (cf ~ DG)
# bcdef -> (ABDG)b
# acdfg -> (ADG)ag ->
# abcdf -> ACDFG
# cf -> AG
# abcdef ->
# bcdefg ->
# abcdeg ->
# abcdefg -> ABCDEFG

def part1(input_str: str) -> None:
    count = 0
    for line in input_str.split('\n'):
        for output_num in line.split('|')[1].strip().split(' '):
            if len(output_num) in (2,3,4,7):
                count += 1
    print(f'Day 8 Part 1: Count: {count}')


def part2(input_str: str) -> None:
    total = 0
    line_num = 1
    for line in input_str.split('\n'):
        io_parts = line.split('|')
        input_list = io_parts[0].strip()
        output_list = io_parts[1].strip()

        key_dict = decode_input(input_list)
        output_num = decode_output(output_list, key_dict)
        total += output_num
        print(f'Line {line_num}: {output_num}')
        line_num += 1
    print(f'Day 8 Part 2: Total = {total}')





if __name__ == '__main__':
    with open('../../resources/2021/inputd8a.txt', 'r') as f:
        test_string = f.read()
        part1(test_string)
        part2(test_string)

    with open('../../resources/2021/inputd8.txt', 'r') as f:
        test_input = f.read()
        part1(test_input)
        part2(test_input)