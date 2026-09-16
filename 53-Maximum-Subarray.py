class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_sum = - INT_MAX;
        int curr_sum = 0;

        for (auto num : nums) {

            curr_sum = max(num, curr_sum + num);
            max_sum = max(curr_sum, max_sum);


        }

        return max_sum;

        
    }
};