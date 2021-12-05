from typing import Dict, List, Optional


def part1(input_str: str) -> None:
    wires: Dict[str, int] = {}
    deferred: List[str] = []
    messages: List[str] = []
    line_number = 1
    for line in input_str.split('\n'):
        processed, message = process_line(line, wires)
        if processed is False:
            deferred.append(line)
        else:
            messages.append(message)
        line_number += 1

    while len(deferred) > 0:
        deferred, def_messages = process_deferred(deferred, wires)
        if len(def_messages) > 0:
            messages.extend(def_messages)

    with open("../../output/2015-day7-part1-commandlist.txt", "a") as output_file:
        i = 1
        for msg in messages:
            output_file.write(f'{i}: {msg}\n')
            i += 1
        output_file.close()
    print_wires(wires)


def print_wires(wires: Dict[str, int]) -> None:
    for k, v in wires.items():
        print(f'Wire[{k}]: {v}')


def process_line(line: str,
                 wires: Dict[str, int]) -> tuple[bool, str]:
    source = line.split('->')[0].strip()
    target = line.split('->')[1].strip()
    amount = 0

    if source.find('AND') > -1:
        amount1 = get_amount(source.split('AND')[0].strip(), wires)
        amount2 = get_amount(source.split('AND')[1].strip(), wires)
        if amount1 is None or amount2 is None:
            return False, ''
        else:
            amount = amount1 & amount2
    elif source.find('OR') > -1:
        amount1 = get_amount(source.split('OR')[0].strip(), wires)
        amount2 = get_amount(source.split('OR')[1].strip(), wires)
        if amount1 is None or amount2 is None:
            return False, ''
        else:
            amount = amount1 | amount2
    elif source.find('LSHIFT') > -1:
        amount1 = get_amount(source.split('LSHIFT')[0].strip(), wires)
        amount2 = get_amount(source.split('LSHIFT')[1].strip(), wires)
        if amount1 is None or amount2 is None:
            return False, ''
        else:
            amount = amount1 >> amount2
    elif source.find('RSHIFT') > -1:
        amount1 = get_amount(source.split('RSHIFT')[0].strip(), wires)
        amount2 = int(source.split('RSHIFT')[1].strip())
        if amount1 is None or amount2 is None:
            return False, ''
        else:
            amount = amount1 >> amount2
    elif source.find('NOT') > -1:
        amount1 = get_amount(source.split('NOT')[1].strip(), wires)
        if amount1 is None:
            return False, ''
        else:
            amount = complement(amount1)
    else:
        amount = get_amount(source, wires)
        if amount is None:
            return False, ''
    wires.update({target: amount})
    return True, f'line: {line} updated {target} to {amount}'


def get_amount(var: str,
               wires: Dict[str, int]) -> Optional[int]:
    try:
        return int(var)
    except ValueError:
        pass

    return wires.get(var)


def complement(start: int) -> int:
    bin_string = f'{start:016b}'
    return_str = ''
    for x in bin_string:
        return_str += '0' if x == '1' else '1'
    return int(return_str, 2)


def process_deferred(deferred: List[str],
                     wires: Dict[str, int]) -> tuple[List[str], List[str]]:
    new_deferred: List[str] = []
    messages: List[str] = []
    for command in deferred:
        processed, message = process_line(command, wires)
        if processed is False:
            new_deferred.append(command)
        else:
            messages.append(message)
    if len(new_deferred) == len(deferred):
        for command in new_deferred:
            print(command)
        return [], []
    return new_deferred, messages


if __name__ == '__main__':
    # test_string_1 = '\n'.join(['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f',
    # 'y RSHIFT 2 -> g', 'NOT x -> h', 'NOT y -> i'])
    # part1(test_string_1)
    with open('../../resources/2015/inputd7.txt', 'r') as f:
        test_input = f.read()
        part1(test_input)
        # part2(test_input)
