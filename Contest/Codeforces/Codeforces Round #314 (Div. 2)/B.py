__author__ = 'trunghieu11'

def main():
    n = int(raw_input())
    room = set()
    maxVal = 0
    for i in range(n):
        line = raw_input().split()
        sign = line[0][0]
        person = int(line[1])
        if sign == '+':
            room.add(person)
            maxVal = max(maxVal, len(room))
        else:
            if person in room:
                room.remove(person)
            else:
                maxVal += 1
    print maxVal

if __name__ == '__main__':
    main()