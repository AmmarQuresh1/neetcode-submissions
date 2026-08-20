class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();

        long int cMax = nums[0];
        long int cMin = nums[0];
        long int maxProd = nums[0];

        for (int i = 1; i < n; ++i) {
            long int curVal = static_cast<long int>(nums[i]);
            long int temp = max({curVal, curVal * cMax, curVal * cMin});
            cMin = min({curVal, curVal * cMax, curVal * cMin});
            cMax = temp;   

            maxProd = max(maxProd, temp);
        }        

        return maxProd;
    }
};
