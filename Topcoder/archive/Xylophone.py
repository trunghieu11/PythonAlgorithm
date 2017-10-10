__author__ = 'trunghieu11'

class Xylophone:
    def countKeys(self, keys):
        dist_key = set()
        for x in keys:
            dist_key.add(x % 7)
        return len(dist_key)