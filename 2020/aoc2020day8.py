class bootcommand:
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


class bootstatement(bootcommand):
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

    def __str__(self):
        return 'command: {} amount: {} index: {} callcount:{}'.format(self._str_command, self._int_amount, self._int_index, self._int_call_count)

class handheld:
    _dict_boot_sequence = None
    _int_accumulator = 0

    def __init__(self, boot_sequence: str):
        self._dict_boot_sequence = {}
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
            stmt = bootstatement(command, amount, index)
            self._dict_boot_sequence.update({index: stmt})

    def boot(self):
        run = True
        complete = False
        index = 0
        while run is True:
            index, run = self._execute(index)
            if index == len(self._dict_boot_sequence):
                complete = True
                break
        print('Boot Sequence {}. Accumulator Value: {}'.format('completed' if complete else 'did not complete', self._int_accumulator))

    def _execute(self, index: int):
        stmt = self._dict_boot_sequence.get(index)
        if stmt.call_count > 0:
            return index, False

        if stmt.command == 'nop':
            index += 1
            stmt.increment_count()
        elif stmt.command == 'acc':
            index += 1
            self._int_accumulator += stmt.amount
            stmt.increment_count()
        elif stmt.command == 'jmp':
            index += stmt.amount
            stmt.increment_count()
        else:
            raise ValueError
        return index, True

    def display(self):
        for index in self._dict_boot_sequence:
            print('{}: {}'.format(index, self._dict_boot_sequence.get(index)))



if __name__ == '__main__':
    with open('../resources/2020/inputd8p1.txt', 'r') as f:
        test_input = f.read()
    handheld = handheld(test_input)
    handheld.boot()

