from __future__ import annotations
from math import prod
from typing import Optional
YEAR = 2021
DAY = 16


class Packet:
    def __init__(self,
                 packet_version: int,
                 packet_type: int) -> None:
        self._packet_version: int = packet_version
        self._packet_type: int = packet_type
        self._length_type_id: str = ''
        self._literal: int = 0
        self._sub_packets: list[Packet] = []
        self._value: int = 0

    @property
    def packet_version(self) -> int:
        return self._packet_version

    @property
    def packet_type(self) -> int:
        return self._packet_type

    @property
    def length_type_id(self) -> str:
        return self._length_type_id

    @property
    def literal(self) -> int:
        return self._literal

    def set_literal(self,
                    literal: int) -> None:
        self._literal = literal

    def set_length_type_id(self,
                           length_type_id: str) -> None:
        self._length_type_id = length_type_id

    def add_sub_packet(self,
                       sub_packet: Packet) -> None:
        self._sub_packets.append(sub_packet)

    @property
    def version_total(self) -> int:
        return self._packet_version + sum([p.version_total for p in self._sub_packets])

    @property
    def value(self) -> int:
        if self._value == 0:
            if self._packet_type == 0:
                self._value = sum([p.value for p in self._sub_packets])
            elif self._packet_type == 1:
                self._value = prod([p.value for p in self._sub_packets])
            elif self._packet_type == 2:
                self._value = min([p.value for p in self._sub_packets])
            elif self._packet_type == 3:
                self._value = max([p.value for p in self._sub_packets])
            elif self._packet_type == 4:
                self._value = self._literal
            elif self._packet_type == 5:
                self._value = 1 if self._sub_packets[0].value > self._sub_packets[1].value else 0
            elif self._packet_type == 6:
                self._value = 1 if self._sub_packets[0].value < self._sub_packets[1].value else 0
            elif self._packet_type == 7:
                self._value = 1 if self._sub_packets[0].value == self._sub_packets[1].value else 0
            else:
                raise ValueError(f'No formula for type: {self._packet_type}')
        return self._value


def part1n2(file_name_str: str) -> None:
    print('***********************')
    print(f'Source File = {file_name_str}')
    hex_str = read_file(file_name_str)
    bits = hex_to_bin(hex_str)
    packet, read_length = read_packet(bits)
    print(f'Day {DAY} Part 1: Total of versions = {packet.version_total}')
    print(f'Day {DAY} Part 2: Total of packets = {packet.value}')
    print('***********************')
    print('')


def read_file(file_name_str: str) -> str:
    hex_string = ''
    with open(file_name_str, 'r') as f:
        hex_string += f.read()
    return hex_string


def read_packet_and_total_version(packet_string: str,
                                  total_version: int) -> tuple[int, str, int]:
    packet_version = bin_to_dec(packet_string[:3])
    packet_type = bin_to_dec(packet_string[3:6])
    total_version += packet_version
    remove_length = 6

    if packet_type == 4:
        literal, remainder, r_l = read_literal_and_total_version(packet_string[6:])
        remove_length += r_l
        return total_version, remainder, remove_length

    packet_length_type_id = packet_string[6:7]
    length_of_sub_packets = 0
    length_of_remaining_sub_packets = 0
    number_of_sub_packets = 0
    number_of_remaining_sub_packets = 0
    sub_length = 0

    if packet_length_type_id == '0':
        length_of_sub_packets = bin_to_dec(packet_string[7:22])
        length_of_remaining_sub_packets = bin_to_dec(packet_string[7:22])
        string_to_consider = packet_string[22:22+length_of_sub_packets]
        remove_length += 16
    else:
        number_of_sub_packets = bin_to_dec(packet_string[7:18])
        number_of_remaining_sub_packets = bin_to_dec(packet_string[7:18])
        string_to_consider = packet_string[18:]
        remove_length += 12

    while len(string_to_consider) > 0 and (length_of_remaining_sub_packets > 0 or number_of_remaining_sub_packets > 0):
        total_version, remainder, r_l = read_packet_and_total_version(string_to_consider, total_version)
        if length_of_remaining_sub_packets > 0:
            packet_length = len(string_to_consider) - len(remainder)
            length_of_remaining_sub_packets -= packet_length
            string_to_consider = remainder
        elif number_of_remaining_sub_packets > 0:
            number_of_remaining_sub_packets -= 1
            sub_length += r_l
            string_to_consider = string_to_consider[r_l:]

    if length_of_sub_packets > 0:
        remove_length += length_of_sub_packets
        packet_string = packet_string[remove_length:]
    elif number_of_sub_packets > 0:
        remove_length += sub_length
        packet_string = packet_string[remove_length:]

    return total_version, packet_string, remove_length


