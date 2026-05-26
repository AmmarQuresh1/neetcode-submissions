class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Build hashmap grouping elements by frequency 
        freq = dict()

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # Sort into a list with descending order of value 
        sorted_list = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Return top K keys
        return [x[0] for x in sorted_list[:k]]