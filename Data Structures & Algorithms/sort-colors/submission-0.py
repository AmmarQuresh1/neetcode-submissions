class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # represents 0, 1, 2
        counts = [0, 0, 0]

        for n in nums:
            counts[n] += 1

        nums.clear()
        for i in range(len(counts)):
            for j in range(counts[i]):
                nums.append(i)