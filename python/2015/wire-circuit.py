from __future__ import annotations
from enum import Enum, unique

@unique
class GateType(Enum):
    SOURCE = ''
    BITWISE_AND = 'AND'
    BITWISE_OR = 'OR'
    LEFTSHIFT = 'LSHIFT'
    RIGHTSHIFT = 'RSHIFT'
    NOT = 'NOT'


class Gate:
    def __init__(self,
                 gate_type: GateType,
                 wire1: Optional[Wire],
                 wire2: Optional[Wire],
                 amount: Optional[int]):
        self._type = gate_type
        if wire1 is not None:
            self._wire1 = wire1
        if wire2 is not None:
            self._wire2 = wire2
        if amount is not None:
            self._amount = amount

    def to_str(self) -> str:
        return f'Gate: Type[{self._type}] Wire1[{self._wire1}] Wire2[{self._wire2}] Amount[{self._amount}]'

    @staticmethod
    def build_gate(gate_code: str):
        try:
            a = int(gate_code)
            return Gate(gate_type=GateType.SOURCE,
                        wire1=None,
                        wire2=None,
                        amount=a)
        except:
            pass

        if gate_code.find('AND') > -1:
            w1 = gate_code.split('AND')[0].strip()
            w2 = gate_code.split('AND')[1].strip()
            return Gate(gate_type=GateType.BITWISE_AND,
                        wire1=w1,
                        wire2=w2,
                        amount=None)

        if gate_code.find('OR') > -1:
            w1 = gate_code.split('OR')[0].strip()
            w2 = gate_code.split('OR')[1].strip()
            return Gate(gate_type=GateType.BITWISE_OR,
                        wire1=w1,
                        wire2=w2,
                        amount=None)

        if gate_code.find('LSHIFT') > -1:
            w1 = gate_code.split('LSHIFT')[0].strip()
            a = int(gate_code.split('LSHIFT')[1].strip())
            return Gate(gate_type=GateType.LEFTSHIFT,
                        wire1=w1,
                        wire2=None,
                        amount=a)

        if gate_code.find('NOT') > -1:
            w1 = gate_code.split('NOT')[1].strip()
            return Gate(gate_type=GateType.NOT,
                        wire1=w1,
                        wire2=None,
                        amount=None)



class Wire:
    def __init__(self,
                 name: str) -> None:
        self._name = name
        self._value = 0

    def consume(self, amount: int) -> None:
        self._value = amount


class Circuit:
    def __init__(self,
                 gates: List[Gate],
                 wires: Dict[str, Wire]) -> None:
        self._gates: List[Gate] = gates
        self._wires: Dict[str, Wire] = wires

    def to_str(self) -> str:
        str_rep =  f'Circuit: \n' \
                   f'  Gates: \n' \
                   '    {}'.format("\n    ".join([g.to_str() for g in self._gates]))


    @staticmethod
    def build(input_str: str) -> Circuit:
        wires: Dict[str, Wire] = {}
        gates: List[Gate] = []
        for instruction in input_str.split('\n'):
            gate_code = instruction.split(' -> ')[0].strip()
            wire_name = instruction.split(' -> ')[1].strip()
            gate = Gate.build_gate(gate_code=gate_code)
            wire = Wire(name=wire_name)
            if wires.get(wire_name) is None:
                wires.update({wire_name: wire})
            gates.append(gate)

        return Circuit(gates=gates, wires=wires)


def part1(input_str: str) -> None:
    circuit: Circuit = Circuit.build(input_str=input_str)
    print(circuit.to_str())


def part2(input_str: str) -> None:
    pass


def binary(dec_num: int,
           num_bits: int) -> str:
    return convert_to_base(dec_num, 2).zfill(num_bits)


def convert_to_base(dec_num: int,
                    base: int) -> str:
    return_value = ''
    if dec_num > 1:
        return_value += convert_to_base(dec_num // base, base)
    return_value += str(dec_num % base)
    return return_value


if __name__ == '__main__':
    test_string_1 = '\n'.join(['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g', 'NOT x -> h', 'NOT y -> i'])
    part1(test_string_1)
    # test_string_2 = '\n'.join(['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy'])
    # part2(test_string_2)

    # with open('../../resources/2015/inputd5.txt', 'r') as f:
    #     test_input = f.read()
    # part1(test_input)
    # part2(test_input)
