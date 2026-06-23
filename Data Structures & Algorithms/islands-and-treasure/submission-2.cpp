auto init = []() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    return 0;
}();

class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        constexpr int max = std::numeric_limits<int>::max();
        constexpr int MAX_ELEMENTS = 100 * 100;
        int head = 0, tail = 0;
        int row = grid.size();
        int col = grid[0].size();

        std::array<std::pair<int, int>, MAX_ELEMENTS> q;


        for (int i{}; i != row; ++i) {
            for (int j{}; j != col; ++j) {
                if (grid[i][j] == 0) {
                    q[tail++] = {i, j};
                }
            }
        }


        constexpr std::array<std::pair<int,int>, 4> directions{{
            {1,0}, {0,1}, {-1,0}, {0,-1}
        }};
        while (head != tail) {
            auto [r, c] = q[head++];

            for (auto [dr, dc] : directions) {
                int nr = dr + r, nc = dc + c;
                if (nr >= 0 && nr < row && nc >= 0 && nc < col
                    && grid[nr][nc] == max) {
                        grid[nr][nc] = grid[r][c] + 1;
                        q[tail++] = {nr, nc};
                    }
            }
        }
    }
};
