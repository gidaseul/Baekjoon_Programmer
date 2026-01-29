class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        pref_len = len(pref)

        for i in strs[1:]:
            while pref != i[0:pref_len]:
                pref_len -= 1
                if pref_len ==0:
                    return ""

                pref = pref[0:pref_len]

        return pref