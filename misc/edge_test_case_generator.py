
def main():
    inputs = []

    # 1) Odd n -> immediate impossible
    inputs.append("1\n1 1 1 1")

    # 2) Smallest even n, p constraint makes it impossible (A+B=1 not divisible by 2)
    inputs.append("1\n2 1 1 2")

    # 3) n=4, force A=0 via c=3, so only B=1 (all-quad corner)
    inputs.append("1\n4 3 1 1")

    # 4) Force B=0 by making d too large; all-twin must satisfy both c and p
    inputs.append("1\n20 5 6 10")

    # 5) Force A=0 by making c too large to fit; all-quad must satisfy d and p
    inputs.append("1\n40 21 5 10")

    # 6) gcd(c,2d) does NOT divide m -> impossible diophantine
    inputs.append("1\n12 4 2 1")

    # 7) Diophantine solvable, but p constraint eliminates all feasible solutions
    inputs.append("1\n12 2 2 5")

    # 8) Very small y_max (0 or 1) -> unique feasible solution due to p
    inputs.append("1\n10 1 2 3")

    # 9) Stress: huge n, d=1 -> enormous y-range, p=1 (no p restriction)
    inputs.append("1\n1000000000000000000 1 1 1")

    # 10) Stress: large n with large non-coprime mod structure (c=d=1e9, p=2e9)
    inputs.append("1\n1000000000000000000 1000000000 1000000000 2000000000")

    # 11) Overflow-prone intermediates: huge p (>> m), large c; should be -1
    inputs.append("1\n1000000000000000000 1000000000 1 1000000000000000000")

    # 12) p > m => impossible since 0 < A+B <= m and cannot be multiple of p
    inputs.append("1\n100 1 1 51")

    # 13) Off-by-one at y_max: y_max fails carton constraint, y_max-1 works and hits p exactly
    inputs.append("1\n100 4 3 29")

    # 14) Large c,d at max (1e9): maximizing y fails p, next-best y works
    inputs.append("1\n8000000000 1000000000 1000000000 3")

    # 15) Multi-test input to verify parsing + mixed edge behaviors
    inputs.append(
        "5\n"
        "3 1 1 1\n"                    # odd n -> -1
        "2 1 1 2\n"                    # small even, p blocks -> -1
        "4 3 1 1\n"                    # all-quad forced
        "100 4 3 29\n"                 # off-by-one y_max case
        "999999999999999998 2 1 1"     # n even but m odd; c=2 forces A even => impossible
    )

    print("Test Cases: ")
    for i, s in enumerate(inputs, 1):
        print(f"Input {i}:\n{s}\n")


if __name__ == "__main__":
    main()
