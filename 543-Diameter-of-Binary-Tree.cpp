/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int max(int one, int two, int three = 0) {
        if (one >= two) {
            if (one >= three) {
                return one;
            }
        } 

        if (two >= three) {
            return two;
        }

        return three;
    }

    int diameterOfBinaryTree(TreeNode* root) {

        int main_root = node_diamater(root, 0);

        int biggest = wrapper(root, 0);

        int largest = max(main_root, biggest);
        
        return largest;

    }

    int wrapper(TreeNode* root, int biggest) {

        if(!root) { return biggest; }

        int left = node_diamater(root->left, 0);
        int right = node_diamater(root->right, 0);

        int big = max(left, right, biggest);

        return max(wrapper(root->right, big), wrapper(root->left, big));

    }


    int node_diamater(TreeNode* root, int big) {

        if (!root) {
            return big;
        }

        int right = recursive(root->right);
        int left = recursive(root->left);
        int r_con = 1;
        int l_con = 1;
        if (right == 0 && !root->right) {
            r_con = 0;
        }

        if (left == 0 && !root->left) {
            l_con = 0;
        }

        int diamater_at_node = r_con + l_con + right + left;

        return diamater_at_node;
    }

    int recursive(TreeNode* root) {

        if (!root) {
            return 0;
        }

        if (!root->right && !root->left) {
            return 0;
        }

        if (!root->left) {
            return 1 + recursive(root->right);
        }

        if (!root->right) {
            return 1 + recursive(root->left);
        }

        int left = 1 + recursive(root->left);
        int right = 1 + recursive(root->right);
        int result = max(left, right);
        return result; 

    }

};