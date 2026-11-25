# 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Solution:

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())

# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
#     print(sol.groupAnagrams(strs = [""]))
#     print(sol.groupAnagrams(strs = ["a"]))