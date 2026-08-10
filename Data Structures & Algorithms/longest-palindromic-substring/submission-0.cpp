class Solution {
public:
    /*
     b a b a d
     0 1 2 3 4
    -----------
  0| 1 0 1 0 0
  1| 0 1 0 1 0
  2| 0 0 1 0 0
  3| 0 0 0 1 0
  4| 0 0 0 0 1

    0 - 2 | bab | T
    1 - 1 | a | T
    1 - 3 | aba | T
    2 - 2 | b | T
    */
    bool isPalindrome(int i, int j, std::string& s, vector<vector<int>>& arr) {
        if (arr[i][j] != -1) return arr[i][j];
        if (i == j) return arr[i][j] = 1;
        if (j-i == 1) return arr[i][j] = (s[i] == s[j]);

        return arr[i][j] = (s[i] == s[j] && isPalindrome(i+1, j-1, s, arr));
    }

    string longestPalindrome(string s) {
        if (s.length() == 1) return s;

        vector<vector<int>> arr(s.length(), vector<int>(s.length(), -1));

        int maxSize = INT_MIN;
        int maxI = -1;
        int count = -1;
        for (int len = 1; len <= s.length(); ++len) {
            for (int i = 0; i + len <= s.length(); ++i) {
                int j = i + len - 1;
                if (isPalindrome(i, j, s, arr) && abs(i-j) > maxSize) {
                    maxSize = abs(i-j);
                    maxI = i;
                    count = j-i+1;
                }
            }
        }

        return s.substr(maxI, count);
    }
};