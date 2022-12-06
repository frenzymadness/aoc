from pathlib import Path

here = Path(__file__).parent

with open(here / "input") as input:
    signal = input.read().strip()

for i in range(len(signal)):
    if len(set(signal[i:i+14])) == 14:
        print(i + 1 + 13)
        break
