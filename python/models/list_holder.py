from abc import ABC, abstractmethod

class ListHolder(ABC):
    def __init__(self,
                 my_list: str,
                 t: type) -> None:
        self._items = list(map(t, my_list.split(',')))

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.__key__() == other.__key__()
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.__key__())

    def __repr__(self) -> str:
        return f"{self.__class__}({self.__hash__()}) [Items = [{', '.join([str(i) for i in self._items])}]"

    def __str__(self) -> str:
        return self.__repr__()

    def __key__(self) -> tuple[list[int]]:
        return (self._items,)

    @property
    def items(self) -> list[type]:
        return self._items
