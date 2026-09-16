class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> counts;

        for (auto num: nums) {
            if (counts.count(num)) {
                return true;
            }

            counts.insert(num);
        }

        return false;
    }
};