class Solution {
public:
    struct Node{
        int price, location, k;

        bool operator>(const Node& o) const { return price > o.price; }
    };

    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        // pair<k, to>
        priority_queue<Node, vector<Node>, greater<>> heap{};
        vector<vector<int>> best(n, vector<int>(k+1, INT_MAX));
        
        for (auto& vi : flights) {
            if (vi[0] == src) {
                heap.push({vi[2],vi[1],k});
                best[vi[1]][k] = vi[2];
            }
        }
        
        int cost = 0;
        while (!heap.empty()) {
            auto [price, loc, cur_k] = heap.top(); heap.pop();
            
            if (cur_k >= 0 && loc == dst) {
                return price;
            }
            
            if (cur_k > 0) {
                for (auto& vi : flights) {
                    if (vi[0] == loc && price + vi[2] < best[vi[1]][cur_k-1]) {
                        heap.push({price + vi[2], vi[1], cur_k - 1});
                        best[vi[1]][cur_k-1] = price + vi[2];
                    } 
                }
            }

        }

        return -1;
    }
};