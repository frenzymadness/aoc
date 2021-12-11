from collections import deque

opens = ["(", "[", "{", "<"]
closes = [")", "]", "}", ">"]

scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

final_scores = []

with open("input.txt") as input_file:
    lines = input_file.read().splitlines()

for line in lines:
    queue = deque()
    for char in line:
        if char in opens:
            queue.appendleft(closes[opens.index(char)])
        elif char in closes:
            expected = queue.popleft()
            if char != expected:
                break
    else:
        score = 0
        for char in queue:
            score *= 5
            score += scores[char]
        final_scores.append(score)

middle = sorted(final_scores)[len(final_scores) // 2]

print(middle)
