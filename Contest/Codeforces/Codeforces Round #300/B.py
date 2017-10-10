__author__ = 'trunghieu11'


def solve(n):
    answer = []
    while n > 0:
        val = 0
        for c in str(n):
            val *= 10
            if c != '0':
                val += 1
        answer.append(val)
        n -= val
    return '\n'.join([str(len(answer)), ' '.join(str(x) for x in answer)])

if __name__ == '__main__':
    n = int(raw_input())
    print solve(n)