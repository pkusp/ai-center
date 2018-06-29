
//#include <stdafx.h>
#include<iostream>
#include<vector>

using namespace std;

class A
{
    //空类
};















int main(int argc, char* argv[])
{

    //int型vector
    vector<int> vecInt;

    //float型vector
    vector<float> vecFloat;

    //自定义类型，保存类A的vector
    vector<A> vecA;

    //自定义类型，保存指向类A的指针的vector
    vector<A*> vecPointA;
    cout<<"hello vector!"<<endl;
    return 0;
}
