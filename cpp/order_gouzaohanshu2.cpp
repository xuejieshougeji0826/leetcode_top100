//
// Created by gzc on 2019-08-22.
//

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
    Student(const Student &stu) {
        cout<<"Student(const Student &stu)"<<endl;
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
    // 通过new方式实例化对象*stu
    Student stu;
    Student stu2 = stu;
    // 更改对象的数据成员为“慕课网”
    stu.setName("慕课网");
    // 打印对象的数据成员
    cout<<stu.getName()<<endl;
    return 0;
}