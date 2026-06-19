auto speedup = []() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    return 0;
}();

class Solution {
public:
    struct Cell {
        int i;
        int j;
        int dist;
    };

    struct Point {
        int i;
        int j;
    };

    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        deque<Cell> q;

        if (grid[0][0] == 1) return -1;

        vector<Point> directions {{1, 0}, {1, 1}, {0, 1}, {-1, 1}, {-1, 0}, {-1, -1}, {0, -1}, {1, -1}};
        q.push_back({0, 0, 1});
        grid[0][0] = 1;        
        while (!q.empty()) {
            auto [i, j, dist] = q.front();
            if (i == static_cast<int>(grid.size())-1 && j == static_cast<int>(grid[i].size())-1)
                return dist;
            q.pop_front();
            
            for (auto& [x,y] : directions){
                if ((i+x >= static_cast<int>(grid.size()) || j+y >= static_cast<int>(grid[i].size())
                    || i+x < 0 || j+y < 0) || (grid[i+x][j+y] == 1))
                    continue;
                q.push_back({i+x, j+y, dist + 1});
                grid[i+x][j+y] = 1;
            }
        }

        return -1;
    }
};