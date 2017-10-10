__author__ = 'trunghieu11'
n = int(input())
mark = {}
allScores = []
for i in range(n):
    name = input()
    scores = float(input())
    if scores not in mark.keys():
        mark.setdefault(scores, [])
    mark[scores].append(name)
    allScores.append(scores)
allScores = list(set(allScores))
allScores.sort()
for name in sorted(mark[allScores[1]]):
    print(name)