FILE_NAME = "sv.txt"

def read():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []

def save(line):
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def delete_by_value(value):
    sv = read()
    sv = [x for x in sv if x != value]

    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for line in sv:
            f.write(line + "\n")
