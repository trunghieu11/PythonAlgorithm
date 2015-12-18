__author__ = 'trunghieu11'

def multiSelection(dimensions, tasks, mouseCoordinates):
    start = mouseCoordinates[0][1]
    end = mouseCoordinates[1][1]

    if start > end:
        start, end = end, start

    x = 0
    answer = []

    n = len(tasks)
    idx = 0

    while idx < n and x + dimensions[1] < start:
        x += dimensions[1] + dimensions[2]
        idx += 1

    while idx < n and x <= end:
        answer.append(tasks[idx])
        x += dimensions[1] + dimensions[2]
        idx += 1

    return answer


if __name__ == '__main__':
    dimensions = [135, 9, 1]
    tasks = ["Task 1", "Task 2", "Task 3", "Very Important Task",
             "Not So Important Task", "Yet Another Task", "The last task"]
    mouseCoordinates = [[132, 42], [35, 13]]

    print multiSelection(dimensions, tasks, mouseCoordinates)