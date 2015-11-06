__author__ = 'trunghieu11'

def main():
    n, s = map(int, raw_input().split())
    buy = dict()
    sell = dict()
    for i in range(n):
        line = raw_input().split()
        d = str(line[0])
        p = int(line[1])
        q = int(line[2])
        if d == "B":
            if (d, p) in buy.keys():
                buy[(d, p)] += q
            else:
                buy.setdefault((d, p), q)
        else:
            if (d, p) in sell.keys():
                sell[(d, p)] += q
            else:
                sell.setdefault((d, p), q)
    keyBuy = buy.keys()
    keyBuy = sorted(keyBuy, key = lambda tup: tup[1], reverse = True)
    keySell = sell.keys()
    keySell = sorted(keySell, key = lambda tup: tup[1])

    if len(keySell) > 0:
        for i in range(min(s, len(keySell)) - 1, -1, -1):
            print keySell[i][0], keySell[i][1], sell.get(keySell[i])

    if len(keyBuy) > 0:
        for i in range(min(s, len(keyBuy))):
            print keyBuy[i][0], keyBuy[i][1], buy.get(keyBuy[i])

if __name__ == '__main__':
    main()