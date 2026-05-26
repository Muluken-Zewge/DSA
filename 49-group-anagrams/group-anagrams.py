class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        ans = []

        for s in strs:
            sorted_s = str(sorted(s))
            anagrams[sorted_s].append(s)
        
        return list(anagrams.values())