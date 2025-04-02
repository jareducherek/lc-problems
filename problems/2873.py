# 04.02.2025
# 2873. Maximum Value of Ordered Triplet I
from typing import List


class Solution:
    def maximum_triplet_value(self, l: List[int]) -> int:
        hi, d, res = 0, 0, 0
        for k in l:
            res = max(res, d * k)
            d = max(d, hi - k)
            hi = max(hi, k)
        return res


def test1():
    sol = Solution()
    assert sol.maximum_triplet_value([12, 6, 1, 2, 7]) == 77


def test2():
    sol = Solution()
    assert sol.maximum_triplet_value([1, 10, 3, 4, 19]) == 133


def test3():
    sol = Solution()
    assert sol.maximum_triplet_value([1, 2, 3]) == 0


if __name__ == '__main__':
    test1()
    test2()
    test3()
