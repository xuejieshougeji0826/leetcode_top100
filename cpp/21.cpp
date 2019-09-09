//
// Created by gzc on 2019-09-09.
//


#include "iostream"
#include "vector"
#include "stack"

using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* prehead = new ListNode(-1);
        ListNode* prev = prehead;
        while(l1 != NULL && l2 != NULL) {
            if(l1->val <= l2->val) {
                prev->next = l1;
                l1 = l1->next;
            } else {
                prev->next = l2;
                l2 = l2->next;
            }
            prev = prev->next;
        }
        prev->next = l1 != NULL ? l1 : l2;

        return prehead->next;
    }
};

ListNode * Creat_Link()
{
    ListNode *head=NULL,*s,*r;
    int n;
    cin>>n;
    while(n!=-1)
    {
        s=new ListNode(n);
        if(head==NULL)
            head=s;
        else
            r->next=s;
        r=s;
        cin>>n;
    }
    r->next=NULL;
    return head;
}

int main()
{
    ListNode *p1,*p2,*result,*end;
    cout<<"input the first"<<endl;
    p1=Creat_Link();
    p2=Creat_Link();
    vector <int> a(10);
    Solution s;
    result=s.mergeTwoLists(p1,p2);
    while(result!=nullptr){
        cout<<result->val<<endl;
        end=result;
        result=result->next;
    }


    return 0;
}