from pathlib import Path

here = Path(__file__).parent

with open(here / "input") as input:
    signal = input.read().strip()

for i in range(len(signal)):
    if len(set(signal[i:i+4])) == 4:
        print(i + 1 + 3)
        break
