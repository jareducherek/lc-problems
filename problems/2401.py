# 03.18.2025
# 2401. Longest Nice Subarray
from typing import List


class Solution:
    def longest_nice_subarray(self, nums: List[int]) -> int:
        l, B, ans = 0, 0, 0
        for r, x in enumerate(nums):
            while l < r and (B & x) != 0:
                B ^= nums[l]
                l += 1
            B |= x
            ans = max(ans, r - l + 1)
        return ans


def test1():
    sol = Solution()
    assert sol.longest_nice_subarray([1, 3, 4]) == 2


def test2():
    sol = Solution()
    assert sol.longest_nice_subarray([1, 1, 1, 1, 2]) == 2


def test3():
    sol = Solution()
    assert sol.longest_nice_subarray([1, 2, 4, 8]) == 4


def main():
    test1()
    test2()
    test3()


if __name__ == '__main__':
    main()
