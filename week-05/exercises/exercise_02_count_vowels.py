"""Exercise 02 — Count vowels

Goal:
- Implement count_vowels(s) that returns the number of vowels in s (aeiou, case-insensitive)

How to complete:
- Edit the TODO and run: python week-05\\exercises\\exercise_02_count_vowels.py
"""

def count_vowels(s: str) -> int:
    # TODO: return the number of vowels in s (a,e,i,o,u)
    raise NotImplementedError("TODO: implement count_vowels")


def main():
    samples = [
        ("hello", 2),
        ("xyz", 0),
        ("AEIOU", 5),
    ]
    for inp, expected in samples:
        try:
            out = count_vowels(inp)
            assert out == expected, f"got {out}, expected {expected}"
            print(f"PASS: {inp!r} -> {out}")
        except AssertionError as e:
            print(f"FAIL: {inp!r} -> {e}")
        except Exception as e:
            print(f"ERROR running count_vowels on {inp!r}: {e}")


if __name__ == '__main__':
    main()
