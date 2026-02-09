
def main():
    inputs = []

    # Input 1: Max n, c=d=1, p=1 (huge feasible space; kills brute force over y)
    inputs.append(
        "1\n"
        "1000000000000000000 1 1 1\n"
    )

    # Input 2: Odd n near 1e18 (must be -1 immediately)
    inputs.append(
        "1\n"
        "999999999999999999 999999937 999999929 999999999999999989\n"
    )

    # Input 3: p > m (m=n/2), impossible due to A+B <= m so no positive multiple of p
    inputs.append(
        "1\n"
        "1000000000000000000 1 1 500000000000000001\n"
    )

    # Input 4: "All TwinTail" corner (B=0 works), large c and large p dividing m
    inputs.append(
        "1\n"
        "1000000000000000000 1000000000 999999937 1000000000000\n"
    )

    # Input 5: "All QuadTail" corner (A=0 works), large d and large p
    inputs.append(
        "1\n"
        "1000000000000000000 999999937 1000000000 1000000000\n"
    )

    # Input 6: n even but m not divisible by gcd(c,2d) (diophantine infeasible)
    inputs.append(
        "1\n"
        "999999999999999998 1000000000 1000000000 999999999999999989\n"
    )

    # Input 7: Non-coprime modular constraint stress (needs gcd-based congruence handling),
    # and chosen so B=0 is NOT allowed by p (forces y>0)
    inputs.append(
        "1\n"
        "999999998000000000 1000000000 1000000000 1000000000000\n"
    )

    # Input 8: Overflow risk in CRT/lcm intermediates (c ~ 1e9, p ~ 1e18, gcd=1)
    inputs.append(
        "1\n"
        "1000000000000000000 999999937 1 999999999999999989\n"
    )

    # Input 9: Off-by-one at y_max: y_max exists but fails parity, y_max-1 is the best
    inputs.append(
        "1\n"
        "999999999999999996 1 1 2\n"
    )

    # Input 10: Multi-test (multi-line) large mixed suite: gcd traps, overflow traps, p>m, etc.
    inputs.append(
        "6\n"
        "999999999999999998 999999937 2 9999999967\n"
        "1000000000000000000 2 999999937 999999999999999989\n"
        "1000000000000000000 1 1 1000000000000000000\n"
        "999999998000000000 999999937 999999929 1000000000000\n"
        "999999999999999998 1 999999937 3\n"
        "999999999999999994 999999937 999999937 999999937\n"
    )

    print("**Test Cases: **")
    for i, s in enumerate(inputs, 1):
        print(f"Input {i}:")
        print(s, end="")
        if not s.endswith("\n"):
            print()
        print()

if __name__ == "__main__":
    main()
