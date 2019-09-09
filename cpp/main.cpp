#include <iostream>
#include "stdio.h"
using namespace std;
//void GetMoney(char * p){
//    p=(char* )malloc (100);
//}
//void test(){
//    char * str= NULL;
//    GetMoney(str);
//    strcpy(str,"Hello");
//    strcat(str+2,"Bigo");
//    printf(str);
//}

class Myclass{
public:
    Myclass(int i=0)
    {
        cout<<i;
    }
    Myclass(const Myclass &x){
        cout<<2;
    }
    Myclass &operator=(const Myclass & x){
        cout<<3;
        return *this;
    }
    ~Myclass(){
        cout<<4;

    }
};


int main() {
//    test();
    Myclass obj1(1),obj2(2);
    Myclass obj3=obj1;
    return 0;
}