# 03.19.2025
# 1295. Find Numbers with Even Number of Digits 
from typing import List
import math


class Solution:
    def find_numbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res += ((math.floor(math.log10(num))+1)%2 == 0)
        return res

def test1():
    sol = Solution()
    assert sol.find_numbers([12, 2, 7896, 345]) == 2


def test2():
    sol = Solution()
    assert sol.find_numbers([555, 901, 482, 1771]) == 1


if __name__ == '__main__':
    test1()
    test2()
