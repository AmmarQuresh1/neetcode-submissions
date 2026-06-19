class Solution {
public:
    void dfs(vector<vector<char>>& grid, int i, int j) {
        if (i < 0 || i >= static_cast<int>(grid.size()) || j < 0 || j >= static_cast<int>(grid[i].size()))
            return;
        if (grid[i][j] == '0')
            return;
        
        grid[i][j] = '0';
        dfs(grid, i+1, j);
        dfs(grid, i-1, j);
        dfs(grid, i, j+1);
        dfs(grid, i, j-1);

        return;
    }

    int numIslands(vector<vector<char>>& grid) {
        int count {};
        for (int i{}; i!=static_cast<int>(grid.size()); ++i){
            for (int j{}; j!=static_cast<int>(grid[i].size()); ++j){
                if (grid[i][j] == '1'){
                    ++count;
                    dfs(grid, i, j);
                }
            }
        }

        return count;
    }
};
