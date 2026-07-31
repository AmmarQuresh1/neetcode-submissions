class Solution {
public:
    int find(vector<int>& parent, int a) {
        if (a != parent[a]) a = find(parent, parent[a]);
        return a;
    }

    void join(vector<int>& parent, int a, int b) {
        a = find(parent, a);
        b = find(parent, b);
        parent[b] = a;
    }

    int mstWeight(int n, vector<vector<int>>& edges, int forced = -1, int banned = -1) {
        vector<int> parent(n);
        iota(parent.begin(), parent.end(), 0);
        int count = 0, total = 0;

        if (forced != -1) {
            join(parent, edges[forced][0], edges[forced][1]);
            ++count; total += edges[forced][2];
        }

        for (int i = 0; i < edges.size(); ++i) {
            if (banned == i) continue;
            int a = edges[i][0], b = edges[i][1], w = edges[i][2];
            if (find(parent, a) != find(parent, b)) {
                join(parent, a, b);
                ++count; total += w;
            }
        }

        return count == n-1 ? total : INT_MAX;
    }

    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>>& edges) {
        for (int i = 0; i < edges.size(); ++i) {
            edges[i].push_back(i);
        }
        sort(edges.begin(), edges.end(), [](const vector<int>& a, const vector<int>& b) { return a[2] < b[2]; });

        int w = mstWeight(n, edges);
        vector<vector<int>> res{{}, {}};

        for (int i = 0; i < edges.size(); ++i) {
            int cur_w = mstWeight(n, edges, -1, i);
            if (w < cur_w) {
                res[0].push_back(edges[i][3]);
            } 
            else if (mstWeight(n, edges, i) == w) {
                res[1].push_back(edges[i][3]);
            }
        }

        return res;
    }
};