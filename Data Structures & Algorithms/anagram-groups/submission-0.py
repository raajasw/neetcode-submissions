class Solution:
    def groupAnagrams(self, strs: List[str]):
        res = defaultdict(list)
        for i in strs:
            strs_sorted = ''.join(sorted(i))
            res[strs_sorted].append(i)
        return list(res.values())
            
        
        