__author__ = 'trunghieu11'


def tasksTypes(deadline, day):
    deadline = sorted(deadline)
    answer = [0 for i in range(3)]
    for x in deadline:
        if x <= day:
            answer[0] += 1
        elif day + 7 >= x:
            answer[1] += 1
        else:
            answer[2] += 1
    return answer


if __name__ == '__main__':
    deadline = [1, 2, 4, 2, 10, 3, 1, 4, 5, 4, 9, 8]
    day = 1
    print tasksTypes(deadline, day)