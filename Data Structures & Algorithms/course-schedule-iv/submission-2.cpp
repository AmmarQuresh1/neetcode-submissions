class Solution {
public:
    vector<bool> checkIfPrerequisite(int numCourses, vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        vector<int> indirects(numCourses, 0);
        vector<vector<int>> adj(numCourses);

        for (vector<int> vi : prerequisites) {
            adj[vi[0]].push_back(vi[1]);
            ++indirects[vi[1]];
        }

        queue<int> can_take{};
        for (int i = 0; i < indirects.size(); ++i) {
            if (indirects[i] == 0) {
                can_take.push(i);
            }
        }

        vector<bool> answer(queries.size(), false);
        vector<unordered_set<int>> ancestor(numCourses);

        while (!can_take.empty()) {
            int cur = can_take.front(); can_take.pop();

            for (int neighbor : adj[cur]) {
                ancestor[neighbor].insert(cur);
                for (int x : ancestor[cur]) {
                    ancestor[neighbor].insert(x);
                }

                if (--indirects[neighbor] == 0) {
                    can_take.push(neighbor);
                }
            }
        }

        for (int i = 0; i < queries.size(); ++i) {
            if (ancestor[queries[i][1]].find(queries[i][0]) != ancestor[queries[i][1]].end()) {
                answer[i] = true;
            }
        }

        return answer;
    }
};