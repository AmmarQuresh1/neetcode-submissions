class Solution {
    struct Node {
        int cost, row, col;
        bool operator>(const Node& o) const { return cost > o.cost; }
    };
public:
    int swimInWater(vector<vector<int>>& grid) {
        constexpr int MAX = INT_MAX / 2;
        constexpr array<pair<int,int>, 4> dirs = {{{1,0},{0,1},{-1,0},{0,-1}}};
        vector<vector<int>> distance(size(grid), vector<int>(size(grid), MAX));

        priority_queue<Node, vector<Node>, greater<>> heap{};
        heap.push({grid[0][0],0,0});
        distance[0][0] = grid[0][0];
        while (!heap.empty()) {
            auto [cost,x,y] = heap.top(); heap.pop();
            if (cost > distance[x][y]) continue;

            for (auto [dx, dy] : dirs) {
                int nx = x + dx, ny = y + dy;
                if (nx < 0 || ny < 0 || nx >= size(grid) || ny >= size(grid[0])) continue;

                int relaxed_dist = max(distance[x][y], grid[nx][ny]);
                if (distance[nx][ny] > relaxed_dist) {
                    distance[nx][ny] = relaxed_dist;
                    heap.push({relaxed_dist, nx, ny});
                }
            }
        }

        return distance[size(grid)-1][size(grid[0])-1];
    }
};