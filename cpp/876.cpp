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
    ListNode* middleNode(ListNode* head) {
        ListNode *slow=head;
        ListNode *fast=head;
        while(fast!=nullptr || fast->next!=nullptr){
            slow=slow->next;
            fast=fast->next->next;
        }
        return slow;
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
    vector <int> a(10);
    Solution s;
    p1=s.middleNode(p1);
    while(p1!=nullptr){
        cout<<p1->val<<endl;
        end=p1;
        p1=p1->next;
    }


    return 0;
}