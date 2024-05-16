import pytest
def longestCommonPrefix(strs: List[str]) -> str:
    s = min(strs, key=len)
    res = ""
    for i in range(len(s)):
        for item in strs:
            if item[i] == s[i]:
                continue
            else:
                return res
        res += item[i]
    return res


@pytest.mark.parametrize("strs,expected_result", [
    (["123", "456"], ""),
    (["123", "1258"], "12"),
    (["abcdedf", "abcd"], "abcd")
])
def test_longest_prefix(strs, expected_result):
    assert longestCommonPrefix(strs) == expected_result
