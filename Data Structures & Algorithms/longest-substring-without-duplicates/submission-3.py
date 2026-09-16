class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        ise = set()
        lenset = set({0})

        while j < len(s):
            while s[j] in ise:
                ise.remove(s[i])
                i += 1
            ise.add(s[j])
            j += 1
            lenset.add(len(ise))
        return max(lenset)

        