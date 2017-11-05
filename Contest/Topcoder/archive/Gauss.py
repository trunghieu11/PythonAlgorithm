def calc(x):
    return x * (x + 1) / 2

class Gauss:
    def whichSums(self, target):
        answer = []
        for i in range(320000):
            cur_target = calc(i)
            left = 0
            right = i - 2
            while right - left > 1:
                mid = int((right + left) / 2)
                if cur_target - calc(mid) > target:
                    left = mid
                else:
                    right = mid

            if cur_target - calc(left) == target:
                answer.append(str("[%s,%s]" % (left + 1, i)))
            if cur_target - calc(right) == target:
                answer.append(str("[%s,%s]" % (right + 1, i)))

        sorted(answer)

        return tuple(answer)


if __name__ == '__main__':
    solver = Gauss()
    print(solver.whichSums(55))