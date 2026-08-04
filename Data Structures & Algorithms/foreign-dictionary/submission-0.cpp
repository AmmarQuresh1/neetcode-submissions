class Solution {
public:
    char to_c(const int i) {
        return static_cast<char>(i + 'a');
    }

    int to_i(const char ch) {
        return static_cast<int>(ch - 'a');
    }

    string foreignDictionary(vector<string>& words) {
        vector<unordered_set<int>> adj(26);
        array<int,26> indirects{};
        array<bool,26> present{};

        for (const string& w : words) {
            for (char ch : w) {
                present[to_i(ch)] = true;
            }
        }

        for (int i = 0; i < words.size() - 1; ++i) {
            for (int y = 0; y < min(words[i].size(), words[i+1].size()); ++y) {
                int first, second;
                first = to_i(words[i][y]);
                second = to_i(words[i+1][y]);
                if (words[i][y] != words[i+1][y]) {
                    if (adj[first].find(second) == adj[first].end()) ++indirects[second];
                    adj[first].insert(second);
                    break;
                }
                if (y != words[i].length()-1 && y == words[i+1].length()-1) return "";
            }
        }

        queue<int> can_take{};
        for (int i = 0; int x : indirects) {
            if (present[i] && x == 0) can_take.push(i);
            ++i; 
        }

        string res;
        while (!can_take.empty()) {
            int cur = can_take.front(); can_take.pop();
            res += to_c(cur);
            for (int neighbor : adj[cur]) {
                if (--indirects[neighbor] == 0) {
                    can_take.push(neighbor);
                }
            }
        }

        return (res.size() == [&](){
            int count = 0;
            for (bool p : present) {
                if (p) ++count;
            }
            return count;
        }() ? res : "");
    }
};
