class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for word in strs:
            sk = ''.join(sorted(word))
            if sk in d:
                d[sk].append(word)
            else:
                d[sk] = [word]
        return d.values()
