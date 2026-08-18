class Solution {
/*
10-1-2
J A B
10-12
J L

s = 1012
arr:
1 0 0 0 0
1 1 1 1 2
if i != 0 && i and i-1 valid then dp[i] = dp[i-1] + dp[i-2]
else dp[i] = dp[i-1]

s = 06
arr:
1 0 0
1 0 0
1 0 1

s = 12345
arr:
1 0 0 0 0 0
1 1 2 3 3 3

*/
public:
    int numDecodings(string s) {
        int n = s.length();
        int cur = 1, prev = 0;

        for (int i = 0; i < n; ++i) {
            int next = 0;
            if (s[i] - '0' != 0) {
                next += cur;
            }
            if (i > 0 && (s[i-1] - '0' == 1) || (s[i-1] - '0' == 2 && s[i] - '0' <= 6)) {
                next += prev;
            }

            prev = cur; cur = next;
        }

        return cur;
    }
};
