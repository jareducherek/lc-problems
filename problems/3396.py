# 04.07.2025
# 3396.  Minimum Number of Operations to Make Elements in Array Distinct 
from typing import List


class Solution:
    def minimum_operations(self, nums: List[int]) -> int:
        i, j, res = 0, 0, 0
        s = set()
        while j < len(nums):
            while nums[j] in s:
                if i > len(nums) - 4:
                    return res+1
                s.discard(nums[i])
                s.discard(nums[i+1])
                s.discard(nums[i+2])
                i += 3
                res += 1
            if i > j:
                j = i
            print(i, j, res, s)
            s.add(nums[j])
            j += 1
        return res

def test1():
    sol = Solution()
    assert sol.minimum_operations([1, 1, 1, 2, 2, 2]) == 2


def test2():
    sol = Solution()
    assert sol.minimum_operations([1, 2, 3, 4, 5, 7, 7, 7]) == 3


def test3():
    sol = Solution()
    assert sol.minimum_operations([1, 2, 3, 1, 2, 3, 1]) == 2


def main():
    test1()
    test2()
    test3()


if __name__ == '__main__':
    main()
