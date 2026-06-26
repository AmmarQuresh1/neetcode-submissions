class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        std::array<int, 100> parent{};
        for (int i = 0; i < 100; ++i) {
            parent[i] = i;
        }

        for (auto vi : edges) {
            if (parent[vi[0]] == parent[vi[1]])
                return false;

            parent[std::max(parent[vi[0]], parent[vi[1]])] = parent[std::min(parent[vi[0]], parent[vi[1]])];
        }
        return true;
    }
};
