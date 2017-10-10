class LexmaxReplace:
    def get(self, s, t):
        s = list(s)
        used = [False for i in range(len(t))]
        for i in range(len(s)):
            max_idx = -1
            for j in range(len(t)):
                if t[j] > s[i] and not used[j]:
                    s[i] = t[j]
                    max_idx = j
            if max_idx >= 0:
                used[max_idx] = True
        return ''.join(x for x in s)


if __name__ == '__main__':
    solver = LexmaxReplace()
    print solver.get("xldyzmsrrwzwaofkcxwehgvtrsximxgdqrhjthkgfucrjdvwlr", "xfpidmmilhdfzypbguentqcojivertdhshstkcysydgcwuwhlk")