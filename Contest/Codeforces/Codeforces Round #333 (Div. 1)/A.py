from Queue import Queue

__author__ = 'trunghieu11'


def solve(n, m, graph):
    haveRailRoads = (n - 1) in graph[0]
    queue = Queue()
    queue.put([0, 0])
    visited = {0}
    while not queue.empty():
        top = queue.get()
        if top[0] == n - 1:
            return top[1]
        cur = top[0]
        for x in range(n):
            if x in visited:
                continue
            if haveRailRoads:
                if x not in graph[cur]:
                    queue.put([x, top[1] + 1])
                    visited.add(x)
            else:
                if x in graph[cur]:
                    queue.put([x, top[1] + 1])
                    visited.add(x)
    return -1


if __name__ == '__main__':
    n, m = map(int, raw_input().split(" "))
    graph = [[] for i in range(n)]
    for i in range(m):
        x, y = map(int, raw_input().split(" "))
        x -= 1
        y -= 1
        graph[x].append(y)
        graph[y].append(x)

    print solve(n, m, graph)