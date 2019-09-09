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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *head1= head;
        while(head->next!= nullptr){
            if (head->val==head->next->val){

                head=head->next->next;
            }
        }
        return head1;
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
    //p2=Creat_Link();
    vector <int> a(10);
    Solution s;
    result=s.deleteDuplicates(p1);
    while(result!=nullptr){
        cout<<result->val<<endl;
        end=result;
        result=result->next;
    }


    return 0;
}