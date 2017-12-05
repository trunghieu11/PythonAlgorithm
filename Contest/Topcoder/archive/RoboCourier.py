DX = [0, 1, 1, 0, -1, -1]
DY = [1, 1, 0, -1, -1, 0]


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.near_node = [None for i in range(6)]


class RoboCourier:
    def timeToDeliver(self, paths):
        path = ''.join(p for p in paths)

        if 'F' not in path:
            return 0

        nodes, target = self.create_path(path)
        total_state = 6 * len(nodes)
        distance = [[10**10 for i in range(6)] for j in range(len(nodes))]

        _, target_idx = self.find_node(target.x, target.y, nodes)

        distance[0][0] = 0
        self.update_distance(distance, 0, 0)
        visited = set()

        while True:
            best = 10**10
            choose_node = -1
            choose_direction = -1

            for i in range(total_state):
                cur_idx = int(i / 6)
                direction = i % 6
                if (cur_idx, direction) not in visited and distance[cur_idx][direction] < best:
                    choose_node = cur_idx
                    choose_direction = direction
                    best = distance[cur_idx][direction]

            if choose_node == -1:
                return 0

            if choose_node == target_idx:
                return best

            visited.add((choose_node, choose_direction))

            go_straight = 0
            cur_node = nodes[choose_node]
            while cur_node.near_node[choose_direction]:
                cur_node = cur_node.near_node[choose_direction]
                _, idx = self.find_node(cur_node.x, cur_node.y, nodes)

                go_straight += 1
                distance[idx][choose_direction] = min(distance[idx][choose_direction], best
                                               + (4 * go_straight if go_straight <= 2 else (8 + (go_straight - 2) * 2)))
                self.update_distance(distance, choose_direction, idx)

    def create_path(self, path):
        nodes = []
        target = None
        direction = 0
        x = 0
        y = 0
        for p in path:
            if p == 'L':
                direction = (direction - 1 + 6) % 6
            elif p == 'R':
                direction = (direction + 1) % 6
            else:
                node_from, _ = self.find_node(x, y, nodes)
                x += DX[direction]
                y += DY[direction]
                node_to, _ = self.find_node(x, y, nodes)

                node_from.near_node[direction] = node_to
                node_to.near_node[(direction + 3) % 6] = node_from

                target = node_to

        return nodes, target

    def find_node(self, x, y, nodes):
        for i, node in enumerate(nodes):
            if node.x == x and node.y == y:
                return node, i
        node = Node(x, y)
        nodes.append(node)
        return node, len(nodes) - 1

    def update_distance(self, distance, direction, idx):
        for i in range(6):
            distance[idx][(direction + i) % 6] = min(distance[idx][direction] + 3 * i, distance[idx][(direction + i) % 6])

        for i in range(6):
            distance[idx][(direction - i + 6) % 6] = min(distance[idx][direction] + 3 * i, distance[idx][(direction - i + 6) % 6])


if __name__ == '__main__':
    solver = RoboCourier()
    print(solver.timeToDeliver((
        "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")))