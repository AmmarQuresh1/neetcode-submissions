class Solution {
public:
    int dfs(int i, std::array<int,2000>& parent) {
        while (i != parent[i]) i = parent[i];
        return i;
    }

    int countComponents(int n, vector<vector<int>>& edges) {
        std::array<int, 2000> parent{};
        for (int i = 0; i < n; ++i) parent[i] = i;

        for (vector<int>& vi : edges) {
            parent[vi[0]] = parent[vi[1]];
        }

        int i = 0;
        int count = 0;
        while (i < n){
            i = dfs(i, parent);
            ++count;
            ++i;
        }
        return count;
    }
};
