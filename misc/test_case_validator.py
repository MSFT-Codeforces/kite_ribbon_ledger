
import sys
import re

def valid_int_line(line: str) -> bool:
    return re.fullmatch(r"[0-9]+", line) is not None

def valid_4ints_line(line: str) -> bool:
    # Exactly 4 non-negative integer tokens separated by single spaces, no leading/trailing spaces
    return re.fullmatch(r"[0-9]+ [0-9]+ [0-9]+ [0-9]+", line) is not None

def main():
    data = sys.stdin.read()
    if data == "":
        print("False")
        return

    lines = data.splitlines()
    # Reject any empty line (strict line formatting)
    lines = [ln.rstrip("\r") for ln in lines]
    if any(ln == "" for ln in lines):
        print("False")
        return

    if not valid_int_line(lines[0]):
        print("False")
        return

    try:
        t = int(lines[0])
    except:
        print("False")
        return

    if t < 1:
        print("False")
        return

    if len(lines) != t + 1:
        print("False")
        return

    for i in range(1, t + 1):
        ln = lines[i]
        if not valid_4ints_line(ln):
            print("False")
            return
        try:
            n_str, c_str, d_str, p_str = ln.split(" ")
            n = int(n_str)
            c = int(c_str)
            d = int(d_str)
            p = int(p_str)
        except:
            print("False")
            return

        if not (1 <= n <= 10**18):
            print("False")
            return
        if not (1 <= c <= 10**9):
            print("False")
            return
        if not (1 <= d <= 10**9):
            print("False")
            return
        if not (1 <= p <= 10**18):
            print("False")
            return

    print("True")

if __name__ == "__main__":
    main()
