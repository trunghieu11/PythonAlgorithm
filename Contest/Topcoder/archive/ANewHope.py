__author__ = 'trunghieu11'

class ANewHope:
    def count(self, firstWeek, lastWeek, D):
        n = len(firstWeek)
        answer = 10**100

        for i in range(n):
            for j in range(n):
                if firstWeek[i] == firstWeek[j]:
                    answer = min(answer, (abs(i - j) + D - 1) / D)

        return answer