def step_one(input_str: str):
    count = 0
    for group in input_str.split('\n\n'):
        this_set = set()
        for c in group.strip():
            if c != '\n':
                this_set.add(c)
        count += len(this_set)
    print('Count Step 1: {}'.format(count))


def step_two(input_str: str):
    count = 0
    for group in input_str.split('\n\n'):
        this_dict = {}
        num_people = 0
        for person in group.split('\n'):
            person = person.strip().replace('\n', '')
            for c in person:
                cur = this_dict.get(c, 0) + 1
                this_dict.update({c: cur})
            num_people += 1
        for value in this_dict.values():
            if value == num_people:
                count += 1
    print('Count Step 2: {}'.format(count))


if __name__ == '__main__':
    with open('resources/inputd6.txt', 'r') as f:
         test_input = f.read()
    # step_one(test_input)
    step_two(test_input)
