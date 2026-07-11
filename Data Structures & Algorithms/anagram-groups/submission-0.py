class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for st in strs:
            srd = str(sorted(st))
            if srd in dct:
                dct[srd].append(st)
            else:
                dct[srd] = [st]
        return [values for values in dct.values()]
