class Bag:
    _contains_list = None

    def __init__(self):
        self.descriptor = None
        self.color = None
        self._contains_list = set()

    def init(self, input_str):
        x = input_str.replace('.', '').split(' contain ')
        bag_info = x[0].split(" ")
        descriptor = bag_info[0]
        color = bag_info[1]
        self.descriptor = descriptor
        self.color = color
        print('Creating {} {} bag.'.format(descriptor, color))

        if x[1][0:2] != 'no':
            for y in x[1].split(','):
                z = y.strip().split(' ')
                this_count = int(z[0])
                this_descriptor = z[1]
                this_color = z[2]

                bag = Bag()
                bag.set_descriptor(this_descriptor)
                bag.set_color(this_color)
                self._contains_list.add(bag)

    def easy_set(self, d: str, c: str):
        self.descriptor = d
        self.color = c

    def set_descriptor(self, d: str):
        self.descriptor = d

    def set_color(self, c: str):
        self.color = c

    def equals(self, bag_type: tuple):
        return (self.descriptor == bag_type[0]) & (self.color == bag_type[1])

    def can_hold_bag_type(self, bag_type: tuple) -> bool:
        for x in self._contains_list:
            if x.equals(bag_type):
                return True
            return x.can_hold_bag_type(bag_type)
        return False


def step_one(input_str: str, bag_type: tuple):
    lines = input_str.split("\n")
    count = 0
    my_dict = {}
    for line in lines:
        # print(line)
        x = line.split(' contain ')
        y = x[0].split(' ')
        key = Duplex(y[0], y[1])

        child_list = set()
        if x[1][0:2] != 'no':
            for z in x[1].split(','):
                a = z.strip().split(' ')
                this_count = a[0]
                this_key = Duplex(a[1], a[2])
                child_list.add(this_key)
            child_list = sorted(child_list)
        my_dict.update({key: child_list})

    x = {k: v for k, v in sorted(my_dict.items())}
    for bag in x:
        str_stuff = ', '.join('{}:{}'.format(k.first, k.second) for k in x.get(bag))
        print('{}: {}'.format(bag, str_stuff))# #print('Checking {}'.format(bag))
        # if can_hold(my_dict, my_dict.get(bag), bag_type, [bag[0], bag[1]]):
        #     print('{} can hold {}'.format(bag, bag_type))
        #     count += 1
    #print('Out of {} bag types, only {} bags can hold {} {}'.format(len(my_dict), count, bag_type[0], bag_type[1]))


def can_hold(my_dict: dict, children: set, type: tuple, label: list, index=0):
    if len(children) == 0:
        return False

    if type in children:
        first = True
        str_display = ''
        for x in label:
            if first:
                str_display += x + ':'
                first = False
            else:
                str_display += x + ' -> '
                first = True
        str_display = str_display[0:-4]
        print('****Label: {} Index: {}'.format(str_display, index))
        return True

    for child in children:
        grandchildren = my_dict.get(child)
        label.extend(child)
        return can_hold(my_dict, grandchildren, type, label, index+1)


class Duplex:
    _first = None
    _second = None

    def __init__(self, first, second):
        self._first = first
        self._second = second

    def __lt__(self, other):
        if self.second < other.second:
            return True
        elif self.second == other.second:
            return self.first < other.first
        return False

    def __eq__(self, other):
        if (self.first == other.first) & (self.second == other.second):
            return True
        else:
            return False

    def __hash__(self):
        return hash(repr(self))

    def __str__(self):
        return '(' + self._first + ',' + self._second + ')'

    @property
    def first(self):
        return self._first

    @property
    def second(self):
        return self._second


def is_dict(var: any):
    try:
        items = var.items()
    except (AttributeError, TypeError):
        return False
    return True

if __name__ == '__main__':
    with open('resources/inputd7.txt', 'r') as f:
        test_input = f.read()
    step_one(test_input, ('pale', 'olive'))
    # step_two(test_input)
