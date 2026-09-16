class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {

        sort(nums.begin(), nums.end());
        vector<vector<int>> output; 
        int len = nums.size();
        int output_count = 0;

        int low = 0;
        int high = len - 1;

        for (int i = 0 ; i < len - 2 ; ++i) {
            
            int curr = i;
            low = i + 1;
            high = len - 1;
            int curr_num = nums[curr];
            int low_num = nums[low];
            int high_num = nums[high];

            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            while (low < high) {
                int low_num = nums[low];
                int high_num = nums[high];

                int sum = nums[i] + nums[low] + nums[high];

                if (high == low) {break;}

                if (sum == 0) {
                    output.push_back({curr_num, high_num, low_num});
                    ++output_count;
                    
                    --high;
                    while ( high >= 0 && high_num == nums[high]) { --high; }

                    ++low;
                    while (low < len - 1 && low_num == nums[low]) { ++low; }

                    continue;
                }

                if (sum < 0) {

                    ++low;
                    while (low < len - 1 && low_num == nums[low] ) { ++low; }
                    continue;
                }

                if (sum > 0) {
                    --high;
                    while (high >= 0 && high_num == nums[high]) { --high; }
                    continue;
                }

            }

        }
        return output;
    }
};