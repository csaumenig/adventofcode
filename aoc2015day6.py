light_grid = {}


def reset_grid():
    for i in range(0, 1000):
        this_list = []
        for j in range(0, 1000):
            this_list.append('x')
        light_grid.update({i: this_list})


def count_lights():
    count = 0
    for my_list in light_grid.values():
        for my_spot in my_list:
            if my_spot == 'o':
                count += 1
    return count


def step1(input_str: str):
    pattern = r"^(turn on|turn off|toggle) ([\d]{1,3},[\d]{1,3}) through ([\d]{1,3},[\d]{1,3})$"
    import re
    p = re.compile(pattern)
    line_num = 1
    for code_string in input_str.split('\n'):
        m = p.match(code_string)
        if m:
            g = m.groups()
            command = g[0].strip()
            start = g[1].strip().split(',')
            end = g[2].strip().split(',')
            for x in range(int(start[0]), (int(end[0]) + 1)):
                my_list = light_grid.get(x)
                for y in range(int(start[1]), (int(end[1]) + 1)):
                    if command == 'turn on':
                        my_list[y] = 'o'
                    elif command == 'turn off':
                        my_list[y] = 'x'
                    elif command == 'toggle':
                        if my_list[y] == 'x':
                            my_list[y] = 'o'
                        else:
                            my_list[y] = 'x'
                light_grid.update({x: my_list})
        line_num += 1
    print(count_lights())


def step2(input_str: str):
    pattern = r"^(turn on|turn off|toggle) ([\d]{1,3},[\d]{1,3}) through ([\d]{1,3},[\d]{1,3})$"
    import re
    p = re.compile(pattern)
    for code_string in input_str.split('\n'):
        m = p.match(code_string)
        if m:
            g = m.groups()
            command = g[0].strip()
            start = g[1].strip().split(',')
            end = g[2].strip().split(',')
            #print('c: {} s: {} e {}'.format(command, start, end))
            for x in range(int(start[0]), (int(end[0]) + 1)):
                my_list = light_grid.get(x)
                for y in range(int(start[1]), (int(end[1]) + 1)):
                    cur_value = 0 if my_list[y] == 'x' else my_list[y]
                    if command == 'turn on':
                        cur_value += 1
                    elif command == 'turn off':
                        cur_value -= 1
                    elif command == 'toggle':
                        cur_value += 2

                    if cur_value <= 0:
                        cur_value = 'x'
                    my_list[y] = cur_value
                light_grid.update({x: my_list})
    print(count_brightness())


def count_brightness():
    count = 0
    for my_list in light_grid.values():
        for my_spot in my_list:
            if my_spot != 'x':
                count += int(my_spot)
    return count


if __name__ == '__main__':
    with open('resources/inputd6p2015.txt', 'r') as f:
         test_input = f.read()

    # reset_grid()
    # step1(test_input)
    reset_grid()
    step2(test_input)
