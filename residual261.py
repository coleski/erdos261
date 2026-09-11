"""Exact residual-state exploration for Erdős problem 261.

Before testing exponent a, r = 2**(a-1) times the remaining sum.  The whole
available tail has scaled sum a+1.  A finite continuation therefore requires
0 <= r < a+1.  Selecting epsilon in {0,1} gives the next state 2*r-a*epsilon.
"""

from fractions import Fraction


def witness(n: int, bound: int, *, all_choices: bool = True) -> tuple[int, ...] | None:
    states: dict[int, tuple[int, ...]] = {n: ()}
    for a in range(n + 1, bound + 1):
        next_states: dict[int, tuple[int, ...]] = {}
        for residual, terms in states.items():
            choices = (0, 1) if all_choices else (int(2 * residual >= a),)
            for digit in choices:
                next_residual = 2 * residual - a * digit
                if 0 <= next_residual < a + 2:
                    next_states[next_residual] = terms + ((a,) if digit else ())

        states = next_states
        if 0 in states:
            terms = states[0]
            assert len(terms) >= 2 and len(set(terms)) == len(terms)
            assert Fraction(n, 2**n) == sum(Fraction(t, 2**t) for t in terms)
            return terms

        assert len(states) <= 2
        assert len(states) < 2 or sum(states) == a + 2

    return None


if __name__ == "__main__":
    for n in (2, 16, 24, 27, 121, 158, 163):
        full = witness(n, 20_000)
        greedy = witness(n, 20_000, all_choices=False)
        print(
            n,
            "full-state endpoint",
            full[-1] if full else None,
            "greedy endpoint",
            greedy[-1] if greedy else None,
        )
        if n == 16:
            print("exact n=16 witness:", full)

