//
// Created by gzc on 2019-08-22.
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
    ListNode* reverseList(ListNode* head) {
        ListNode  *head2=  head;
        stack <int> a;
        while(head!=nullptr){
            a.push(head->val);
            head=head->next;
        }
//        cout<<a[-1]<<endl;
        ListNode  *head3=head2;

        for (int i=a.size();i>0;i--){
            head2->val=a.top();
            a.pop();
            head2=head2->next;
        }
        return head3;
    }
};
//
//struct ListNode {
//    int val;
//    ListNode *next;
//    ListNode(int x) : val(x), next(NULL) {}
//};
//
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
//
//ListNode *reverseList(ListNode *head) {
//    ListNode *pre = nullptr, *cur = head, *r = nullptr;
//    while (cur != nullptr) {
//        r = cur->next;
//        cur->next = pre;
//        pre = cur;
//        cur = r;
//    }
//    return pre;
//}
//
int main()
{
    ListNode *p1,*p2,*result,*end;
    cout<<"input the first"<<endl;
    p1=Creat_Link();
    vector <int> a(10);
    Solution s;
    p1=s.reverseList(p1);
    while(p1!=nullptr){
        cout<<p1->val<<endl;
        end=p1;
        p1=p1->next;
    }


    return 0;
}