# 03.19.2025
# 3191. Minimum Operations to Make Binary Array Elements Equal to One I
from typing import List


class Solution:
    def make_elements_equal_one(self, l: List[int]) -> int:
        res = 0
        for i in range(len(l) - 2):
            if l[i]:
                continue
            l[i] = 1
            l[i + 1] = (l[i + 1] + 1) % 2
            l[i + 2] = (l[i + 2] + 1) % 2
            res += 1
        return res if l[-2] and l[-1] else -1


def test1():
    sol = Solution()
    assert sol.make_elements_equal_one([0, 1, 1, 1, 0, 0]) == 3


def test2():
    sol = Solution()
    assert sol.make_elements_equal_one([1, 0, 0, 0]) == 1


def test3():
    sol = Solution()
    assert sol.make_elements_equal_one([0, 0, 0, 0]) == -1


if __name__ == "__main__":
    test1()
    test2()
    test3()
