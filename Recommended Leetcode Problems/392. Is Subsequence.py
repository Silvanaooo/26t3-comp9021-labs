class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Determines whether string s is a subsequence of string t.

        A subsequence means all characters of s appear in t
        in the same order, but not necessarily consecutively.

        Example:
            s = "abc", t = "ahbgdc"  →  True
            s = "axc", t = "ahbgdc"  →  False

        Algorithm:
            - Use the Two Pointer Technique.
            - One pointer (i) scans through s, another pointer (j) scans through t.
            - Move both forward when characters match.
            - Move only j forward when they don’t.
            - If i reaches the end of s, it means all characters were found in order.

        Time Complexity: O(len(t))
        Space Complexity: O(1)
        """

        # Initialize two pointers:
        # i for traversing s (the pattern)
        # j for traversing t (the text we search in)
        i, j = 0, 0

        # Continue while both pointers are within their string bounds
        while i < len(s) and j < len(t):
            # If current characters match, move pointer i forward
            if s[i] == t[j]:
                i += 1
            # Always move pointer j forward to keep scanning t
            j += 1

        # If i has reached the end of s, all characters have been matched in order
        return i == len(s)