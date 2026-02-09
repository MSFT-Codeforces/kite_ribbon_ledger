
def build_input(cases):
    lines = [str(len(cases))]
    for n, c, d, p in cases:
        lines.append(f"{n} {c} {d} {p}")
    return "\n".join(lines)

inputs = []

# 1) Boundary: minimal n odd -> impossible
inputs.append(build_input([
    (1, 1, 1, 1),
]))

# 2) Boundary: n=2 but carton constraint blocks the only solution (A=1 not multiple of c)
inputs.append(build_input([
    (2, 2, 1, 1),
]))

# 3) Boundary: n=2 with trivial constraints -> only A=1 works
inputs.append(build_input([
    (2, 1, 1, 1),
]))

# 4) Structural: all-QuadTail solution (A=0), with large c irrelevant
inputs.append(build_input([
    (4, 5, 1, 1),
]))

# 5) GCD necessary condition fails: gcd(c,2d) ∤ m
inputs.append(build_input([
    (10, 4, 2, 1),  # m=5, gcd(4,4)=4 does not divide 5
]))

# 6) GCD passes but no nonnegative solution exists (integer solutions exist, but x<0 always)
inputs.append(build_input([
    (8, 6, 4, 1),  # m=4, equation 6x+8y=4 has integer solutions but no x,y>=0
]))

# 7) Feasible to satisfy ribbons/cartons, but p-divisibility makes it impossible
inputs.append(build_input([
    (12, 1, 1, 7),  # m=6, A+B = 6-B in {6,5,4,3}, none divisible by 7
]))

# 8) p > m: impossible since 0 < A+B <= m
inputs.append(build_input([
    (20, 1, 1, 11),  # m=10, no positive multiple of 11 is <=10
]))

# 9) p=1: divisibility removed; test "maximize y" under c,d constraints
inputs.append(build_input([
    (30, 2, 3, 1),  # m=15, A multiple of 2, B multiple of 3
]))

# 10) Off-by-one: y_max fails congruence, y_max-1 works (also checks p constraint)
inputs.append(build_input([
    (20, 3, 2, 4),  # m=10, y_max=2 invalid, y=1 valid
]))

# 11) Off-by-one counterpart: y_max is valid and should be chosen
inputs.append(build_input([
    (20, 1, 2, 3),  # m=10, y_max=2 gives total 6 divisible by 3
]))

# 12) Non-coprime modular constraints (shared factors), still solvable
inputs.append(build_input([
    (40, 4, 2, 6),  # m=20, requires handling congruences with non-coprime moduli
]))

# 13) Unique feasible solution due to tight y bound and carton divisibility
inputs.append(build_input([
    (16, 4, 3, 4),  # m=8, y<=1; only y=0 works; total must be divisible by 4
]))

# 14) Many solutions; need to pick maximum y satisfying parity via p=2
inputs.append(build_input([
    (50, 1, 1, 2),  # m=25, y odd; maximize y (<=12) -> y=11
]))

# 15) Multi-test input (I/O handling) mixing several tricky patterns
inputs.append(build_input([
    (3, 1, 1, 1),    # odd n -> -1
    (4, 2, 2, 2),    # n=4, m=2; constraints likely force A=0,B=1 fails B multiple of 2
    (24, 6, 1, 5),   # tests carton constraint + p constraint interplay
    (18, 3, 3, 1),   # p=1; check feasibility with both multiples
]))

print("Test Cases:")
for i, inp in enumerate(inputs, 1):
    print(f"Input {i}:\n{inp}\n")
