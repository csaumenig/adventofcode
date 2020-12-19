def load_file(file_name: str):
    with open(file_name, 'r') as f:
        test_input = f.read()
        lines = test_input.split("\n")
        busses = []
        for bus_number in lines[1].split(","):
            if bus_number != 'x':
                busses.append(int(bus_number))
        busses.sort()
    return int(lines[0].strip()), busses


def load_file2(file_name: str) -> list:
    with open(file_name, 'r') as f:
        test_input = f.read()
        lines = test_input.split("\n")
        busses = []
        for bus_number in lines[1].split(","):
            busses.append(bus_number)
    return busses


def load_file2a(file_name: str) -> list:
    with open(file_name, 'r') as f:
        test_input = f.read()
        lines = test_input.split("\n")
        return_list = []
        for line in lines:
            busses = []
            for bus_number in line.split(","):
                busses.append(bus_number)
            return_list.append(busses)
    return return_list


def part1(file_name: str):
    earliest_time, busses = load_file(file_name)
    wait_times = {}
    for bus in busses:
        bus_time = 0
        while bus_time < earliest_time:
            bus_time += int(bus)
        wait_times.update({bus: (bus_time - earliest_time)})

    sorted_busses = sorted(wait_times, key=wait_times.get)
    print('Earliest Bus Time x Wait: {}'.format(int(sorted_busses[0]) * int(wait_times.get(sorted_busses[0]))))


def part2(file_name: str):
    busses = load_file2(file_name)
    complete = False
    cycle = 1
    start = 0
    while complete is False:
        start += int(busses[0])
        complete = True
        for i in range(1, len(busses)):
            this_target = start + i
            this_bus = busses[i]
            if this_bus != 'x':
                if this_target % int(this_bus) != 0:
                    complete = False
                    break
    print('Earliest Timestamp: {}'.format(start))


def part2a(file_name: str):
    for busses in load_file2a(file_name):
        if len(busses) == 1:
            if busses[0] == '':
                return ''
        complete = False
        cycle = 1
        start = 0
        while complete is False:
            start += int(busses[0])
            complete = True
            for i in range(1, len(busses)):
                this_target = start + i
                this_bus = busses[i]
                if this_bus != 'x':
                    if this_target % int(this_bus) != 0:
                        complete = False
                        break
        print('Earliest Timestamp: {}'.format(start))


#part1('../resources/2020/inputd13p1.txt')

#part1('../resources/2020/inputd13.txt')

part2('../resources/2020/inputd13.txt')

#part2a('../resources/2020/inputd13p2.txt')
