class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ouptut = [] 
        anagramMap = dict()

        # Build hashmap (Signature -> List of Words)
        # Signature, tuple of cc's from list

        for s in strs:
            charCounts = [0] * 26 # Letters in alphabet
            for c in s:
                index = ord(c) - ord("a")
                charCounts[index] += 1
            charCounts = tuple(charCounts)
            anagramMap[charCounts] = anagramMap.get(charCounts, [])
            anagramMap[charCounts].append(s)
        
        # Group anagrams in anagramsMap
        return list(anagramMap.values())
