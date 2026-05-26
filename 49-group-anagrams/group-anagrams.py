class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        ans = []

        for s in strs:
            sorted_s = str(sorted(s))
            anagrams[sorted_s].append(s)
        
        for key in anagrams:
            ans.append(anagrams[key])
        
        return ans