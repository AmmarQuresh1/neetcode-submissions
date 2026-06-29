class Solution {
public:
    int find(int n, std::array<int,2000>& parent) {
        while (n != parent[n]) n = parent[n];
        return n;
    }

    int countComponents(int n, vector<vector<int>>& edges) {
        std::array<int, 2000> parent{};
        for (int i = 0; i < n; ++i) parent[i] = i;

        for (vector<int>& vi : edges) {
            parent[find(vi[0], parent)] = find(vi[1], parent);
        }

        int i = 0;
        int count = 0;
        while (i < n-1) {
            i = find(i, parent);
            ++i;
            ++count;
        }
        return count;
    }
};
