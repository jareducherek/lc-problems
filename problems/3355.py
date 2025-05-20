# 05.19.2025
# 3355. Zero Array Transformation I 
from typing import List


class Solution:
    def zero_array_transformation(self, l: List[int], q: List[List[int]]) -> int:
        n = len(l)
        cs = [0]*(n+1)
        for a, b in q:
            cs[a] += 1
            cs[b+1] -= 1
        val = 0
        for i in range(n):
            val += cs[i]
            if l[i] - val > 0:
                return False
        return True


def test1():
    sol = Solution()
    assert sol.zero_array_transformation([1, 0, 1], [[0, 2]])


def test2():
    sol = Solution()
    assert not sol.zero_array_transformation([3, 1, 1], [[0, 2], [0, 1]])


def test3():
    sol = Solution()
    assert sol.zero_array_transformation([1, 2, 2, 1], [[0, 3], [1, 2]])



if __name__ == '__main__':
    test1()
    test2()
    test3()
