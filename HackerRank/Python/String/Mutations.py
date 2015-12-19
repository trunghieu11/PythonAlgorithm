__author__ = 'trunghieu11'
ls = list(input())
line = input().split()
idx = int(line[0])
ls[idx] = line[1][0]
print(''.join(ls))