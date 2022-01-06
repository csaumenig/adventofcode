from __future__ import annotations
YEAR = 2021
DAY = 16


class Packet:
    def __init__(self,
                 version: int,
                 packet_type: int) -> None:
        self._version = version
        self._packet_type = packet_type
        self._literal = 0
        self._length_type_id = ''
        self._sub_packets: list[Packet] = []

    @property
    def version(self) -> int:
        return self._version

    @property
    def packet_type(self) -> int:
        return self._packet_type

    @property
    def length_type(self) -> int:
        return self._length_type

    def set_literal(self, literal: int) -> None:
        self._literal = literal

    def set_length_type_id(self, length_type_id: str) -> None:
        self._length_type_id = length_type_id

    def add_sub_packet(self, sub_packet: Packet) -> None:
        self._sub_packets.append(sub_packet)

    def version_total(self) -> int:
        return self._version + sum([packet.version for packet in self._sub_packets])


convert_dict = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}


def part1(file_name_str: str) -> None:
    hex_str = read_file(file_name_str)
    print(f'Hex Str = {hex_str}')
    bits = convert(hex_str)
    print(f'Bit Str = {bits}')
    total_version, remainder = read_packet(bits, 0)
    print(f'Day {DAY} Part 1: Total of versions = {total_version}')


def part2(file_name_str: str) -> None:
    grid = read_file(file_name_str)
    print(f'Day {DAY} Part 2: ANSWER')


def read_file(file_name_str: str) -> str:
    hex_string = ''
    with open(file_name_str, 'r') as f:
        hex_string += f.read()
    return hex_string


def read_packet(packet_string: str,
                total_version: int) -> tuple[int, str, int]:
    print(f'packet_string = {packet_string}')
    packet_version = bin_to_dec(packet_string[:3])
    packet_type = bin_to_dec(packet_string[3:6])
    total_version += packet_version
    remove_length = 6

    if packet_type == 4:
        literal, remainder, r_l = read_literal(packet_string[6:])
        return total_version, remainder, remove_length + r_l

    packet_length_type_id = packet_string[6:7]
    length_of_remaining_sub_packets = 0
    number_of_remaining_sub_packets = 0

    if packet_length_type_id == '0':
        length_of_remaining_sub_packets = bin_to_dec(packet_string[7:22])
        string_to_consider = packet_string[22:22 + length_of_remaining_sub_packets]
    else:
        number_of_remaining_sub_packets = bin_to_dec(packet_string[7:18])
        string_to_consider = packet_string[18:]

    while length_of_remaining_sub_packets > 0 or number_of_remaining_sub_packets > 0:
        total_version, remainder, r_l = read_packet(string_to_consider, total_version)
        remove_length += r_l
        if length_of_remaining_sub_packets > 0:
            packet_length = len(string_to_consider) - len(remainder)
            length_of_remaining_sub_packets -= packet_length
            string_to_consider = remainder
        elif number_of_remaining_sub_packets > 0:
            number_of_remaining_sub_packets -= 1
            string_to_consider = string_to_consider[remove_length:]

    return total_version, packet_string, remove_length


def read_literal(packet_str: str) -> tuple[int, str, int]:
    end_found = False
    literal_str: str = ''
    remove_length = 0
    while end_found is False:
        this_group = packet_str[:5]
        packet_str = packet_str[5:]
        group_type = this_group[:1]
        this_group = this_group[1:]
        literal_str += this_group
        remove_length += 5
        if group_type == '0':
            end_found = True
    return bin_to_dec(literal_str), packet_str, remove_length


def convert(hex_string: str) -> str:
    converted = [convert_dict.get(c) for c in hex_string]
    return ''.join(converted)


def bin_to_dec(bin_string) -> int:
    power = 0
    total = 0
    for c in reversed(bin_string):
        total += (2 ** power) * int(c)
        power += 1
    return total


if __name__ == '__main__':
    #file_name = f'../../resources/{YEAR}/inputd{DAY}a.txt'
    #part1(file_name)
    #part2(file_name)
    #file_name = f'../../resources/{YEAR}/inputd{DAY}b.txt'
    #part1(file_name)
    #part2(file_name)
    file_name = f'../../resources/{YEAR}/inputd{DAY}c.txt'
    part1(file_name)
    part2(file_name)
    #
    # file_name = f'../../resources/{YEAR}/inputd{DAY}.txt'
    # part1(file_name)
    # part2(file_name)
    # bins = ['100', '101', '110', '111']
    # for b in bins:
    #     print(f'b: {b} = {bin_to_dec(b)}')
