# 04.16.2025
# 2537. Count the number of good subarrays

from typing import List
from collections import defaultdict


class Solution:
    def count_good_subarrays(self, arr: List[int], k: int) -> int:
        res, l, cur_k = 0, 0, 0
        N = len(arr)
        d = defaultdict(int)
        for r in range(N):
            cur_k += d[arr[r]]
            d[arr[r]] += 1

            while cur_k >= k:
                res += N - r
                d[arr[l]] -= 1
                cur_k -= d[arr[l]]
                l += 1

        return res


def test1():
    sol = Solution()
    assert sol.count_good_subarrays(arr=[1,1,1,1,1], k=10) == 1


def test2():
    sol = Solution()
    assert sol.count_good_subarrays(arr=[3,1,4,3,2,2,4], k=2) == 4


if __name__ == '__main__':
    test1()
    test2()
