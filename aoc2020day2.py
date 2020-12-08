def find_answer_part1(input_str: str):
    input_list = input_str.split('\n')
    valid_count = 0
    for entry in input_list:
        # Each line should be in d1-d2 k: password format where:
        #  d1 and d2 are integers > 0 and represent the minimum and maximum number of times the key needs to appear in
        #   the password
        #  k is a single character (letter?)
        #  password is any length string
        entry_list = entry.split(' ')
        valid_range = entry_list[0].strip()
        key = entry_list[1].replace(':', '').strip()
        password = entry_list[2].strip()

        if validate_password_part1(valid_range, key, password) == 1:
            print('{} is valid'.format(entry))
            valid_count = valid_count + 1
        else:
            print('{} is not valid'.format(entry))
    return valid_count


def validate_password_part1(valid_count: str,
                            key: str,
                            password: str):
    minimum = int(valid_count.split("-")[0])
    maximum = int(valid_count.split("-")[1])
    total = password.count(key)
    if total in range(minimum, maximum + 1):
        return 1
    return 0


def find_answer_part2(input_str: str):
    input_list = input_str.split('\n')
    valid_count = 0
    for entry in input_list:
        # Each line should be in d1-d2 k: password format where:
        #  d1 and d2 are integers > 0 and represent two separate indexes in the password.  Of these two indexes, exactly
        #    one of the characters at that index (starting with 1) needs to match the key
        #  k is a single character (letter?)
        #  password is any length string
        entry_list = entry.split(' ')
        check_indices = entry_list[0].strip()
        key = entry_list[1].replace(':', '').strip()
        password = entry_list[2].strip()

        valid1, valid2 = validate_password_part2(check_indices, key, password)

        if valid1 & (not valid2):
            print('{} is valid'.format(entry))
            valid_count = valid_count + 1
        elif (not valid1) & valid2:
            print('{} is valid'.format(entry))
            valid_count = valid_count + 1
        elif valid1 & valid2:
            print('{} is invalid because both index characters == {}'.format(entry, key))
        else:
            print('{} is invalid because neither index character == {}'.format(entry, key))
    return valid_count


def validate_password_part2(valid_count: str,
                            key: str,
                            password: str):
    index1 = int(valid_count.split("-")[0])
    index2 = int(valid_count.split("-")[1])
    valid1 = False
    valid2 = False

    if password[index1-1:index1] == key:
        valid1 = True

    if password[index2 - 1:index2] == key:
        valid2 = True

    return valid1, valid2


if __name__ == '__main__':
    with open('resources/inputd2.txt', 'r') as f:
        test_input = f.read()

    count = find_answer_part1(test_input)
    print('Part 1: Valid Passwords: {}'.format(count))

    count = find_answer_part2(test_input)
    print('Part 2: Valid Passwords: {}'.format(count))
