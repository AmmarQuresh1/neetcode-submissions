class Solution {
    std::array<int, 101> parent{};
public:
    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }

    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        for (size_t i = 1; i < std::size(edges) + 1; ++i) parent[i] = i;

        for (auto vi : edges) {
            int a = find(vi[0]);
            int b = find(vi[1]);
            if (a == b) return vi;
            parent[a] = b;
        }

        return edges[edges.size() - 1];
    }
};
