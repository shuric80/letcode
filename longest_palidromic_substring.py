import pytest


def longest_palindrome(word: str) -> str:



@pytest.mark.parametrize("word, result", (("babad", "bab"),))
def test_longest_palindromic_substring(word: str, result: str):
    assert longest_palindrome(word) == result
