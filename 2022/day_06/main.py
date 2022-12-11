from rich import print
from utils import load_input


marker_length = 14

input_data = load_input()

buffer = []

for i, data in enumerate(input_data[0]):

    if len(buffer) < marker_length:
        buffer.append(data)
        print(buffer)

    if len(buffer) == marker_length:

        if len(set(buffer)) == marker_length:
            print(i)
            break

        buffer.pop(0)
        buffer.append(data)
        print(buffer)
