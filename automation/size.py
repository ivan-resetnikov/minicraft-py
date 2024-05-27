# Codebase size measuring utility.
# Copyright (c) 2024 Ivan Reshetnikov - All right reserved.

import os


def main() -> None:
    lines_count: int = 0
    file_count: int = 0

    for dirpath, dirnames, filenames in os.walk("./source/"):
        for filename in filenames:
            if not filename[-3:] == ".py": continue

            file_count += 1
            
            filepath: str = os.path.join(dirpath, filename)
            with open(filepath, "r") as f:
                lines_count += len(f.readlines())

    print("+=" + "="*20 + "=+=" + "="*20+ "=+")
    print("| " + "Property".ljust(20) + " | " + "Value".ljust(20) + " |")
    print("+=" + "="*20 + "=+=" + "="*20+ "=+")
    print("| " + "File count: ".ljust(20) + " | " + str(file_count).ljust(20) + " |")
    print("| " + "Line count: ".ljust(20) + " | " + str(lines_count).ljust(20) + " |")
    print("+=" + "="*20 + "=+=" + "="*20 + "=+")


if __name__ == "__main__":
    main()