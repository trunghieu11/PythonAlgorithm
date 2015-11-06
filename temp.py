__author__ = 'trunghieu11'

def main():
    fin = open("/home/nthieu6/Dropbox/WTE R&D Data/GameCategoryInterest/installedGames/installedIOSGames2.csv", "r")
    fout = open("/home/nthieu6/Dropbox/WTE R&D Data/GameCategoryInterest/installedGames/installedIOSGames3.csv", "w")
    table = []
    line = fin.readline().split(",")
    for i in range(1, len(line)):
        line[i] = line[i][4:]
    while len(line) > 1:
        table.append(line)
        line = fin.readline().split(",")
    table[0][0] = 'UID'
    for i in range(len(table[0])):
        fout.writelines(','.join(str(table[j][i].rstrip()) for j in range(len(table))))
        fout.writelines('\n')


if __name__ == '__main__':
    main()