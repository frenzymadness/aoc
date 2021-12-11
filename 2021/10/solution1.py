from collections import deque

opens = ["(", "[", "{", "<"]
closes = [")", "]", "}", ">"]

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

with open("input.txt") as input_file:
    lines = input_file.read().splitlines()

queue = deque()
final_score = 0

for line in lines:
    for char in line:
        if char in opens:
            queue.appendleft(closes[opens.index(char)])
        elif char in closes:
            expected = queue.popleft()
            if char != expected:
                final_score += scores[char]
                break

print(final_score)
