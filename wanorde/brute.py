# WORK IN PROGRESS

import string
from itertools import chain, combinations


def powerset(iterable, size):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(size + 1))


class Brute:
    def __init__(self, names: list[str]):
        self.ps = powerset(string.ascii_lowercase, 1)
        self.ps = ["".join(comb) for comb in self.ps]
        self.original_names = names

        self.gen_candidates()

    def gen_candidates(self):
        for name in self.original_names:
            parts = name.split(".")
            new = [parts[0] + comb + "." + ".".join(parts[1:]) for comb in self.ps]
            for name in new:
                print(name)


names = [...]
brute = Brute(names)
