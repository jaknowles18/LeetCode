class Solution {
public:
    int numberOfSubstrings(string s) {
        int n = s.length();
        int left = 0;
        int ans = 0;

        map<char, int> count;

        for (int right = 0; right < n; right++) {
            count[s[right]]++;

            while (count['a'] > 0 && count['b'] > 0 && count['c'] > 0) {
                ans += n - right;

                count[s[left]]--;
                left++;
            }
        }

        return ans;

    }
};