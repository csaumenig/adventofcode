def load_file(file_name: str):
    with open(file_name, 'r') as f:
        test_input = f.read()
        return test_input.split("\n")


def part1(file_name: str):
    import re
    instructions = load_file(file_name)
    mask = ''
    memory = {}
    for line in instructions:
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
        elif line.startswith('mem'):
            pattern = r"^mem\[([\d]+)\] = ([\d]+)$"
            regex = re.compile(pattern)
            matches = regex.match(line)
            mem_spot = 0
            mem_amount = 0
            if matches:
                g = 0
                for group in matches.groups():
                    if g == 0:
                        mem_spot = int(group)
                    elif g == 1:
                        mem_amount = int(group)
                    else:
                        raise ValueError
                    g += 1

            mem_storage = convert_int_to_36_digit_binary(mem_amount)
            mem_storage = apply_bitmask(mem_storage, mask)
            memory.update({mem_spot: mem_storage})

    mem_sum = 0
    for key in memory:
        mem_amount = memory.get(key)
        mem_amount = convert_36_digit_binary_to_int(mem_amount)
        mem_sum += mem_amount

    print('Sum of all memory is: {}'.format(mem_sum))


def part2(file_name: str):
    import re
    instructions = load_file(file_name)
    mask = ''
    memory = {}
    for line in instructions:
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
        elif line.startswith('mem'):
            pattern = r"^mem\[([\d]+)\] = ([\d]+)$"
            regex = re.compile(pattern)
            matches = regex.match(line)
            mem_spot = 0
            mem_amount = 0
            if matches:
                g = 0
                for group in matches.groups():
                    if g == 0:
                        mem_spot = int(group)
                    elif g == 1:
                        mem_amount = int(group)
                    else:
                        raise ValueError
                    g += 1

            memory_addresses = generate_memory_address_list(mem_spot, mask)


            mem_storage = apply_bitmask(mem_storage, mask)
            memory.update({mem_spot: mem_storage})

    mem_sum = 0
    for key in memory:
        mem_amount = memory.get(key)
        mem_amount = convert_36_digit_binary_to_int(mem_amount)
        mem_sum += mem_amount

    print('Sum of all memory is: {}'.format(mem_sum))


def convert_int_to_36_digit_binary(number: int) -> list[int()]:
    quotient = number
    bits = []
    finished = False
    while finished is False:
        quotient, remainder = convert_int_to_bit(quotient)
        bits.append(remainder)
        if quotient == 0:
            finished = True

    while len(bits) < 36:
        bits.append(0)
    bits.reverse()
    return bits


def convert_int_to_bit(number: int):
    quotient = number // 2
    remainder = number % 2
    return int(quotient), int(remainder)


def apply_bitmask(bits: list[int()], bitmask: str) -> list[int()]:
    for i in range(0, len(bitmask)):
        if (bitmask[i] == '0') or (bitmask[i] == '1'):
            bits[i] = int(bitmask[i])
    return bits


def convert_36_digit_binary_to_int(bits: list[int()]) -> int:
    number = 0
    bits.reverse()
    for i in range(0, len(bits)):
        number += int(bits[int(i)]) * (2 ** int(i))
    return number


def generate_memory_address_list(mem_spot: int, mask: str) -> list:
    memory_address_list = []

    original = convert_int_to_36_digit_binary(mem_spot)
    converted = apply_bitmask_2(original, mask)


def apply_bitmask2(bits: list[int()], bitmask: str) -> list[int()]:
    for i in range(0, len(bitmask)):
        if (bitmask[i] == '1') or (bitmask[i] == 'X'):
            bits[i] = bitmask[i]
    return bits


part1('inputd14.txt')
