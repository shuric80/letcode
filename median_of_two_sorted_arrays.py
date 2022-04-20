from typing import List
import pytest


def get_max(array, partition: int) -> int:
    if partition == 0:
        return float('-inf')
    else:
        return array[partition - 1]


def get_min(array, partition: int) -> int:
    if partition == len(array):
        return float('inf')
    else:
        return array[partition]


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    lo = 0
    hi = len(nums1)
    total = len(nums1) + len(nums2)
    while lo <= hi:
        part_x = int((lo + hi) / 2)
        part_y = int((total + 1) / 2 - part_x)

        left_x = get_max(nums1, part_x)
        right_x = get_min(nums1, part_x)

        left_y = get_max(nums2, part_y)
        right_y = get_min(nums2, part_y)

        if left_x <= right_y and left_y <= right_x:
            if total % 2 == 0:
                return (max(left_x, left_y) + min(right_x, right_y)) / 2.0
            return max(left_y, left_x)
        if left_x > right_y:
            hi = part_x - 1
        else:
            lo = part_x + 1
    return -1


@pytest.mark.parametrize("num1, num2, output",
                         (([1, 3], [2], 2), ([1, 2], [3, 4], 2.5)))
def test_median_of_two_sorted(num1, num2, output):
    assert find_median_sorted_arrays(num1, num2) == output
