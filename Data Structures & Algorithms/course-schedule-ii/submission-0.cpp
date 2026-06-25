class Solution {
    constexpr static int MAX_SIZE = 2000;

    template<typename T, std::size_t N>
    struct FixedQueue{
        std::array<T,N> queue{};
        int head = 0;
        int tail = 0;
        void push (T item) { queue[tail++] = item; }
        T pop () { return queue[head++]; }
        bool empty () { return head == tail; }
    };
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        FixedQueue<int, MAX_SIZE> queue;
        std::vector<int> indirects(numCourses);
        std::vector<vector<int>> adj(numCourses);

        for (vector<int>& vi : prerequisites) {
            ++indirects[vi[0]];
            adj[vi[1]].push_back(vi[0]);
        }

        for (int i = 0; i < std::size(indirects); ++i) {
            if (indirects[i] == 0) {
                queue.push(i);
            }
        }

        std::vector<int> res{};
        while (!queue.empty()) {
            int course = queue.pop();
            res.push_back(course);
            for (int neighbor : adj[course]) {
                if (--indirects[neighbor] == 0) { queue.push(neighbor); } 
            }
        }

        return std::size(res) == numCourses ? res : std::vector<int>();
    }
};