import re


class Passport:
    _byr = None
    _byr_exists = False
    _byr_valid = False

    _iyr = None
    _iyr_exists = False
    _iyr_valid = False

    _eyr = None
    _eyr_exists = False
    _eyr_valid = False

    _hgt = None
    _hgt_exists = False
    _hgt_valid = False

    _hcl = None
    _hcl_exists = False
    _hcl_valid = False

    _ecl = None
    _ecl_exists = False
    _ecl_valid = False

    _pid = None
    _pid_exists = False
    _pid_valid = False

    _cid = None

    def __init__(self, passport_block: str) -> None:
        self._load(passport_block)

    def _load(self, passport_block: str) -> None:
        if passport_block.rstrip() != '':
            passport_dict = dict([tuple(entry.split(':')) for entry in re.split(r"[\n\r\s]+", passport_block)])
            birth_year = passport_dict.get('byr')
            issue_year = passport_dict.get('iyr')
            expire_year = passport_dict.get('eyr')
            height = passport_dict.get('hgt')
            hair_color = passport_dict.get('hcl')
            eye_color = passport_dict.get('ecl')
            passport_id = passport_dict.get('pid')
            country_id = passport_dict.get('cid')

            if birth_year:
                self._byr_exists = True
                try:
                    self._byr = int(birth_year)
                except ValueError:
                    self._byr = 0

            if issue_year:
                self._iyr_exists = True
                try:
                    self._iyr = int(issue_year)
                except ValueError:
                    self._iyr = 0

            if expire_year:
                self._eyr_exists = True
                try:
                    self._eyr = int(expire_year)
                except ValueError:
                    self._eyr = 0

            if height:
                self._hgt = height
                self._hgt_exists = True

            if hair_color:
                self._hcl_exists = True
                self._hcl = hair_color

            if eye_color:
                self._ecl_exists = True
                self._ecl = eye_color

            if passport_id:
                self._pid_exists = True
                self._pid = passport_id

            self._cid = country_id

    def _validate_keys_exist(self) -> bool:
        return self._byr_exists & self._iyr_exists & self._eyr_exists & self._hgt_exists & self._hcl_exists & self._ecl_exists & self._pid_exists

    def _validate_rules(self) -> bool:
        if self._byr in range(1920, 2003):
            self._byr_valid = True

        if self._iyr in range(2010, 2021):
            self._iyr_valid = True

        if self._eyr in range(2020, 2031):
            self._eyr_valid = True

        regex = re.compile(r"^[\d]{2,3}(cm|in)$")
        m = regex.match(self._hgt)
        if m:
            if m.group(1) == 'cm':
                if int(self._hgt.split('c')[0]) in range(150, 194):
                    self._hgt_valid = True
            else:
                if int(self._hgt.split('i')[0]) in range(59, 77):
                    self._hgt_valid = True

        if re.match(r"^#[0-9a-f]{6}$", self._hcl) is not None:
            self._hcl_valid = True

        if re.match(r"^(amb|blu|brn|grn|gry|hzl|oth)$", self._ecl) is not None:
            self._ecl_valid = True

        if re.match(r"^[\d]{9}$", self._pid) is not None:
            self._pid_valid = True

        return self._byr_valid & self._iyr_valid & self._eyr_valid & self._hgt_valid & self._hcl_valid & self._ecl_valid & self._pid_valid

    @property
    def byr(self) -> int:
        return self._byr

    @property
    def iyr(self) -> int:
        return self._iyr

    @property
    def eyr(self) -> int:
        return self._eyr

    @property
    def hgt(self) -> int:
        return self._hgt

    @property
    def hcl(self) -> str:
        return self._hcl

    @property
    def ecl(self) -> str:
        return self._ecl

    @property
    def pid(self) -> str:
        return self._pid

    @property
    def cid(self) -> str:
        return self._cid

    @property
    def to_string(self):
        return 'byr:{} iyr:{} eyr:{} hgt:{} hcl:{} ecl:{} pid:{} cid:{}'.format(self._byr, self._iyr, self._eyr, self._hgt, self._hcl, self._ecl, self._pid, self._cid)

    def validate(self, apply_rules=False) -> bool:
        if self._validate_keys_exist():
            if apply_rules:
                return self._validate_rules()
            else:
                return True
        return False


def read_passports(input_str: str):
    return list(Passport(entry) for entry in input_str.split('\n\n'))


def valid_passports(passport_list: list,
                    apply_rules: bool):
    valid_list = []
    invalid_list = []
    for passport in passport_list:
        if passport.validate(apply_rules):
            valid_list.append(passport)
        else:
            invalid_list.append(passport)
    return valid_list


def write_passport_file(passport_list: list, file_name) -> None:
    from os import path
    if path.exists(file_name) is False:
        with open(file_name, 'w') as f:
            for passport in passport_list:
                f.write(passport.to_string)
                f.write('\n\n')


if __name__ == '__main__':
    with open('resources/inputd4p1.txt', 'r') as f:
        test_input = f.read()

    passports = read_passports(test_input)
    valid_passports_step1 = valid_passports(passports, False)
    print('Part1: ')
    print('Valid Passports: {}'.format(len(valid_passports_step1)))
    print('')
    print('')
    valid_passports_step2 = valid_passports(valid_passports_step1, True)
    print('Part2: ')
    print('Valid Passports: {}'.format(len(valid_passports_step2)))
    print('')
    print('')

