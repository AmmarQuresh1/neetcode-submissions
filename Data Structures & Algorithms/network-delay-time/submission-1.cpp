class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int,int>>> adj(n+1);

        for (vector<int> time : times) {
            int u = time[0], v = time[1], w = time[2];
            adj[u].push_back({v, w});
        }

        vector<int> dists(n+1, numeric_limits<int>::max());
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> heap{};
        dists[k] = 0;
        dists[0] = 0;
        heap.push({0,k});

        while(!heap.empty()) {
            auto [d, node] = heap.top();
            heap.pop();
            if (d > dists[node]) {
                continue;
            }
            for (auto[v,w] : adj[node]) {
                if ((dists[node] + w) < (dists[v])) {
                    dists[v] = dists[node] + w;
                    heap.push({dists[v], v});
                }
            }
        }


        int max = -1;
        for (auto x : dists) {
            if (x == numeric_limits<int>::max()) return -1;
            if (x > max) max = x;
        }

        return max;
    }
};