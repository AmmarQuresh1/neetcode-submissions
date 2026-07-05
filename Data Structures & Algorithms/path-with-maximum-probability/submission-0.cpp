class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        vector<vector<pair<int,double>>> adj(n);
        for (int i = 0; i < edges.size(); ++i) {
            adj[edges[i][0]].push_back({edges[i][1], succProb[i]}); // index: a -> [b, prob], ...
            adj[edges[i][1]].push_back({edges[i][0], succProb[i]}); // index : b -> [a, prob], ..
        }

        vector<double> prob_nodes(n, -1);
        priority_queue<pair<double,int>> max_pq{};
        prob_nodes[start_node] = 1.0;
        max_pq.push({prob_nodes[start_node], start_node});

        while (!max_pq.empty()) {
            auto [prob,cur] = max_pq.top(); max_pq.pop();
            if (prob < prob_nodes[cur]) continue;

            for (auto [b, succProb] : adj[cur]) {
                double prob_to_b = prob * succProb;
                if (prob_to_b > prob_nodes[b]) {
                    prob_nodes[b] = prob_to_b;
                    max_pq.push({prob_nodes[b], b});
                }
            }
        }

        return prob_nodes[end_node] != -1 ? prob_nodes[end_node] : 0;
    }
};