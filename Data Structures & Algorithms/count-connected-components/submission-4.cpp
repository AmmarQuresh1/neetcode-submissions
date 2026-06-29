class Solution {
public:
    int dfs(int i, std::array<int,2000>& parent) {
        
    }

    int countComponents(int n, vector<vector<int>>& edges) {
        std::array<int, 2000> parent{};
        for (int i = 0; i < n; ++i) parent[i] = i;

        for (vector<int>& vi : edges) {
            if (vi[0] < vi[1]) parent[vi[1]] = parent[vi[0]];
            else parent[vi[0]] = parent[vi[1]];
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
