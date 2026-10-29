# ================= Explanation ================= #
"""
We use DP to solve the problem.

1. DP definition: dp[i] = the length of the longest increasing subsequence ending at index i
Each subsequence must end with some number,
so it's natural to define it as “ending at nums[i]”.
That helps compare previous elements (nums[j] < nums[i]).

2. Transition: dp[i] = max(dp[i], dp[j] + 1)
If the current number nums[i] is larger than nums[j],
then nums[i] can be added after the sequence that ends at nums[j].

3. Initialization: dp = [1] * n
Each element itself can form a subsequence of length 1.

4. Traversal order
i goes from left to right.
For each i, check all previous j from 0 to i-1.
This ensures smaller indexes are already computed.

5. Result
The final answer is the maximum value in dp,
because the longest subsequence might end anywhere.
"""

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # Edge case: empty list
        if not nums:
            return 0

        # dp[i] means:
        # the length of the longest increasing subsequence
        # that ends with nums[i]
        dp = [1] * len(nums)

        # For each position i, look at all numbers before it (0 ~ i-1)
        for i in range(len(nums)):
            for j in range(i):
                # If nums[i] can extend the sequence that ends at nums[j]
                if nums[j] < nums[i]:
                    # Update dp[i] to be the longest found so far
                    dp[i] = max(dp[i], dp[j] + 1)

        # The result is the longest subsequence among all dp[i]
        return max(dp)