/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        ListNode* head = new ListNode{0, nullptr};

        ListNode* output = head;

        ListNode* end = recursive(output,l1, l2, 0);

        return head->next;

    }

    ListNode* recursive(ListNode* output, ListNode* l1, ListNode* l2, int carry) {
        int value = 0;

        if (!l1 && !l2) {

            if ( carry > 0) {
                output->next = new ListNode{carry, nullptr};
                return output;
            } 

            return output;

        }

        if (!l1) {
            value = carry + l2->val;
            
            if (value > 9) {
                carry = value / 10;
                value = value % 10;
                
                output->next = new ListNode{value, nullptr};
                return recursive(output->next, l1, l2->next, carry);

            } else {
                output->next = new ListNode{value, nullptr};
                return recursive(output->next, l1, l2->next, 0);
            }
        }

        if (!l2) {
            value = carry + l1->val;
            
            if (value > 9) {
                carry = value / 10;
                value = value % 10;
                output->next = new ListNode{value, nullptr};
                return recursive(output->next, l1->next, l2, carry);

            } else {
                output->next = new ListNode{value, nullptr};
                return recursive(output->next, l1->next, l2, 0);
            }
        }

        value = l1->val + l2->val + carry;

        if (value > 9) {
            carry = value / 10;
            value = value % 10;

            output->next = new ListNode{value, nullptr};
            return recursive(output->next, l1->next, l2->next, carry);

        } else {

            output->next = new ListNode{value, nullptr};
            return recursive(output->next, l1->next, l2->next, 0);

        }

    }
};