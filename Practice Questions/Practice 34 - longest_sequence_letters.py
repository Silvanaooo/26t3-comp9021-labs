import sys
word = input('Please input a string of lowercase letters: ')
if not word:
    print('The solution is: ')
    sys.exit()
if not all(c.islower() for c in word):
    print('Incorrect input.')
    sys.exit()






# Convert each character to its ASCII number for easy comparison
nums = [ord(c) for c in word]

# dp[i] stores the length of the longest consecutive-letter subsequence
# that ends at index i (using nums[i] as the last letter).
dp = [1] * len(nums)

# max_len keeps track of the global longest subsequence length found so far.
# last_index keeps the ending index (position in 'nums') of that subsequence.
max_len = 1
last_index = 0

# For each position i, look at all previous letters j < i
# and check if nums[i] continues a +1 pattern from nums[j].
for i in range(1, len(nums)):
    for j in range(0, i):
        # If current letter is exactly 1 greater (alphabetically next)
        # than nums[j], it can extend that subsequence.
        if nums[i] == nums[j] + 1:
            # Extend dp[j] by 1 and update dp[i] if it gives a longer chain.
            dp[i] = max(dp[i], dp[j] + 1)

    # After checking all j, update the global maximum if needed.
    if dp[i] > max_len:
        max_len = dp[i]
        last_index = i

# The sequence must be alphabetically consecutive (e.g., 'a' → 'b' → 'c' ...),
# so once we know the last letter (nums[last_index]) and the length (max_len),
# we can directly reconstruct the full sequence:
#   starting from (nums[last_index] - max_len + 1)
#   and generating +1 characters up to the end.
start_char_ord = nums[last_index] - max_len + 1
result = ''.join(chr(start_char_ord + k) for k in range(max_len))

# Output the final consecutive sequence
print(f"The solution is: {result}")