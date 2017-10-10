cache = dict()

def findPercent(word, glossary):
    if word in cache:
        return cache[word]

    answer = 0

    for i in range(1, len(word) + 1):
        sub = word[:i]
        if sub in glossary:
            answer = max(answer, len(sub) + findPercent(word[i:], glossary))
        else:
            answer = max(answer, findPercent(word[i:], glossary))

    cache[word] = answer
    return answer


if __name__ == '__main__':
    word = "catdogcatdogcatogcatdogcatdogcatdogcatdogcatdog"
    glossary = ["dog", "frog", "cat", "c"]

    print findPercent(word, glossary) * 100.0 / len(word)