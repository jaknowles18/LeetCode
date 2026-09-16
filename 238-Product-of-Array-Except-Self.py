class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int len = nums.size();
        vector<int> left(len);
        vector<int> answer(len);

        map<int, int> seen;
        
        int prod = 1;

        if (len == 0) { return answer;}

        for (int i = 1 ; i < len ; ++i) {

            prod *= nums[i - 1]; 
            left[i] = prod; 

        }
        answer[len - 1] = prod ;
        prod = 1;

        for (int i = len - 2 ; i > 0 ; --i) {
            prod *= nums[i + 1];

            answer[i] = prod * left[i];
        }

        answer[0] = prod * nums[1];
        return answer;

    }
};