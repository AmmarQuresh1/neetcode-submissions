class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return nums[0];

        vector<vector<long int>> dp(n, vector<long int>(n, 1));

        long int maxProduct = INT_MIN;
        for (int i = 0; i < n; ++i) {
            dp[i][i] = nums[i];
            maxProduct = max(maxProduct, static_cast<long int>(nums[i]));
        }

        for (int len = 2; len <= n; ++len) {
            for (int i = 0; i + len <= n; ++i) {
                int j = i + len - 1;

                dp[i][j] = dp[i][j-1] * nums[j];

                maxProduct = max(maxProduct, dp[i][j]);
            }
        }

        return maxProduct;
    }
};
