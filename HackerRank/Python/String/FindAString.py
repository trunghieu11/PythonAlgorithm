__author__ = 'trunghieu11'
s = input()
sub = input()
answer = 0
for i in range(len(s)):
    if s[i:].find(sub) == 0:
        answer += 1
print(answer)