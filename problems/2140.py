# 04.01.2025
# 2140. Most points from a list of (points, brainpower) list
from typing import List


class Solution:
    def most_points(self, l: List[List[int]]) -> int:
        N = len(l)
        res = [0] * (N + 1)
        for i in range(N - 1, -1, -1):
            q, b = l[i]
            if i + b + 1 < N:
                q += res[i + b + 1]
            res[i] = max(res[i + 1], q)
        return res[0]


def test1():
    sol = Solution()
    assert sol.most_points([[3, 2], [4, 3], [4, 4], [2, 5]]) == 5


def test2():
    sol = Solution()
    assert sol.most_points([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 7


if __name__ == "__main__":
    test1()
    test2()
