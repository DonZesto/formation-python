"""Exercise 03 — Sum numbers from a list

Goal:
- Implement sum_positive_numbers(numbers) that returns the sum of positive numbers only.

How to complete:
- Edit the TODO and run: python week-05\\exercises\\exercise_03_sum_numbers.py
"""

def sum_positive_numbers(numbers):
    # TODO: return the sum of numbers > 0
    raise NotImplementedError("TODO: implement sum_positive_numbers")


def main():
    samples = [
        ([1, -2, 3, 0], 4),
        ([], 0),
        ([-1, -2], 0),
    ]
    for inp, expected in samples:
        try:
            out = sum_positive_numbers(inp)
            assert out == expected, f"got {out}, expected {expected}"
            print(f"PASS: {inp} -> {out}")
        except AssertionError as e:
            print(f"FAIL: {inp} -> {e}")
        except Exception as e:
            print(f"ERROR running sum_positive_numbers on {inp}: {e}")


if __name__ == '__main__':
    main()
