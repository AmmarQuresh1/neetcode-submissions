class Solution {
public:
    int dfs(int i, int j, vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int size{};

        if (i < 0 || j < 0 || i >= rows || j >= cols || grid[i][j] == 0) {
            return size;
        }
        grid[i][j] = 0;
        ++size;

        size += dfs(i+1, j, grid);
        size += dfs(i-1, j, grid);
        size += dfs(i, j+1, grid);
        size += dfs(i, j-1, grid);
        
        return size;
    }

    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();

        int max_size{};
        for (int i{}; i != rows; ++i) {
            for (int j{}; j != cols; ++j) {
                max_size = std::max(dfs(i, j, grid), max_size);
            }
        }

        return max_size;
    }
};
