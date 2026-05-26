class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = []
        postfixProduct = []
        length = len(nums)
        for i, num in enumerate(nums):
            if i == 0:
                prefixProduct.append(num)
                postfixProduct.append(nums[length-i-1])
            else:
                prefixProduct.append(num * prefixProduct[i-1])
                postfixProduct.append(nums[length-i-1] * postfixProduct[i-1])
        
        output = []

        for i in range(length):
            if i == 0:
                output.append(postfixProduct[length-2])
            elif i == length - 1:
                output.append(prefixProduct[i-1])
            else:
                output.append(prefixProduct[i-1] * postfixProduct[length-2-i])

        return output