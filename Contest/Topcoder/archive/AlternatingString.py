__author__ = 'trunghieu11'

class AlternatingString:
    def maxLength(self, s):
        answer = 0
        cur = 1

        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                cur += 1
            else:
                answer = max(answer, cur)
                cur = 1

        return max(answer, cur)