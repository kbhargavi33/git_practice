# to sort array by
# iterate through array, find max number. shift last number in array to max number index
# and then shift max number to last index.
# repeat the process for len(array)-1 subarray each time until array gets sorted

import pytest
def f(a):
    j = len(a)-1
    l = len(a)
    while(j>=1):
        max_item = float('-inf')
        for i in range(l):
            if a[i] > max_item:
                max_item = a[i]
                max_index = i
        l-=1
        if a[j]!= max_item:
            a[max_index] = a[j]
            a[j] = max_item
        j-=1
    return a

@pytest.mark.parametrize("input_array, expected_output", [
    ([5,1,6,2], [1,2,5,6]),
    ([1,2], [1,2]),
    ([2,1], [1,2]),
    ([5,2,1,5], [1,2,5,5])
])
def test_f(input_array, expected_output):
    assert f(input_array) == expected_output

# Run tests
pytest.main()
