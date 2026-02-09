import sys
import math


def extended_gcd(first: int, second: int) -> tuple:
    """
    Compute gcd and Bézout coefficients using the extended Euclidean algorithm.

    Args:
        first: First integer.
        second: Second integer.

    Returns:
        A tuple (gcd_value, coefficient_first, coefficient_second) such that:
        gcd_value = gcd(first, second)
        coefficient_first * first + coefficient_second * second = gcd_value
    """
    old_remainder, remainder = first, second
    old_first_coef, first_coef = 1, 0
    old_second_coef, second_coef = 0, 1

    while remainder != 0:
        quotient = old_remainder // remainder

        old_remainder, remainder = remainder, old_remainder - quotient * remainder
        old_first_coef, first_coef = first_coef, old_first_coef - quotient * first_coef
        old_second_coef, second_coef = (
            second_coef,
            old_second_coef - quotient * second_coef,
        )

    gcd_value = abs(old_remainder)
    if old_remainder < 0:
        old_first_coef = -old_first_coef
        old_second_coef = -old_second_coef

    return gcd_value, old_first_coef, old_second_coef


def modular_inverse(value: int, modulus: int) -> int:
    """
    Compute the modular inverse of value modulo modulus (assuming coprime).

    Args:
        value: Integer whose inverse is needed.
        modulus: Modulus, must be positive.

    Returns:
        inverse such that (value * inverse) % modulus == 1

    Raises:
        ValueError: If inverse does not exist.
    """
    gcd_value, value_coef, _ = extended_gcd(value, modulus)
    if gcd_value != 1:
        raise ValueError("Modular inverse does not exist.")
    return value_coef % modulus


def solve_linear_congruence(coefficient: int, right_side: int, modulus: int):
    """
    Solve coefficient * unknown ≡ right_side (mod modulus).

    Args:
        coefficient: The coefficient multiplying the unknown.
        right_side: The right-hand side constant.
        modulus: Modulus of the congruence (positive).

    Returns:
        (residue, reduced_modulus) representing:
        unknown ≡ residue (mod reduced_modulus),
        or None if no solution exists.
    """
    if modulus == 1:
        return 0, 1

    coefficient %= modulus
    right_side %= modulus

    gcd_value = math.gcd(coefficient, modulus)
    if right_side % gcd_value != 0:
        return None

    coefficient_reduced = coefficient // gcd_value
    right_side_reduced = right_side // gcd_value
    modulus_reduced = modulus // gcd_value

    if modulus_reduced == 1:
        return 0, 1

    inverse = modular_inverse(coefficient_reduced % modulus_reduced,
                              modulus_reduced)
    residue = (right_side_reduced % modulus_reduced) * inverse
    residue %= modulus_reduced
    return residue, modulus_reduced


def merge_congruences(
    first_residue: int,
    first_modulus: int,
    second_residue: int,
    second_modulus: int,
):
    """
    Merge two congruences using generalized CRT:
    unknown ≡ first_residue (mod first_modulus)
    unknown ≡ second_residue (mod second_modulus)

    Args:
        first_residue: Residue of the first congruence.
        first_modulus: Modulus of the first congruence (positive).
        second_residue: Residue of the second congruence.
        second_modulus: Modulus of the second congruence (positive).

    Returns:
        (merged_residue, merged_modulus) representing:
        unknown ≡ merged_residue (mod merged_modulus),
        or None if inconsistent.
    """
    if first_modulus == 1:
        return second_residue % second_modulus, second_modulus
    if second_modulus == 1:
        return first_residue % first_modulus, first_modulus

    gcd_value = math.gcd(first_modulus, second_modulus)
    residue_difference = second_residue - first_residue
    if residue_difference % gcd_value != 0:
        return None

    first_modulus_reduced = first_modulus // gcd_value
    second_modulus_reduced = second_modulus // gcd_value

    left_coefficient = first_modulus_reduced % second_modulus_reduced
    right_constant = (residue_difference // gcd_value) % second_modulus_reduced

    if second_modulus_reduced == 1:
        multiplier = 0
    else:
        inverse = modular_inverse(left_coefficient, second_modulus_reduced)
        multiplier = (right_constant * inverse) % second_modulus_reduced

    merged_modulus = first_modulus_reduced * second_modulus
    merged_residue = (first_residue + first_modulus * multiplier) % merged_modulus
    return merged_residue, merged_modulus


def minimum_kites(
    n_ribbons: int,
    carton_size: int,
    fleet_size: int,
    parade_modulus: int,
) -> int:
    """
    Compute the minimum number of kites satisfying all constraints.

    Args:
        n_ribbons: Total number of ribbons n.
        carton_size: TwinTail batch size c.
        fleet_size: QuadTail batch size d.
        parade_modulus: Divisibility requirement p for total kites.

    Returns:
        Minimum possible total number of kites, or -1 if impossible.
    """
    if n_ribbons % 2 != 0:
        return -1

    maximum_fleets = n_ribbons // (4 * fleet_size)

    first_solution = solve_linear_congruence(
        4 * fleet_size,
        n_ribbons,
        2 * carton_size,
    )
    if first_solution is None:
        return -1
    first_residue, first_modulus = first_solution

    second_solution = solve_linear_congruence(
        fleet_size,
        n_ribbons // 2,
        parade_modulus,
    )
    if second_solution is None:
        return -1
    second_residue, second_modulus = second_solution

    merged_solution = merge_congruences(
        first_residue,
        first_modulus,
        second_residue,
        second_modulus,
    )
    if merged_solution is None:
        return -1

    merged_residue, merged_modulus = merged_solution
    if merged_residue > maximum_fleets:
        return -1

    step_count = (maximum_fleets - merged_residue) // merged_modulus
    best_fleets = merged_residue + step_count * merged_modulus

    total_kites = n_ribbons // 2 - fleet_size * best_fleets
    return total_kites


def main() -> None:
    """
    Read input, solve all test cases, and print outputs.
    """
    data = sys.stdin.buffer.read().split()
    test_cases = int(data[0])

    outputs: list = []
    token_index = 1
    for _ in range(test_cases):
        n_ribbons = int(data[token_index])
        carton_size = int(data[token_index + 1])
        fleet_size = int(data[token_index + 2])
        parade_modulus = int(data[token_index + 3])
        token_index += 4

        answer = minimum_kites(
            n_ribbons,
            carton_size,
            fleet_size,
            parade_modulus,
        )
        outputs.append(str(answer))

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    main()