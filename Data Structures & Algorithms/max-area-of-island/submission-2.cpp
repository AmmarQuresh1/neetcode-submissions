class Solution {
public:
    int dfs(int i, int j, vector<vector<int>>& grid, vector<vector<bool>>& seen) {
        int rows = grid.size();
        int cols = grid[0].size();
        int size{};

        if (i < 0 || j < 0 || i >= rows || j >= cols) {
            return size;
        }
        if (grid[i][j] == 0) {
            return size;
        }
        if (seen[i][j] == true) {
            return size;
        }
        seen[i][j] = true;
        ++size;

        size += dfs(i+1, j, grid, seen);
        size += dfs(i-1, j, grid, seen);
        size += dfs(i, j+1, grid, seen);
        size += dfs(i, j-1, grid, seen);
        
        return size;
    }

    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();

        std::vector<std::vector<bool>> seen(rows, std::vector<bool>(cols, false));

        int max_size{};
        for (int i{}; i != rows; ++i) {
            for (int j{}; j != cols; ++j) {
                max_size = std::max(dfs(i, j, grid, seen), max_size);
            }
        }

        return max_size;
    }
};
