def bin_to_dec(bin_string) -> None:
    power = 0
    total = 0
    for c in reversed(bin_string):
        total += (2 ** power) * int(c)
        power += 1
    print(f'{bin_string} = {total}')


bins = ['100', '010', '00000000001', '101', '000000000001011', '1111', '000000000010110']


[bin_to_dec(b) for b in bins]
