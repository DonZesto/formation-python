from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
EX_DIR = ROOT / "exercises"


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_reverse_words():
    mod = load_module(EX_DIR / "exercise_01_reverse_words.py")
    assert mod.reverse_words("hello world") == "world hello"
    assert mod.reverse_words("a b c") == "c b a"
    assert mod.reverse_words(" single ") == "single"


def test_count_vowels():
    mod = load_module(EX_DIR / "exercise_02_count_vowels.py")
    assert mod.count_vowels("hello") == 2
    assert mod.count_vowels("xyz") == 0
    assert mod.count_vowels("AEIOU") == 5


def test_sum_positive_numbers():
    mod = load_module(EX_DIR / "exercise_03_sum_numbers.py")
    assert mod.sum_positive_numbers([1, -2, 3, 0]) == 4
    assert mod.sum_positive_numbers([]) == 0
    assert mod.sum_positive_numbers([-1, -2]) == 0
