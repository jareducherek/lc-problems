# 03.30.2025
# 763. Partition Labels
from typing import List


class Solution:
    def partition_labels(self, s: str) -> List[int]:
        lasts = {c: i for i, c in enumerate(s)}

        lens = []
        start, end = 0, 0
        for i in range(len(s)):
            end = max(end, lasts[s[i]])

            if i == end:
                lens.append(end - start + 1)
                start = end + 1

        return lens


def test1():
    sol = Solution()
    assert sol.partition_labels("eccbbbbdec") == [10]


def test2():
    sol = Solution()
    assert sol.partition_labels("ababcbacadefegdehijhklij") == [9, 7, 8]


def test3():
    sol = Solution()
    assert sol.partition_labels("aaaaa") == [5]


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
