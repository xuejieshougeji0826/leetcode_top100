//
// Created by gzc on 2019-08-22.
//
#include "iostream"

//Definition for a binary tree node.
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if (t1 == nullptr && t2 == nullptr)
            return nullptr;
        if (t1 == nullptr)
            return t2;
        if (t2 == nullptr)
            return t1;
        else {
            t2->val = t2->val + t1->val;
            t2->left = mergeTrees(t1->left, t2->left);
            t2->right = mergeTrees(t1->right, t2->right);
        }
        return t2;
    }};