__author__ = 'trunghieu11'


def bfs(first, second, n, graph):
    answer = 0

    queue = []
    queue.append([first, 0])
    queue.append([second, 0])

    processed = []
    processed.append(first)
    processed.append(second)

    while len(queue) > 0:
        top = queue[0]
        answer = max(answer, top[1])
        queue = queue[1:]
        for x in graph[top[0]]:
            if x not in processed:
                processed.append(x)
                queue.append([x, top[1] + 1])

    return answer


def solve(n, graph):
    answer = 10**9

    for i in range(n):
        for j in range(i + 1, n):
            answer = min(answer, bfs(i, j, n, graph))

    return answer


if __name__ == '__main__':
    n = int(raw_input())
    graph = [[] for i in range(n)]
    for i in range(n - 1):
        x, y = map(int, raw_input().split(" "))
        x -= 1
        y -= 1
        graph[x].append(y)
        graph[y].append(x)
    print solve(n, graph)