from pathlib import Path

from rich import print
from utils import load_input


size_limit = 100000

total_space = 70000000
required_space = 30000000

input_data = load_input()


def add_dir(parent_dir: dict, line: str):
    tokens = line.split(" ")
    if tokens[1] not in parent_dir:
        parent_dir[tokens[1]] = {"_size": 0, "_file_list": []}
    return parent_dir


def add_file(parent_dir: dict, line: str):
    tokens = line.split(" ")
    if tokens[1] not in parent_dir["_file_list"]:
        parent_dir["_file_list"].append(tokens[1])
        parent_dir["_size"] += int(tokens[0])
    return parent_dir


def get_cwd(file_system: dict, cwd: Path):
    for dir in cwd.parts[1:]:
        file_system = file_system[dir]
    return file_system


def cd(cwd, line):
    if line.startswith("$ cd /"):
        cwd = Path("/")
    if line.startswith("$ cd .."):
        cwd = cwd.parent
    elif line.startswith("$ cd"):
        cwd = cwd.joinpath(line.split(" ")[2])
    return cwd


def update_size(this_dir):
    """Update the size of this directory and all subdirectories"""
    for key in this_dir:
        if key not in ["_file_list", "_size"]:
            this_dir[key] = update_size(this_dir[key])
            this_dir["_size"] += this_dir[key]["_size"]
    return this_dir


def list_size_dirs_above_threshold(this_dir, threshold, size_list=None):
    if size_list is None:
        size_list = []

    if this_dir["_size"] >= threshold:
        size_list.append(this_dir["_size"])

    print(this_dir["_size"])

    for key in this_dir:
        if key not in ["_file_list", "_size"]:
            size_list = list_size_dirs_above_threshold(
                this_dir[key], threshold, size_list=size_list
            )

    return size_list


def total_small_dirs(this_dir, total=0):
    if this_dir["_size"] < size_limit:
        total += this_dir["_size"]
    for key in this_dir:
        if key not in ["_file_list", "_size"]:
            total = total_small_dirs(this_dir[key], total=total)
    return total


def main():
    cwd = ""

    file_system = {"_size": 0, "_file_list": []}

    for line in input_data:
        if line == "":
            continue

        if line.startswith("$ cd"):
            cwd = cd(cwd, line)

        elif line.startswith("$ ls"):
            pass

        elif line.startswith("dir"):
            this_dir = get_cwd(file_system, cwd)
            this_dir = add_dir(this_dir, line)

        else:
            this_dir = get_cwd(file_system, cwd)
            this_dir = add_file(this_dir, line)

    file_system = update_size(file_system)

    print(file_system)
    print(f"used space: {file_system['_size']}")

    total = total_small_dirs(file_system, total=0)
    print(f"total of all small dirs: {total}")

    free_space = total_space - file_system["_size"]
    space_to_free = required_space - free_space
    print(f"space to free: {space_to_free}")

    size_list = list_size_dirs_above_threshold(file_system, space_to_free)

    print(sorted(size_list, reverse=True))


if __name__ == "__main__":
    main()
