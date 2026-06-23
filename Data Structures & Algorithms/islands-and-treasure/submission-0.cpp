class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int max = std::numeric_limits<int>::max();
        int row = grid.size();
        int col = grid[0].size();
        std::queue<std::pair<int,int>> q;

        for (int i{}; i != row; ++i) {
            for (int j{}; j != col; ++j) {
                if (grid[i][j] == 0) {
                    q.push({i, j});
                }
            }
        }


        std::array<std::pair<int,int>, 4> directions{{
            {1,0}, {0,1}, {-1,0}, {0,-1}
        }};
        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop();

            for (auto [dr, dc] : directions) {
                int nr = dr + r, nc = dc + c;
                if (nr >= 0 && nr < row && nc >= 0 && nc < col
                    && grid[nr][nc] == max) {
                        grid[nr][nc] = grid[r][c] + 1;
                        q.push({nr, nc});
                    }
            }
        }
    }
};
