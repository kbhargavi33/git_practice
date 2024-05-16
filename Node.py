from typing import List

import pytest

def f(l:List[int]) -> int:
    return len(l)

@pytest.mark.parametrize("l, expected_result", [
    ([1,2,3,4,5], 5),
    ([], 0),
    ([], 1)
    ])
def test_find_length(l, expected_result):
    assert f(l) == expected_result
