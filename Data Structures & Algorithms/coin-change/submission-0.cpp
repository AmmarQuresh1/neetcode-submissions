class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount+1, -1);
        dp[0] = 0;
        
        for (int c : coins) {
            if (c > amount) continue;
            dp[c] = 1;
        }
        
        for (int i = 1; i <= amount; ++i) {
            if (dp[i] == -1) {
                int fewest_coins = INT_MAX;
                for (int c : coins) {
                    if (i - c < 0) continue;
                    if (dp[i-c] == -1) continue;
                    fewest_coins = min(1+dp[i-c], fewest_coins);
                }
                if (fewest_coins != INT_MAX) dp[i] = fewest_coins;
            }
        }

        return dp[amount];
    }
};
