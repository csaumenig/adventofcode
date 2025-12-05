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


def find_sum(n: int,
             total: int,
             jump: int = 1,
             seq=()):
    """
    Find all the possible ways that n numbers can add up to total
    Taken From: https://stackoverflow.com/a/67647716
    """
    if n == 0:
        if total == 0 and jump == 1: yield seq
        return
    for i in range(0, total + 1):
        yield from find_sum(n - 1, total - i, jump if i % jump else 1, seq + (i,))


def nth_string_replace(source: str,
                       old: str,
                       new: str,
                       n: int) -> str:
    """
    Replaces the nth occurrence of old in source with new
    Taken From: https://stackoverflow.com/a/35092436
    """
    find = source.find(old)
    # If find is not -1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != n:
        # find + 1 means we start searching from after the last match
        find = source.find(old, find + 1)
        i += 1
    # If i is equal to n we found nth match so replace
    if i == n:
        return source[:find] + new + source[find + len(old):]
    return source


if __name__ == '__main__':
    bins = ['100', '010', '00000000001', '101', '000000000001011', '1111', '000000000010110']
    [bin_to_dec(b) for b in bins]
    decs = [4, 2, 1, 5, 11, 15, 22]
    [dec_to_bin(d, d) for d in decs]
