class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        std::unordered_map<std::string,std::vector<int>> wildcard{};
        for (int i = 0; i < std::size(wordList); ++i){
            for (int j = 0; j < std::size(wordList[i]); ++j) {
                std::string temp_word = wordList[i];
                temp_word[j] = '*';
                wildcard[temp_word].push_back(i);
            }
        }


        std::queue<std::string> queue{};
        std::unordered_set<std::string> seen{};
        queue.push(beginWord);
        int count = 1;
        while (!queue.empty()) {
            int levelSize = queue.size();

            for (int lvl = 0; lvl < levelSize; ++lvl) {
                std::string word = queue.front();
                queue.pop();
            
                if (word == endWord) return count;

                for (int i = 0; i < std::size(word); ++i) {
                    std::string temp = word;
                    temp[i] = '*';
                    if (wildcard.find(temp) != wildcard.end()) {
                        for (auto wordIdx : wildcard[temp]) {
                            if (!seen.contains(wordList[wordIdx])) {
                                queue.push(wordList[wordIdx]);
                                seen.insert(wordList[wordIdx]);
                            }
                        }
                    }
                }
            }
            ++count; 
        }

        return 0;
    }
};