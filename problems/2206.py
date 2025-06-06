# 03.17.2025
# 2206. Divide Array Into Equal Pairs
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)

        return not s


def test1():
    sol = Solution()
    assert sol.divideArray([1, 1, 2, 2, 3, 3])


def test2():
    sol = Solution()
    assert sol.divideArray([1, 1, 1, 1, 2])


def test3():
    sol = Solution()
    assert sol.divideArray([1, 1, 1, 1])


def main():
    test1()
    test2()
    test3()


if __name__ == '__main__':
    main()
