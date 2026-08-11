class Solution {
public:
    int countSubstrings(string s) {
        int n = s.length();
        if (n == 1) return 1;

        vector<vector<int>> dp(n, vector<int>(n, -1));
        int count {};

        for (int len = 1; len <= n; ++len) {
            for (int i = 0; i + len <= n; ++i) {
                int j = len + i - 1;

                if (len == 1) dp[i][j] = true;
                else if (len == 2) dp[i][j] = (s[i] == s[j]);
                else dp[i][j] = (s[i] == s[j] && dp[i+1][j-1]);

                if (dp[i][j] == 1) ++count;
            }
        }

        return count;
    }
};