# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without duplicate characters.

# Solution:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        max_len = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1

            seen.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len


# Check:
# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.lengthOfLongestSubstring("abcabcbb"))
#     print(sol.lengthOfLongestSubstring("bbbbb"))
#     print(sol.lengthOfLongestSubstring("pwwkew"))