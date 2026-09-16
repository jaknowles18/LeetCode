class Solution {
public:
    bool isPalindrome(int x) {
        
        string rex = to_string(x);
        string ex = to_string(x);
        reverse(rex.begin(), rex.end());

        return ex == rex;
    }
};