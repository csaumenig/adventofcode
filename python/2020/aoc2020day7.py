class Bag:
    _name = None
    _children = None
    _parents = None

    def __init__(self, name: str):
        self._name = name
        self._children = list()
        self._parents = list()

    def add_child(self, child: str):
        self._children.append(child)

    def add_parent(self, parent: str):
        self._parents.append(parent)

    def name(self) -> str:
        return self._name

    def children(self) -> list:
        return self._children

    def parents(self) -> list:
        return self._parents

    def has_children(self) -> bool:
        if self._children:
            if len(self._children) > 0:
                return True
        return False


dict_bags = {}


def load(input_str: str):
    for line in input_str.split("\n"):
        x = line.split(' contain ')
        bag_info = x[0].strip()
        children_info = x[1].strip()

        bag_name = ':'.join(bag_info.split(' ')[0:2])
        bag = Bag(bag_name)

        if children_info[0:2] != 'no':
            children = children_info.strip().split(',')
            for child in children:
                child_count = child.strip().split(' ')[0]
                child_name = ':'.join(child.strip().split(' ')[1:3]) + ':' + child_count
                bag.add_child(child_name)
        dict_bags.update({bag_name: bag})

    copy_bags = dict_bags.copy()
    for this_bag_name, this_bag in copy_bags.items():
        for child in this_bag.children():
            this_child_name = ':'.join(child.split(':')[0:2])
            that_bag = dict_bags.get(this_child_name)
            that_bag.add_parent(this_bag_name)
            dict_bags.update({this_child_name: that_bag})
    copy_bags = None


def step_one(search_bag_name: str, input_str=''):
    if len(dict_bags) == 0:
        load(input_str)
    contains = count_ancestors(dict_bags.get(search_bag_name))
    print('Out of {} bags, {} will contain {} bags'.format(len(dict_bags), len(contains), search_bag_name))


def step_two(search_bag_name: str, input_str=''):
    if len(dict_bags) == 0:
        load(input_str)
    contains = count_descendants(dict_bags.get(search_bag_name))
    print('1 {} bag will contain {} total bags'.format(search_bag_name, contains))


def count_ancestors(bag: Bag) -> set:
    contains = set()
    for parent_name in bag.parents():
        contains.add(parent_name)
        contains = contains.union(count_ancestors(dict_bags.get(parent_name)))
    return contains


def count_descendants(bag: Bag) -> int:
    _count = 0
    if bag.has_children():
        for child in bag.children():
            child_count = int(child.split(':')[2])
            _count += child_count
            child_name = ':'.join(child.split(':')[0:2])
            this_child_bag = dict_bags.get(child_name)
            this_child_count = count_descendants(this_child_bag)
            this_child_total = int(child_count * this_child_count)
            _count += this_child_total

    return _count


def combine_dicts(primary, secondary, coefficient):
    for k, v in secondary.items():
        this_count = (v * coefficient) + coefficient
        primary.update({k, primary.get(k) + this_count})
    return primary

if __name__ == '__main__':
    with open('inputd7.txt', 'r') as f:
        test_input = f.read()
    #step_one('shiny:gold', input_str=test_input)
    step_two('shiny:gold', input_str=test_input)
