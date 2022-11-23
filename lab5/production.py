# It's better to use a list for the rhs because we want O(1) access of the elements
from typing import List


class Production:
    def __init__(self, lhs: str, rhs: List[str]):
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        return f"""
            {self.lhs} -> {self.rhs}
        """

