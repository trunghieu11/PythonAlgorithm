def findPath(matrix):
    matrix = matrix[0]
    n = len(matrix)
    m = len(matrix[0])

    queue = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                queue.append([i, j])
                break
        if len(queue) > 0:
            break
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited = [False for i in range(0, n * m + 1)]
    visited[0] = True
    visited[1] = True

    while len(queue) > 0:
        top = queue[0]
        print top[0], top[1]
        queue = queue[1:]
        visited[matrix[top[0]][top[1]]] = True
        for i in range(4):
            nextX = top[0] + dx[i]
            nextY = top[1] + dy[i]
            if 0 <= nextX < n and 0 <= nextY < m and matrix[nextX][nextY] > matrix[top[0]][top[1]]:
                queue.append([nextX, nextY])

    for i in range(1, n * m + 1):
        if not visited[i]:
            return False
    return True

if __name__ == '__main__':
    matrix = [[[2,3],[1,4],[10,5],[7,6],[8,9]]]
    print findPath(matrix)