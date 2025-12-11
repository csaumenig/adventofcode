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


def factors(n):
    """
    For a given integer find all factors
    Taken from: https://stackoverflow.com/a/6800214
    """
    from functools import reduce
    return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))


def reduce_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Given a list of ranges (tuples of the form (low, high) where low and high are integers and low <= high), reduce it
    so that all overlapping ranges are combined
    """
    ranges.sort(key=lambda x: x[0])
    reduced_ranges = [ranges[0]]

    for current_start, current_end in ranges[1:]:
        last_reduced_start, last_reduced_end = reduced_ranges[-1]

        if current_start <= last_reduced_end + 1:
            reduced_ranges[-1] = (last_reduced_start, max(last_reduced_end, current_end))
        else:
            reduced_ranges.append((current_start, current_end))
    return reduced_ranges


# def reduce_ranges2(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
#     """
#     Needs work at the moment
#     Given a list of ranges (tuples of the form (low, high) where low and high are integers and low <= high), reduce it
#     so that all overlapping ranges are combined
#     """
#     from functools import reduce
#     ranges.sort(key=lambda x: x[0])
#
#     reduced_ranges = reduce(lambda x, y: (x[0], max(x[1], y[1])) if y[0] <= x[1] + 1 else (y[0], y[1]), ranges)
#     print(reduced_ranges)
#     return reduced_ranges

def dfs_start_end(edges, paths, visited, start, end, exclude=None, include=None):
    if len(visited) == 0:
        visited.append(start)

    for neighbor in edges.get(start, []):
        if exclude and neighbor in exclude:
            continue
        else:
            visited.append(neighbor)
            if neighbor == end:
                paths.append([x for x in visited])
                visited.pop()
                return paths
            else:
                paths = dfs_start_end(edges, paths, visited, neighbor, end, exclude, include)
                visited.pop()
    if include:
        paths = [p for p in paths if include in p]
    return paths

def count_paths(edges, paths, start, end):
    if start == end:
        return 1

    if start in paths:
        return paths.get(start)

    total = 0
    for neighbor in edges.get(start, []):
        total += count_paths(edges, paths, neighbor, end)

    paths[start] = total
    return total


if __name__ == '__main__':
    bins = ['100', '010', '00000000001', '101', '000000000001011', '1111', '000000000010110']
    print(''.join([f'{b} => {bin_to_dec(b)}\n' for b in bins]))
    decs = [4, 2, 1, 5, 11, 15, 22]
    [dec_to_bin(d, d) for d in decs]
