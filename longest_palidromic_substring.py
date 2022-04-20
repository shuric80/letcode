import pytest


def longest_palindrome(s: str) -> str:
    if s is "":
        return ""
    rev = s[::-1]
    dp = [[0 for i in range(len(s))] for j in range(len(s))]
    max_len = 0
    max_end = 0
    for i, a in enumerate(s):
        for j, b in enumerate(rev):
            if a == b:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j - 1] + 1
            if dp[i][j] > max_len:
                if i - dp[i][j] + 1 == len(s) - 1 - j:
                    max_len = dp[i][j]
                    max_end = i
    return s[max_end - max_len + 1:max_end + 1]


@pytest.mark.parametrize("a, b", (("babad", "bab"), ))
def test_longest_palindromic_substring(a: str, b: str):
    assert longest_palindrome(a) == b
