"""
	1.	DP definition
dp[i] = the length of the longest continuous increasing subsequence that ends at i.
Continuous means: indices are consecutive (no gaps).
	2.	Transition
Only one check is needed:
If nums[i+1] > nums[i], then dp[i+1] = dp[i] + 1
Else, the increasing run breaks at i+1, so dp[i+1] = 1 (already set)
	3.	Initialization
Every index can start a new run ⇒ dp[i] = 1.
	4.	Answer
The maximum value of dp[i] over all i.
"""
class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        # Edge case: empty array → length is 0
        if len(nums) == 0:
            return 0

        # dp[i] = length of the Longest Continuous (i.e., contiguous) Increasing
        # Subsequence that ENDS at index i (must include nums[i]).
        # Every single element is a longest continuous subsequence of length 1 by itself.
        dp = [1] * len(nums)

        # result keeps the maximum dp[i] seen so far.
        result = 1

        # For each position i+1, check if it can extend the increasing run ending at i.
        # Because the subsequence must be CONTIGUOUS, we only compare nums[i+1] with nums[i].
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                # nums[i+1] extends the increasing sequence ending at i
                dp[i + 1] = dp[i] + 1
            # Otherwise dp[i+1] stays 1 (already initialized), because the run breaks here.

            # Update the global best
            result = max(result, dp[i + 1])

        return result