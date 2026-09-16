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
    vector<int> inorderTraversal(TreeNode* root) {
        
        vector<int> output;

        inorderTraversall(root, output);

        return output;
    }


    void inorderTraversall(TreeNode* root, vector<int>& output) {

        if (!root) { return; }

        if (!root->left && !root->right) {
            output.push_back(root->val);
            return;
        }

        if (root->left && root->right) {
            inorderTraversall(root->left, output);
            output.push_back(root->val);
            inorderTraversall(root->right, output);
            return;
        }

        if (root->left) {
            inorderTraversall(root->left, output);
            output.push_back(root->val);
            return;
        }

        if (root->right) {
            output.push_back(root->val);
            inorderTraversall(root->right, output);
            return;
        }

        return;
    }
};