class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        total = []

        for i in strs:
            
            key = ''.join(sorted(i))

            if key not in seen:
                seen[key] = []
            
            seen[key].append(i)
        
        return list(seen.values())

                