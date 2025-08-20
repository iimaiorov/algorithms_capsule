from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Return indices of the two numbers that add up to ``target``.

    Args:
        nums: List of integers.
        target: Desired sum.

    Returns:
        Indices of the two numbers that sum to ``target``.
    """
    result = {}
    for index, value in enumerate(nums):
        diff = target - value
        if diff in result:
            return [result[diff], index]
        result[value] = index
    return []
