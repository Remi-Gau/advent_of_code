from rich import print
from utils import load_input


input_data = load_input()

buffer = []

for i, data in enumerate(input_data[0]):

    if len(buffer) < 4:
        buffer.append(data)
        print(buffer)

    if len(buffer) == 4:

        if len(set(buffer)) == 4:
            print(i)
            break

        buffer.pop(0)
        buffer.append(data)
        print(buffer)
