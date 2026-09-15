class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        res = []

        for s in strs:
            key = tuple(sorted(s))  # sorted(s) => is a list ['a', 'c', 't']
                                    # use tuple => ('a', 'c', 't') - Immutable

            if key in anagram:
                anagram[key].append(s)
            else:
                anagram[key] = [s]

        return list(anagram.values())