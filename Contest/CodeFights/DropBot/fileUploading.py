__author__ = 'trunghieu11'


def loadTimeEstimator(sizes, uploadingStart, V):
    files = []
    n = len(sizes)
    for i in range(n):
        files.append([uploadingStart[i], sizes[i]])
    minVal = min(uploadingStart)
    for x in files:
        x[0] -= minVal
    files = sorted(files)
    start = files[0][0]
    answer = files[n - 1][1]
    for i in range(1, n):
        diff = files[i][0] - start
        for l in range(diff):
            k = 0
            for j in range(0, i + 1):
                if files[j][1] > 0:
                    k += 1
            speed = V / k
            for j in range(0, i + 1):
                files[j][1] -= speed
    for l in range(diff):
        k = 0
        for j in range(0, n):
            if files[j][1] > 0:
                k += 1
        speed = V / k
        for j in range(0, n):
            files[j][1] -= speed



if __name__ == '__main__':
    sizes = [21, 10]
    uploadingStart = [100, 105]
    V = 2
    print loadTimeEstimator(sizes, uploadingStart, V)