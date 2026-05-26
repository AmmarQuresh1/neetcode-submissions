class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Build hashmap grouping elements by frequency 
        freq = dict()

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # Bucket sort
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        # Return top K keys
        output = []
        for freq in range(len(buckets) - 1, -1, -1):
            for num in buckets[freq]:
                output.append(num)
                if len(output) == k:
                    return output
