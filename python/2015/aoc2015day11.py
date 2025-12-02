YEAR = 2015
DAY = 11


def increment_string(password: str) -> str:
    output = ''
    flip = True
    for c in reversed(password):
        if flip:
            if c == 'z':
                output += 'a'
            else:
                output += chr(ord(c) + 1)
                flip = False
        else:
            output += c
    return output[::-1]


def test_rules(password: str) -> bool:
    import re
    if re.match(r'^[a-z]{8}$', password) is None:
        if len(password) != 8:
            # print(f'Password must be 8 lowercase characters, {password} is {len(password)} characters.')
            return False
        # print(f'Password must contain only lowercase characters, {password} has other stuff.')
        return False

    # Test for a sequence of 3 straight
    index = 0
    valid = False
    while (index + 3) < (len(password) + 1):
        this_run = password[index: index+3]
        if (ord(this_run[-1:]) == (ord(this_run[-2:-1]) + 1)) and (ord(this_run[-2:-1]) == (ord(this_run[-3:-2]) + 1)):
            valid = True
            break
        index += 1
    if valid is False:
        # print(f'Password must contain at least one increasing straight of at least three letters, ie. abc or efg')
        return False

    if 'i' in password or 'l' in password or 'o' in password:
        # print(f'Password may not contain i, l, or o.')
        return False

    pairs = 0
    pair_found = False
    last_char = password[0: 1]
    valid = False
    for i in range(1, len(password)):
        this_char = password[i: i + 1]
        if pair_found:
            last_char = this_char
            pair_found = False
            continue
        if last_char == this_char:
            pairs += 1
            pair_found = True
        if pairs == 2:
            valid = True
            break
        last_char = this_char
    if valid is False:
        # print(f'Passwords must contain at least two different, non-overlapping pairs of letters')
        return False
    return True


def part1(file_name: str):
    with open(file_name, 'r') as f:
        lines = f.read()
        for line in lines.split('\n'):
            new_password = increment_string(line)
            while test_rules(new_password) is False:
                new_password = increment_string(new_password)
            print(f'AOC {YEAR} Day {DAY} Part 1: {line} -> {new_password}')


if __name__ == '__main__':
    # part1(f'../../resources/{YEAR}/inputd{DAY}-a.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt')
    part1(f'../../resources/{YEAR}/inputd{DAY}-b.txt')
    # part1(f'../../resources/{YEAR}/inputd{DAY}.txt', 50)
