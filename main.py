def findRepeatedDnaSequences(self, s: str) -> list[str]:
    data = set()
    result = set()
    k = 10
    for i in range(0, len(s) - k + 1):
        substring = s[i:i + k]
        if substring in data:
            result.add(substring)
        data.add(substring)
    return list(result)


class FreqStack:
    def __init__(self):
        self.frequency = {}     # key = element, value = frequency
        self.map_stacks = {}    # key = frequency of elements, value = list of elements which given frequency
        self.max_frequency = 0

    def push(self, x):
        if x not in self.frequency:
            self.frequency[x] = 0
        self.frequency[x] += 1

        self.max_frequency = max(self.max_frequency, self.frequency[x])

        if self.frequency[x] not in self.map_stacks.keys():
            self.map_stacks[self.frequency[x]] = []
        self.map_stacks[self.frequency[x]].append(x)

    def pop(self):
        x = self.map_stacks[self.max_frequency].pop()
        if not self.map_stacks[self.max_frequency]:
            self.max_frequency -= 1
        self.frequency[x] -= 1
        return x


if __name__ == '__main__':
    pass

