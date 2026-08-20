class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();

        long int maxSubarray = nums[0];
        long int curSubarray = nums[0];

        int i = 0;
        for (int j = 1; j < n; ++j) {
            if (i <= j && nums[j] * curSubarray < curSubarray) {
                curSubarray *= nums[j];
                curSubarray /= nums[i];
                ++i;
            } else {
                curSubarray *= nums[j];
            }
            maxSubarray = max(maxSubarray, curSubarray);
        }

        return maxSubarray;
    }
};
