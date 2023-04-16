from typing import List, Tuple

from gameLogic.Attestation import Attestation


class Field:
    DEFAULT_SIZE = 10

    @staticmethod
    def _generate_attestations(size: int):
        return [
            [Attestation.create_random() for c in range(size)]
            for r in range(size)
        ]

    def __init__(self, size=DEFAULT_SIZE):
        self._selected_attestations: List[Tuple] = []
        self.size = size
        self.attestations = Field._generate_attestations(self.size)

    def __getitem__(self, item):
        return self.attestations[item]

    def __len__(self):
        return len(self.attestations)

    def is_select(self, r, c):
        return (r, c) in self._selected_attestations

    @property
    def is_any_selected(self):
        return len(self._selected_attestations) > 0

    def get_index(self, src, delta):
        if 0 <= src + delta < self.size:
            return src + delta
        else:
            return 0 if delta < 0 else self.size - 1

    def in_field(self, r: int, c: int) -> bool:
        return 0 <= r < self.size and 0 <= c < self.size

    def select(self, r: int, c: int) -> bool:
        if not self.in_field(r, c):
            raise IndexError("Выбрана клетка за пределами поля")

        if not self.is_any_selected:
            self._selected_attestations.append((r, c))
            return True

        if (r, c) in self._selected_attestations:
            return False

        gi = self.get_index
        to_check = (
            (gi(r, -1), c),
            (gi(r, 1), c),
            (r, gi(c, -1)),
            (r, gi(c, 1))
        )

        if any(atta_pos in self._selected_attestations for atta_pos in to_check):
            self._selected_attestations.append((r, c))
            return True

        return False

    def unselect(self, r: int, c: int) -> bool:
        if not self.in_field(r, c):
            raise IndexError("Выбрана клетка за пределами поля")

        if (r, c) in self._selected_attestations:
            self._selected_attestations.remove((r, c))
            return True
        return False

    def clear_selected(self):
        for selected in self._selected_attestations:
            r, c, = selected
            self[r][c] = Attestation.create_random()
        self._selected_attestations.clear()

    @property
    def selected_attestations(self):
        return [self[atta_pos[0]][atta_pos[1]] for atta_pos in self._selected_attestations]
