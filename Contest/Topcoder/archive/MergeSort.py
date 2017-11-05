class MergeSort:
    answer = 0

    def howManyComparisons(self, numbers):
        self.answer = 0
        a = list(numbers)
        self.countCompareMergeSort(a)
        return self.answer

    def countCompareMergeSort(self, a):
        if len(a) <= 1:
            return a

        mid = int(len(a) / 2)
        b = a[:mid]
        c = a[mid:]

        b = self.countCompareMergeSort(b)
        c = self.countCompareMergeSort(c)

        a = []
        i = 0
        j = 0
        while i < len(b) and j < len(c):
            self.answer += 1
            if b[i] < c[j]:
                a.append(b[i])
                i += 1
            elif b[i] > c[j]:
                a.append(c[j])
                j += 1
            else:
                a.append(b[i])
                a.append(c[j])
                i += 1
                j += 1

        while i < len(b):
            a.append(b[i])
            i += 1

        while j < len(c):
            a.append(c[j])
            j += 1

        return a

if __name__ == '__main__':
    solver = MergeSort()
    print(solver.howManyComparisons((36, 26, 33, 14)))