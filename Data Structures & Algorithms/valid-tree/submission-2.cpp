class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if (size(edges) != n-1) return false;

        std::array<int, 100> parent{};
        for (int i = 0; i < 100; ++i) {
            parent[i] = i;
        }

        for (auto vi : edges) {
            int temp = vi[0];
            while (temp != parent[temp]) {
                temp = parent[temp];
            }
            int temp2 = vi[1];
            while (temp2 != parent[temp2]) {
                temp2 = parent[temp2];
            }
            if (temp == temp2) return false;

            parent[std::max(parent[vi[0]], parent[vi[1]])] = parent[std::min(parent[vi[0]], parent[vi[1]])];
        }

        return true;
    }
};
