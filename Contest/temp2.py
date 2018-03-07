known_words = ["KATALON",
               "TESTING",
               "DEVELOPMENT",
               "INTEGRITY",
               "JAVASCRIPT",
               "ARCHITECTURE",
               "INNOVATION"]

total = dict()

for x in ''.join(word for word in known_words):
    total[x] = 0

for x in ''.join(word for word in known_words):
    total[x] += 1

def index_of(letter):
    return ord(letter) - ord('A')

counter = [0 for i in range(26)]
for letter in ''.join(x for x in known_words):
    counter[index_of(letter)] += 1

result = []

for letter in set(list(''.join(x for x in known_words))):
    result.append((letter, counter[index_of(letter)]))

result.sort(key=lambda x:x[1], reverse=True)

print(result)