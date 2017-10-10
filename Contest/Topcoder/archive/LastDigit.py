def sum_digit(x):
    answer = 0
    while x > 0:
        answer += x
        x /= 10
    return answer


class LastDigit:
    def findX(self, S):
        left = 1
        right = 10**18
        while right - left > 1:
            mid = (right + left) >> 1
            if sum_digit(mid) < S:
                left = mid
            else:
                right = mid
        if sum_digit(left) == S:
            return left
        if sum_digit(right) == S:
            return right
        return -1