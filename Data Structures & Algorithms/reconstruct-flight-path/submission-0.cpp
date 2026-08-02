class Solution {
public:
    void dfs(string cur, unordered_map<string, priority_queue<string, vector<string>, greater<>>>& adj_heap, vector<string>& res) {
        while(!adj_heap[cur].empty()) {
            string next_dest = adj_heap[cur].top();
            adj_heap[cur].pop();

            dfs(next_dest, adj_heap, res);
        }
        res.push_back(cur);
    }

    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string, priority_queue<string, vector<string>, greater<>>> adj_heap{};

        for (auto& vs : tickets) {
            string from = vs[0];
            string to = vs[1];
            adj_heap[from].push(to);
        }

        vector<string> res{};
        dfs("JFK", adj_heap, res);

        reverse(res.begin(), res.end());
        return res;
    }
};