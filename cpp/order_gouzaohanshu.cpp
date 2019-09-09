#include <iostream>
#include <string>
using namespace std;
/**
 * 定义类：Student
 * 数据成员：m_strName
 * 无参构造函数：Student()
 * 有参构造函数：Student(string _name)
 * 拷贝构造函数：Student(const Student& stu)
 * 析构函数：~Student()
 * 数据成员函数：setName(string _name)、getName()
 */
class Student
{
public:
    Student() {
        m_strName = "jack";
        cout<<"Student()"<<endl;
    }
    Student(string _name) {
        m_strName = _name;
        cout<<"Student(string _name)"<<endl;
    }
    Student(const Student& stu) {
        cout<<"Student(const Student& stu)"<<endl;
    }
    ~Student() {
        cout<<"~Student()"<<endl;
    }
    void setName(string _name) {
        m_strName = _name;
    }
    string getName() {
        return m_strName;
    }
private:
    string m_strName;
};


int main(void)
{

    Student *stu = new Student("小李");

    stu->setName("慕课网");

    cout<<stu->getName()<<endl;
    delete stu;
    stu = NULL;
    return 0;
}//
// Created by gzc on 2019-08-22.
//

