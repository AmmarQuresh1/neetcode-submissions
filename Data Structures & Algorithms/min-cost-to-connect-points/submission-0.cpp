class Solution {
    struct Point {
        int x, y;
        Point(int ix, int iy) : x{ix}, y{iy} {}
    };

public:
    int manhattan(Point x, Point y) {
        return abs(x.x - y.x) + abs(x.y - y.y);
    }

    int minCostConnectPoints(vector<vector<int>>& points) {
        vector<int> dist(points.size(), INT_MAX);
        vector<bool> inTree(points.size(), false);
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> min_pq{};

        dist[0] = 0;
        min_pq.push({0, 0});
        int cost = 0;
        while (!min_pq.empty()) {
            auto [d, i] = min_pq.top(); min_pq.pop();
            if (inTree[i]) continue;
            inTree[i] = true;
            cost += d;
            for (int j = 0; j < points.size(); ++j) {
                if (inTree[j]) continue;

                int man = manhattan({points[j][0], points[j][1]}, {points[i][0], points[i][1]});
                if (man < dist[j]) {
                    dist[j] = man;
                    min_pq.push({dist[j], j});
                }
            }
        }

        return cost;
    }
};