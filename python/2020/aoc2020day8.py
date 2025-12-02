class BootCommand:
    _str_command = None
    _int_amount = 0

    def __init__(self, command: str, amount: int):
        self._str_command = command
        self._int_amount = amount

    @property
    def command(self):
        return self._str_command

    @property
    def amount(self):
        return self._int_amount


class BootStatement(BootCommand):
    _int_index = 0
    _int_call_count = 0

    def __init__(self, command: str, amount: int, index: int):
        super().__init__(command, amount)
        self._int_index = index

    @property
    def index(self):
        return self._int_index

    @property
    def call_count(self):
        return self._int_call_count

    @property
    def command(self):
        return self._str_command

    @property
    def amount(self):
        return self._int_amount

    def increment_count(self):
        self._int_call_count += 1

    def flip(self):
        self._int_call_count = 0
        if self._str_command == 'nop':
            self._str_command = 'jmp'
        elif self._str_command == 'jmp':
            self._str_command = 'nop'

    def __str__(self):
        return 'command: {} amount: {} index: {} callcount:{}'.format(self._str_command, self._int_amount, self._int_index, self._int_call_count)


class HandHeld:
    _dict_boot_sequence = None
    _list_steps_taken = None

    def __init__(self, boot_sequence: str):
        self._dict_boot_sequence = {}
        self._list_steps_taken = []
        self._load_boot_sequence(boot_sequence)

    def _load_boot_sequence(self, boot_sequence: str):
        i = 0
        for line in boot_sequence.split('\n'):
            self._decode(line, i)
            i += 1

    def _decode(self, line: str, index: int):
        import re
        pattern = r"^([a-zA-Z]{3}) (\+?-?[\d]+)$"
        regex = re.compile(pattern)
        matches = regex.match(line)
        if matches:
            g = 0
            command = ''
            amount = 0
            for group in matches.groups():
                if g == 0:
                    command = group
                elif g == 1:
                    amount = int(group)
                else:
                    raise ValueError
                g += 1
            stmt = BootStatement(command, amount, index)
            self._dict_boot_sequence.update({index: stmt})

    def step1(self):
        complete, accumulator = run(0, self._dict_boot_sequence, self._list_steps_taken, 0)

        print('Boot Sequence {}. Accumulator Value: {}'.format('completed' if complete is True else 'not completed', accumulator))

    def step2(self):
        complete, accumulator = run(0, self._dict_boot_sequence, self._list_steps_taken, 0)

        if complete is False:
            num_steps = 1
            done_now = False
            while done_now is False:
                this_accumulator = accumulator
                copy_steps_taken = self._list_steps_taken
                copy_boot_sequence = self._dict_boot_sequence

                index, copy_steps_taken, copy_boot_sequence, this_accumulator = backup(num_steps, this_accumulator, copy_steps_taken, copy_boot_sequence)
                done_now, this_accumulator = run(index, copy_boot_sequence, copy_steps_taken, this_accumulator)
                num_steps += 1
                if done_now is True:
                    accumulator = this_accumulator
        print('Boot Sequence complete. Accumulator Value: {}'.format(accumulator))

    def display(self):
        for index in self._dict_boot_sequence:
            print('{}: {}'.format(index, self._dict_boot_sequence.get(index)))


def backup(num_steps: int,
           accumulator: int,
           steps_taken: list,
           sequence: dict):
    copy_steps_taken = steps_taken.copy()
    copy_boot_sequence = sequence.copy()

    i = 1
    last_index = 0
    while i <= num_steps:
        this_step = copy_steps_taken.pop()
        last_index = this_step.index
        seq_step = copy_boot_sequence.get(this_step.index)
        seq_step.flip()
        copy_boot_sequence.update({this_step.index: seq_step})

        if can_flip(this_step.command) is False:
            accumulator -= this_step.amount
        i += 1
    return last_index, copy_steps_taken, copy_boot_sequence, accumulator


def execute(index: int,
            sequence: dict,
            steps_taken: list,
            accumulator: int):
    stmt = sequence.get(index)
    if stmt.call_count > 0:
        return index, False, accumulator

    steps_taken.append(stmt)
    if stmt.command == 'nop':
        index += 1
        stmt.increment_count()
    elif stmt.command == 'acc':
        index += 1
        accumulator += stmt.amount
        stmt.increment_count()
    elif stmt.command == 'jmp':
        index += stmt.amount
        stmt.increment_count()
    else:
        raise ValueError
    return index, True, accumulator


def run(index: int,
        sequence: dict,
        steps_taken: list,
        accumulator: int):
    go = True
    complete = False
    while go is True:
        index, go, accumulator = execute(index, sequence, steps_taken, accumulator)
        if index == len(sequence):
            complete = True
            break

    # print('Steps Taken:')
    # i = 1
    # for s in steps_taken:
    #     print('{}: {}'.format(i, s.__str__()))
    #     i += 1
    return complete, accumulator


def can_flip(command: str):
    return (command == 'nop') or (command == 'jmp')


if __name__ == '__main__':
    with open('inputd8.txt', 'r') as f:
        test_input = f.read()
    handheld = HandHeld(test_input)
    handheld.step1()

    handheld2 = HandHeld(test_input)
    handheld2.step2()

