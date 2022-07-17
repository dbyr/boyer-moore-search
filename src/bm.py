from typing import Dict


def make_km_table(pattern: str) -> Dict[str, int]:
    table = dict()
    offset = len(pattern) - 1
    # don't add the last character of the pattern
    # because if the end char matches it won't progress
    for i in range(offset):
        table[pattern[i]] = len(pattern) - i - 1
    return table

class Bm(object):
    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern
        self.table = make_km_table(pattern)

    def decide_slide_width(self, c: str) -> int:
        assert len(c) == 1
        if c in self.table:
            return self.table[c]
        return len(self.pattern)

    def search(self) -> int:
        patlen = len(self.pattern)
        i = patlen - 1
        while i < len(self.text):
            for j in range(patlen):
                if self.text[i - j] != self.pattern[patlen - j - 1]:
                    i += self.decide_slide_width(self.text[i - j])
                    break
            else:
                return i - (patlen - 1)
        return -1
