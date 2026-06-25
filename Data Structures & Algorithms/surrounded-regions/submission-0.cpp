class Solution {
    constexpr static int MAX_SIZE = 200 * 200 + 1;

    template<typename T, std::size_t N>
    struct FixedQueue {
        std::array<T, N> queue{};
        int head = 0;
        int tail = 0;
        void push(T item) { queue[tail++] = item; }
        T pop() { return queue[head++]; }
        bool empty() { return head==tail; }
    };
public:
    void solve(vector<vector<char>>& board) {
        int ROWS = std::size(board), COLS = std::size(board[0]);
        FixedQueue<std::pair<int,int>, MAX_SIZE> queue;

        if (ROWS <= 2 || COLS <= 2) { return; }

        for (int i = 0; i < ROWS; ++i) {
            if (board[i][0] == 'O') { queue.push({i,0}); }
            if (board[i][COLS-1] == 'O') { queue.push({i,COLS-1}); }
        }
        for (int i = 0; i < COLS; ++i) {
            if (board[0][i] == 'O') { queue.push({0,i}); }
            if (board[ROWS-1][i] == 'O') { queue.push({ROWS-1,i}); }
        }

        constexpr std::array<std::pair<int,int>,4> directions {{{1,0},{0,1},{-1,0},{0,-1}}};
        while (!queue.empty()) {
            auto [i,j] = queue.pop();
            board[i][j] = 'U'; 
            for (auto [dr,dc] : directions) {
                int nr = i + dr, nc = j + dc;
                if (nr >= 0 && nc >= 0
                    && nr < ROWS && nc < COLS
                    && board[nr][nc] == 'O') {
                        queue.push({nr,nc});
                        board[nr][nc] = 'U';
                    }
            }
        }

        for (vector<char>& vc : board) {
            for (char& c : vc) {
                if (c == 'U') { c = 'O'; continue; }
                c = 'X';
            }
        }
    }
};