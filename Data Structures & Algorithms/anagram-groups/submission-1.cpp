class Solution {
    struct ArrayHash {
        size_t operator()(const array<int, 26> arr) const {
            size_t h = 0;
            for (int x : arr) {
                h = h * 31 + x;
            }
            return h;
        }
    };

public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<array<int, 26>, vector<string>, ArrayHash> char_map;

        for (string& str : strs) {
            array<int, 26> char_count{};
            for (char c : str) {
                int idx = static_cast<int>(c - 'a');
                ++char_count[idx];
            }
            char_map[char_count].push_back(str);
        }

        vector<vector<string>> res{};
        for (auto& [arr, vs] : char_map) {
            res.push_back(vs);
        }

        return res;
    }
};