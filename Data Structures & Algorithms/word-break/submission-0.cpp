class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.length();
        vector<int> dp(n+1, 0);
        dp[0] = 1;
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());

        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (dp[j] && wordSet.count(s.substr(j, i-j))) dp[i] = 1;
            }
        }

        return dp[n];
    }
};