
import os
from typing import Tuple, List


def _is_int_token(tok: str) -> bool:
    if tok == "":
        return False
    if tok[0] == "-":
        return len(tok) > 1 and tok[1:].isdigit()
    return tok.isdigit()


def _parse_int_token(tok: str) -> int:
    if not _is_int_token(tok):
        raise ValueError(f"not an integer token: {tok!r}")
    return int(tok)


def _split_lines_strict(output_text: str) -> List[str]:
    """
    Strict output parsing:
    - Accept LF or CRLF newlines (normalize CRLF to LF).
    - Allow at most one trailing newline at EOF.
    - Disallow any other extra blank lines (i.e., empty lines among the t lines).
    - Disallow any stray '\\r' (bare CR) characters.
    """
    # Normalize CRLF to LF for robustness; reject remaining CR.
    text = output_text.replace("\r\n", "\n")
    if "\r" in text:
        raise ValueError("carriage return (\\r) is not allowed (use LF or CRLF newlines)")

    if text.endswith("\n"):
        # Allow exactly one trailing newline; disallow multiple trailing newlines.
        if text.endswith("\n\n"):
            raise ValueError("multiple trailing newlines are not allowed")
        body = text[:-1]
    else:
        body = text

    return body.split("\n") if body != "" else []


def check(input_text: str, output_text: str) -> Tuple[bool, str]:
    # ---- Parse input ----
    try:
        in_tokens = input_text.split()
        if not in_tokens:
            return False, "Input is empty"
        if not _is_int_token(in_tokens[0]):
            return False, f"Input: t is not a valid integer token: {in_tokens[0]!r}"
        t = int(in_tokens[0])
        if t < 1:
            return False, f"Input: t must be >= 1, got {t}"
        expected = 1 + 4 * t
        if len(in_tokens) != expected:
            return False, f"Input: expected {expected} tokens (t + 4*t), got {len(in_tokens)}"
        cases = []
        idx = 1
        for case_id in range(1, t + 1):
            # We assume input respects constraints; still ensure tokens are integers.
            toks = in_tokens[idx:idx + 4]
            if len(toks) < 4:
                return False, f"Input: case {case_id} is incomplete"
            for j, tok in enumerate(toks):
                if not _is_int_token(tok):
                    return False, f"Input: case {case_id}, token {j+1} is not an integer: {tok!r}"
            n, c, d, p = map(int, toks)
            idx += 4
            cases.append((n, c, d, p))
    except Exception as e:
        return False, f"Input parsing error: {e}"

    # ---- Parse output strictly as t lines, 1 integer each ----
    try:
        lines = _split_lines_strict(output_text)
    except Exception as e:
        return False, f"Output formatting error: {e}"

    if len(lines) != t:
        return False, f"Expected exactly {t} lines of output, got {len(lines)}"

    for i, line in enumerate(lines, start=1):
        if line == "":
            return False, f"Case {i}: empty line; expected one integer"
        if line.strip() != line:
            return False, f"Case {i}: leading/trailing whitespace is not allowed"
        parts = line.split()
        if len(parts) != 1:
            return False, f"Case {i}: expected exactly 1 token on the line, got {len(parts)}"
        tok = parts[0]
        if not _is_int_token(tok):
            return False, f"Case {i}: expected an integer, got {tok!r}"
        try:
            ans = _parse_int_token(tok)
        except Exception as e:
            return False, f"Case {i}: integer parsing error: {e}"

        n, c, d, p = cases[i - 1]

        # ---- Validations that do not require solving the optimization problem ----

        # Necessary impossibility: 2A+4B is always even.
        if n % 2 == 1:
            if ans != -1:
                return False, f"Case {i}: n is odd, so output must be -1, got {ans}"
            continue

        m = n // 2  # A + 2B = m

        # Necessary impossibility: K=A+B is in [ceil(m/2), m], so if p > m then no positive multiple of p fits.
        if p > m:
            if ans != -1:
                return False, f"Case {i}: p > n/2 implies impossible; output must be -1, got {ans}"
            continue

        if ans == -1:
            # General impossibility cannot be verified without solving; accept -1 here.
            continue

        K = ans  # K = A+B

        # K must be positive (since n>=1 implies m>=1 for even n, hence K>=ceil(m/2)>=1).
        if K <= 0:
            return False, f"Case {i}: output must be -1 or a positive integer, got {K}"

        # Divisibility constraint.
        if K % p != 0:
            return False, f"Case {i}: (A+B) must be divisible by p={p}, got {K}"

        # Nonnegativity constraints translated into bounds on K.
        K_min = (m + 1) // 2  # ceil(m/2)
        K_max = m
        if not (K_min <= K <= K_max):
            return False, f"Case {i}: output K={K} is out of feasible range [{K_min}..{K_max}]"

        # Recover A,B uniquely from (A+2B=m, A+B=K):
        B = m - K
        A = 2 * K - m

        if A < 0 or B < 0:
            return False, f"Case {i}: derived A={A}, B={B} must be nonnegative"

        # Multiplicity constraints.
        if A % c != 0:
            return False, f"Case {i}: derived A={A} is not a multiple of c={c}"
        if B % d != 0:
            return False, f"Case {i}: derived B={B} is not a multiple of d={d}"

        # Sanity check: ribbons equation.
        if 2 * A + 4 * B != n:
            return False, f"Case {i}: derived A,B do not satisfy 2A+4B=n (got {2*A + 4*B} vs {n})"

    return True, "OK"


if __name__ == "__main__":
    in_path = os.environ.get("INPUT_PATH")
    out_path = os.environ.get("OUTPUT_PATH")
    if not in_path or not out_path:
        raise SystemExit("Environment variables INPUT_PATH and OUTPUT_PATH are required")
    with open(in_path, "r", encoding="utf-8", newline="") as f:
        input_text_ = f.read()
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        output_text_ = f.read()
    ok, _reason = check(input_text_, output_text_)
    print("True" if ok else "False")
