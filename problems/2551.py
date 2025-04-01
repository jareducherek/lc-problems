# 03.31.2025
# 2551. Put marbles in k bags and return score between max and min.
from typing import List


class Solution:
    def put_marbles(self, l: List[int], k: int) -> int:
        if k < 2 or k > len(l):
            return 0
        l = sorted([l[i] + l[i + 1] for i in range(len(l) - 1)])
        return sum(l[-(k - 1) :]) - sum(l[: (k - 1)])


def test1():
    sol = Solution()
    assert sol.put_marbles([1, 1, 2, 2, 1, 1, 2, 2], k=2) == 2


def test2():
    sol = Solution()
    assert sol.put_marbles([1, 3], k=1) == 0


if __name__ == '__main__':
    test1()
    test2()
