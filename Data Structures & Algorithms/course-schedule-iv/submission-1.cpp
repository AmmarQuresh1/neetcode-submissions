class Solution {
public:
    vector<bool> checkIfPrerequisite(int numCourses, 
    vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        vector<int> indegree(numCourses, 0);
        vector<vector<int>> adj(numCourses);

        for (vector<int> vi : prerequisites) {
            ++indegree[vi[1]];
            adj[vi[0]].push_back(vi[1]);
        }
        queue<int> can_take;
        
        for (int i = 0; i < indegree.size(); ++i) {
            if (indegree[i] == 0) {
                can_take.push(i);
            }
        }

        vector<vector<bool>> successors(numCourses, vector<bool>(numCourses, false));
        while (!can_take.empty()) {
            int cur = can_take.front(); can_take.pop();
            for (int x : adj[cur]) {
                successors[x][cur] = true;
                for (int anc = 0; anc < numCourses; ++anc) {
                    if (successors[cur][anc]) successors[x][anc] = true;
                }
                if (--indegree[x] == 0) can_take.push(x);
            }
        }

        vector<bool> res(queries.size(), false);
        for (int i = 0; i < queries.size(); ++i) {
            res[i] = successors[queries[i][1]][queries[i][0]];
        }

        return res;
    }
};