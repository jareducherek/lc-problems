# 04.13.2025
# 1534. Count Good Triplets

from typing import List


class Solution:
    def count_good_triplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        n = len(arr)
        for i in range(n - 2):
            for j in range(i+1, n-1):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j+1, n):
                    if abs(arr[j] - arr[k]) > b:
                        continue
                    if abs(arr[i] - arr[k]) > c:
                        continue
                    res += 1
        return res


def test1():
    sol = Solution()
    assert sol.count_good_triplets(arr=[3,0,1,1,9,7], a=7, b=2, c=3) == 4


def test2():
    sol = Solution()
    assert sol.count_good_triplets(arr=[1, 1, 2, 2, 3], a=0, b=0, c=1) == 0


if __name__ == '__main__':
    test1()
    test2()
