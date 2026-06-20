/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* dfs(Node* node, unordered_map<Node*,Node*>& seen) {
        if (seen.find(node) != seen.end()) {
            return seen[node];
        }

        Node* new_node = new Node(node->val);
        seen[node] = new_node;

        for (auto&x:node->neighbors) {
            new_node->neighbors.push_back(dfs(x,seen));
        }
        return new_node;
    }

    Node* cloneGraph(Node* node) {
        if (!node) {
            return nullptr;
        }

        unordered_map<Node*,Node*> seen;
        return dfs(node, seen);
    }
};
