# 03.22.2025
# 2685. Count the Number of Complete Components

from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        complete_components = 0

        for v in range(n):
            if not visited[v]:
                component = []
                q = [v]
                visited[v] = True

                while q:
                    curr = q.pop(0)
                    component.append(curr)

                    for neighbor in graph[curr]:
                        if not visited[neighbor]:
                            q.append(neighbor)
                            visited[neighbor] = True

                is_complete = True
                for node in component:
                    if len(graph[node]) != len(component) - 1:
                        is_complete = False
                        break

                if is_complete:
                    complete_components += 1

        return complete_components


def test1():
    sol = Solution()
    assert sol.countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4]]) == 3


def test2():
    sol = Solution()
    assert sol.countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]) == 1


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
