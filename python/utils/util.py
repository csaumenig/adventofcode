def bin_to_dec(bin_string) -> int:
    power = 0
    total = 0
    for c in reversed(bin_string):
        total += (2 ** power) * int(c)
        power += 1
    # print(f'{bin_string} = {total}')
    return total


def dec_to_bin(dec_string, spaces) -> str:
    bin_string = bin(int(dec_string))[2:].rjust(spaces, '0')
    # print(f'{dec_string} = {bin_string}')
    return bin_string


if __name__ == '__main__':
    bins = ['100', '010', '00000000001', '101', '000000000001011', '1111', '000000000010110']
    [bin_to_dec(b) for b in bins]
    decs = [4, 2, 1, 5, 11, 15, 22]
    [dec_to_bin(d, d) for d in decs]