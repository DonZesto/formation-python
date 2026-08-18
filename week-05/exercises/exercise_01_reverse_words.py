"""Exercise 01 — Reverse words

Goal:
- Implement reverse_words(s) that returns the words of s in reverse order.

How to complete:
- Open this file in VS Code
- Replace the TODO in reverse_words
- Run: python week-05\\exercises\\exercise_01_reverse_words.py
"""

def reverse_words(s: str) -> str:
    # TODO: Implement this function so that words in the string are reversed.
    # Example: "hello world" -> "world hello"
    raise NotImplementedError("TODO: implement reverse_words")


def main():
    samples = [
        ("hello world", "world hello"),
        ("a b c", "c b a"),
        (" single ", "single"),
    ]
    for inp, expected in samples:
        try:
            out = reverse_words(inp)
            assert out == expected, f"got {out!r}, expected {expected!r}"
            print(f"PASS: {inp!r} -> {out!r}")
        except AssertionError as e:
            print(f"FAIL: {inp!r} -> {e}")
        except Exception as e:
            print(f"ERROR running reverse_words on {inp!r}: {e}")


if __name__ == '__main__':
    main()
