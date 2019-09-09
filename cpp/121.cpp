//
// Created by gzc on 2019-08-26.
//
#include "iostream"
#include "vector"
#include "algorithm"
using namespace std;
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max1=0;

        if (prices.empty()){
            return 0;
        }
        int min1=prices[0];
        for (int i=0;i<prices.size();i++){
            min1=min(min1,prices[i]);
            max1=max(max1,prices[i]-min1);
        }
        return max1;
    }
};


int main(){
    vector <int> a;
//    a.push_back(7);
//    a.push_back(1);
//    a.push_back(5);
//    a.push_back(3);
//    a.push_back(6);
//    a.push_back(4);

    Solution s;

    cout<<s.maxProfit(a);


}