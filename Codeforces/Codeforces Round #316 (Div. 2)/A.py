__author__ = 'trunghieu11'

def main():
    m, n = map(int, raw_input().split())
    voted = [0] * m
    for i in range(n):
        curVote = map(int, raw_input().split())
        maxVote = max(curVote)
        for j in range(m):
            if curVote[j] == maxVote:
                voted[j] += 1
                break
    maxVote = max(voted)
    for i in range(len(voted)):
        if maxVote == voted[i]:
            print i + 1
            break

if __name__ == '__main__':
    main()