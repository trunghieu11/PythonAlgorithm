class Team:
    def __init__(self, data):
        info = data.split()
        self.name = info[0]
        self.scores = []
        for sc in info[1:]:
            self.scores.append(float(sc))
        self.rank = [-1 for x in self.scores]

    def update_rank(self, i, value):
        if i >= len(self.rank):
            return
        self.rank[i] = value

    def __str__(self):
        return self.name + " " + str(sum(self.rank)) + " " + str(sum(self.scores))


class ContestScore:
    def sortResults(self, data):
        teams = [Team(d) for d in data]
        total_area = len(teams[0].scores)
        for i in range(total_area):
            teams = sorted(teams, key=lambda x: x.scores[i], reverse=True)
            for j in range(len(teams)):
                if j > 0 and teams[j].scores[i] == teams[j - 1].scores[i]:
                    teams[j].rank[i] = teams[j - 1].rank[i]
                else:
                    teams[j].rank[i] = j + 1

        teams = sorted(teams, key=lambda x:(sum(x.rank), -sum(x.scores), x.name))
        return [str(t) for t in teams]


if __name__ == '__main__':
    solver = ContestScore()
    # print(solver.sortResults(("A 90.7 92.9 87.4", "B 90.5 96.6 88.0", "C 92.2 91.0 95.3")))

 #    print(solver.sortResults(("STANFORD 85.3 90.1 82.6 84.6 96.6 94.5 87.3 90.3",
 # "MIT 95.5 83.9 80.4 85.5 98.7 98.3 96.7 82.7",
 # "PRINCETON 99.2 79.1 87.6 85.1 93.6 96.4 86.0 90.6",
 # "HARVARD 83.6 92.0 85.5 94.3 97.5 91.5 92.5 83.0",
 # "YALE 99.5 92.6 86.2 82.0 96.4 92.6 84.5 78.6",
 # "COLUMBIA 97.2 87.6 81.7 93.7 88.0 86.3 95.9 89.6",
 # "BROWN 92.2 95.8 92.1 81.5 89.5 87.0 95.5 86.4",
 # "PENN 96.3 80.7 81.2 91.6 85.8 92.2 83.9 87.8",
 # "CORNELL 88.0 83.7 85.0 83.8 99.8 92.1 91.0 88.9")))

    # print(solver.sortResults(("A 00.1", "B 05.2", "C 29.0","D 00.0")))

 #    print(solver.sortResults(("AA 90.0 80.0 70.0 60.0 50.0 40.0",
 # "BBB 80.0 70.0 60.0 50.0 40.0 90.0",
 # "EEE 70.0 60.0 50.0 40.0 90.0 80.0",
 # "AAA 60.0 50.0 40.0 90.0 80.0 70.0",
 # "DDD 50.0 40.0 90.0 80.0 70.0 60.0",
 # "CCC 40.0 90.0 80.0 70.0 60.0 50.0")))