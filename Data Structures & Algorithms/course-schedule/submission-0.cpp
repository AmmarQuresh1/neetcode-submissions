class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> indegrees(numCourses, 0);
        vector<vector<int>> adj(numCourses);

        for (vector<int>& vi : prerequisites) {
            ++indegrees[vi[0]];
            adj[vi[1]].push_back(vi[0]); // prerequisite vi[1] unlocks vi[0]
        }

        queue<int> can_take;
        
        for (int i = 0; i < numCourses; ++i) {
            if (indegrees[i] == 0) {
                can_take.push(i);
            }
        }

        int coursesTaken {};
        while (!can_take.empty()){
            int cur_course = can_take.front();
            can_take.pop();
            ++coursesTaken;
            for (int neighbor : adj[cur_course]) {
                if (--indegrees[neighbor] == 0) {
                    can_take.push(neighbor);
                }
            }
        }

        return coursesTaken == numCourses;
    }
};
