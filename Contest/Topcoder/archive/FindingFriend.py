__author__ = 'trunghieu11'

class FindingFriend:
    def find(self, roomSize, place, friendPlace):
        if friendPlace in place:
            return 1

        leaders = [friendPlace]
        for x in place:
            leaders.append(x)

        leaders = sorted(leaders)

        answer = 1
        remain = roomSize - 1
        for i in range(1, len(leaders)):
            remain = remain - (leaders[i] - leaders[i - 1] - 1)
            if remain <= 0:
                answer = 1
            if leaders[i] == friendPlace:
                break
            remain += roomSize - 1
            answer += 1

        return answer



if __name__ == '__main__':
    solver = FindingFriend()
    print solver.find(2, {5,1,2}, 4)