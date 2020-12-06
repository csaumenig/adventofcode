class BoardingPass:
    _row_num = 0
    _col_num = 0
    _seat_id = 0
    _size = ()

    def __init__(self, boarding_pass_code: str):
        self._init(boarding_pass_code)
        self._decode(boarding_pass_code)

    def _init(self, boarding_pass_code: str):
        _rows = 0
        _cols = 0
        for c in boarding_pass_code:
            if c == 'F':
                _rows += 1
            elif c == 'B':
                _rows += 1
            elif c == 'R':
                _cols += 1
            elif c == 'L':
                _cols += 1
            else:
                raise ValueError
        self._size = (_rows, _cols)

    def _decode(self, boarding_pass_code: str):
        row_range = (0, (2 ** self._size[0]) - 1)
        self._row_num = self.refine_range(row_range, boarding_pass_code[0:self._size[0]])
        col_range = (0, (2 ** self._size[1]) - 1)
        self._col_num = self.refine_range(col_range, boarding_pass_code[-self._size[1]:])
        self._seat_id = self._row_num * 8 + self._col_num

    def refine_range(self, _range: tuple, boarding_pass_code: str) -> int:
        import math
        midpoint = (_range[0] + _range[1]) / 2

        flag = boarding_pass_code[0]
        boarding_pass_code = boarding_pass_code[1:]

        # Lower half
        if flag == 'F':
            _range = (_range[0], math.floor(midpoint))
        elif flag == 'L':
            _range = (_range[0], math.floor(midpoint))
        elif flag == 'B':
            _range = (math.ceil(midpoint), _range[1])
        elif flag == 'R':
            _range = (math.ceil(midpoint), _range[1])

        if _range[0] < _range[1]:
            return self.refine_range(_range, boarding_pass_code)

        return _range[0]

    def output(self):
        print('Row: {} Col: {} Idx: {}'.format(self._row_num, self._col_num, self._seat_id))

    def seat_id(self) -> int:
        # self.output()
        return self._seat_id


if __name__ == '__main__':
    # code_strings = {
    #     'FBFBBFFRLR': 0,  # 357
    #     'BFFFBBFRRR': 0,  # 567
    #     'FFFBBBFRRR': 0,  # 119
    #     'BBFFBBFRLL': 0,  # 820
    # }
    #
    # for code_string in code_strings:
    #     b_pass = BoardingPass(code_string)
    # code_string    code_strings.update({code_string, b_pass.seat_id()})

    with open('resources/inputd5p1.txt', 'r') as f:
        test_input = f.read()

    code_strings = {}
    for code_string in test_input.split():
        b_pass = BoardingPass(code_string)
        code_strings.update({code_string: b_pass.seat_id()})

    import operator
    max_item = max(code_strings.items(), key=operator.itemgetter(1))
    print('Max Key: {} Max Value: {}'.format(max_item[0], max_item[1]))

    last_seat_id = 0
    x = {k: v for k, v in sorted(code_strings.items(), key=lambda item: item[1])}
    for seat_id in x.values():
        if (seat_id != last_seat_id + 1) & (last_seat_id > 0):
            print('Missing Seat Id: {}'.format(last_seat_id + 1))
            break
        last_seat_id = seat_id


