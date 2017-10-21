class Node:
    def __init__(self):
        self.next_node = [None for i in range(6)]


class RoboCourier:
    def timeToDeliver(self, path):
        root = self.create_tree(path)
        return root

    def create_tree(self, path):
        root = Node()
        current_node = root
        direction = 0
        for x in path:
            if x == 'L':
                direction = (direction - 1 + 6) % 6
            elif x == 'R':
                direction = (direction + 1) % 6
            else:
                if current_node.next_node[direction] is None:
                    new_node = Node()

                    current_node.next_node[direction] = new_node
                    new_node.next_node[(direction + 3) % 6] = current_node

                    if current_node.next_node[(direction + 1) % 6] is not None:
                        old_node = current_node.next_node[(direction + 1) % 6]
                        old_node.next_node[(direction - 1 + 6) % 6] = new_node
                        new_node.next_node[(direction - 1 + 3) % 6] = old_node

                    if current_node.next_node[(direction - 1 + 6) % 6] is not None:
                        old_node = current_node.next_node[(direction - 1 + 6) % 6]
                        old_node.next_node[(direction + 1) % 6] = new_node
                        new_node.next_node[(direction + 3 + 1) % 6] = old_node

                    current_node = new_node
                else:
                    current_node = current_node.next_node[direction]
        return root


if __name__ == '__main__':
    robo_courier = RoboCourier()
    robo_courier.timeToDeliver("FRRFLLFLLFRRFLF")