def read_literal_and_total_version(packet_str: str) -> tuple[int, str, int]:
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


def read_packet(packet_string: str) -> tuple[Packet, int]:
    packet_version = bin_to_dec(packet_string[:3])
    packet_type = bin_to_dec(packet_string[3:6])
    read_length = 6

    packet = Packet(packet_version=packet_version, packet_type=packet_type)
    if packet_type == 4:
        literal, literal_length_read = read_literal(packet_string[6:])
        packet.set_literal(literal)
        read_length += literal_length_read
    else:
        packet_length_type_id = packet_string[6:7]
        length_of_sub_packets = 0
        length_of_remaining_sub_packets = 0
        number_of_sub_packets = 0
        number_of_remaining_sub_packets = 0
        sub_length = 0

        if packet_length_type_id == '0':
            length_of_sub_packets = bin_to_dec(packet_string[7:22])
            length_of_remaining_sub_packets = bin_to_dec(packet_string[7:22])
            string_to_consider = packet_string[22:22+length_of_sub_packets]
            read_length += 16
        else:
            number_of_sub_packets = bin_to_dec(packet_string[7:18])
            number_of_remaining_sub_packets = bin_to_dec(packet_string[7:18])
            string_to_consider = packet_string[18:]
            read_length += 12

        while len(string_to_consider) > 0 and \
                (length_of_remaining_sub_packets > 0 or number_of_remaining_sub_packets > 0):
            sub_packet, sub_packet_length_read = read_packet(string_to_consider)
            packet.add_sub_packet(sub_packet)
            if length_of_remaining_sub_packets > 0:
                length_of_remaining_sub_packets -= sub_packet_length_read
                string_to_consider = string_to_consider[sub_packet_length_read:]
            elif number_of_remaining_sub_packets > 0:
                number_of_remaining_sub_packets -= 1
                sub_length += sub_packet_length_read
                string_to_consider = string_to_consider[sub_packet_length_read:]

        if length_of_sub_packets > 0:
            read_length += length_of_sub_packets
        elif number_of_sub_packets > 0:
            read_length += sub_length
    return packet, read_length


def read_literal(packet_str: str) -> tuple[int, int]:
    end_found = False
    literal_str: str = ''
    length_read = 0
    while end_found is False:
        this_group = packet_str[:5]
        packet_str = packet_str[5:]
        group_type = this_group[:1]
        this_group = this_group[1:]
        literal_str += this_group
        length_read += 5
        if group_type == '0':
            end_found = True
    return bin_to_dec(literal_str), length_read


def hex_to_bin(hex_string: str) -> str:
    return_val = ''
    for h in hex_string:
        dec_val = int(h, 16)
        bin_val = ''
        remainder = dec_val
        for i in range(3, -1, -1):
            if remainder // (2 ** i) == 1:
                bin_val += '1'
                remainder -= 2 ** i
            else:
                bin_val += '0'
        return_val += bin_val
    return return_val


def bin_to_dec(bin_string) -> int:
    power = 0
    total = 0
    for c in reversed(bin_string):
        total += (2 ** power) * int(c)
        power += 1
    return total


if __name__ == '__main__':
    # file_name = f'../../resources/{YEAR}/inputd{DAY}a.txt'
    # part1n2(file_name)
    #
    # file_name = f'../../resources/{YEAR}/inputd{DAY}b.txt'
    # part1n2(file_name)
    #
    # file_name = f'../../resources/{YEAR}/inputd{DAY}c.txt'
    # part1n2(file_name)
    #
    # file_name = f'../../resources/{YEAR}/inputd{DAY}d.txt'
    # part1n2(file_name)
    #
    # file_name = f'../../resources/{YEAR}/inputd{DAY}e.txt'
    # part1n2(file_name)
    #
    # file_name = f'../../resources/{YEAR}/inputd{DAY}.txt'
    # part1n2(file_name)

    print(bin_to_dec('111111111'))

