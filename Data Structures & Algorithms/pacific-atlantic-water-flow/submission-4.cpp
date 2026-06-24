class Solution {
private:
    constexpr static std::size_t MAX_SIZE = 200 * 200 + 1;

    template<typename T, std::size_t N>
    struct FixedQueue {
        std::array<T, N> data;
        int head = 0;
        int tail = 0;
        void push(T item) { data[tail++] = item; }
        T pop() { return data[head++]; }
        bool empty() { return head==tail; }
    };
public:
    void bfs(std::vector<std::vector<int>>& grid, 
            FixedQueue<std::pair<int,int>, MAX_SIZE>& queue,
            std::array<std::array<int,201>, 201>& bitwise_seen, int bitwise_append) {
        constexpr std::array<std::pair<int,int>, 4> directions{{{1,0}, {0,1}, {-1,0}, {0,-1}}};
        while (!queue.empty()) {
            auto [i, j] = queue.pop();
            for (auto [r,c] : directions) {
                int nr = i + r, nc = j + c;
                if (nr >= 0 && nc >= 0 &&
                    nr < std::size(grid) && nc < std::size(grid[0])
                    && grid[nr][nc] >= grid[i][j]
                    && (bitwise_seen[nr][nc] & bitwise_append) == 0) {// 00 & 01 == 0 || 01 & 10 == 0  
                        queue.push({nr,nc});
                        bitwise_seen[nr][nc] |= bitwise_append;
                    }
            }
        }
    }

    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        std::array<std::array<int,201>, 201> bitwise_seen{};
        FixedQueue<std::pair<int,int>, MAX_SIZE> p_queue{};
        FixedQueue<std::pair<int,int>, MAX_SIZE> a_queue{};
        int rows = heights.size(), cols = heights[0].size();

        for (int i = 0; i < rows; ++i) {
            p_queue.push({i,0});
            bitwise_seen[i][0] |= 1;

            a_queue.push({i,cols-1});
            bitwise_seen[i][cols-1] |= 2;
        }

        for (int i = 0; i < cols; ++i) {
            p_queue.push({0,i});
            bitwise_seen[0][i] |= 1;

            a_queue.push({rows-1,i});
            bitwise_seen[rows-1][i] |= 2;
        }
        
        bfs(heights, p_queue, bitwise_seen, 1);
        bfs(heights, a_queue, bitwise_seen, 2);
        
        std::vector<std::vector<int>> res{};
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (bitwise_seen[i][j] == 3)
                    res.push_back({i,j});
            }
        }

        return res;
    }
};