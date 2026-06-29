class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        std::unordered_set<int> seen_nodes{};
        int count = 0;
        for (vector<int>& vi : edges) {
            if (seen_nodes.find(vi[0]) == seen_nodes.end()) ++count;
            seen_nodes.insert(vi[0]);
            seen_nodes.insert(vi[1]);
        }

        return count + (n - edges.size());
    }
};
