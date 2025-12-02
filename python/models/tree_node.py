from __future__ import annotations

class TreeNode:
    def __init__(self,
                 value: int,
                 total: int,
                 level: int | None = 1) -> None:
        self._value = value
        self._total = total
        self._plus: TreeNode | None = None
        self._concat: TreeNode | None = None
        self._mult: TreeNode | None = None
        self._level = level
        self._num_levels = 1

    def add_level(self,
                  value: int) -> None:
        self._plus = TreeNode(value=value,
                              total=self._total + value,
                              level=self._level + 1)
        self._concat = TreeNode(value=value,
                                total=eval(f'{self._total}{value}'),
                                level=self._level + 1)
        self._mult = TreeNode(value=value,
                              level=self._total * value,
                              total=self._level + 1)
        self._num_levels += 1

    @property
    def leaves(self) -> list[TreeNode]:
        return [self._plus, self._concat, self._mult]