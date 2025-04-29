# 04.29.2025
# 2962. Count Subarrays Where Max Element Appears at Least K Times 

from typing import List


class Solution:
    def count_subarrays(self, nums: List[int], k: int) -> int:
        M = max(nums)
        res, c, r = 0, 0, 0
        for l in range(len(nums)):
            while r < len(nums) and c < k:
                c += nums[r] == M
                r += 1

            res += int(c == k)*(len(nums) - r + 1)
            c -= nums[l] == M
        return res

def test1():
    sol = Solution()
    assert sol.count_subarrays([1,3,2,3,3], 2) == 6


def test2():
    sol = Solution()
    assert sol.count_subarrays([1,4,2,1], 3) == 0


def main():
    test1()
    test2()


if __name__ == '__main__':
    main()
