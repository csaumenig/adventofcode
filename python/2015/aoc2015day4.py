from hashlib import md5


def part1(key: str) -> None:
    found = False
    my_num = 0
    while found is False:
        my_num += 1
        this_str = (key + str(my_num)).encode('utf-8')
        found = md5(this_str).hexdigest().startswith('00000')
    print(f'Day 4 Part 1: Key = {key}, Num = {my_num}')


def part2(key: str) -> None:
    found = False
    my_num = 0
    while found is False:
        my_num += 1
        this_str = (key + str(my_num)).encode('utf-8')
        found = md5(this_str).hexdigest().startswith('000000')
    print(f'Day 4 Part 1: Key = {key}, Num = {my_num}')


if __name__ == '__main__':
    part1('abcdef')
    part1('pqrstuv')
    part1('yzbqklnj')
    part2('yzbqklnj')
