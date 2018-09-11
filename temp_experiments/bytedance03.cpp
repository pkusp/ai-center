//class Solution{
//public:
//    vector<string> restoreIP(string s){
//        vector<string> res;
//        restore(s,4,"",res);
//        return res;
//    }
//    void restore(string s, int k, string out, vector<string> &res){
//        if(k==0){
//            if(s.empty())
//                res.push_back(out);
//            }
//        else{
//            for(int i=1; i<=3;++i){
//                if(s.size()>=i&&isValid(s.substr(0,i))){
//                    if(k==1)
//                        restore(s.substr(i),k-1,out+s.substr(o,i),res);
//                    else
//                        restore(s.substr(i),k-1,out+s.substr(0,i)+".",res);
//                }
//            }
//        }
//    }
//    bool isValid(string s){
//        if(s.empty()||s.size()>3||(s.size()>1&&s[0]=='0'))
//            return false;
//        int res = atoi(s.c_str());
//        return res<=255 && res>= 0;
//    }
//}
#include <iostream>
#include<vector>
using namespace std;

bool isValid(string s){
    if(s.empty()||s.size()>3||(s.size()>1&&s[0]=='0'))
        return false;
    int res = atoi(s.c_str());
    return res<=255 && res>= 0;
}
void restore(string s, int k, string out, vector<string> &res){
    if(k==0){
        if(s.empty())
            res.push_back(out);
        }
    else{
        for(int i=1; i<=3;++i){
            if(s.size()>=i&&isValid(s.substr(0,i))){
                if(k==1)
                    restore(s.substr(i),k-1,out+s.substr(0,i),res);
                else
                    restore(s.substr(i),k-1,out+s.substr(0,i)+".",res);
            }
        }
    }
}

int restoreIP(string s){
    vector<string> res;
    restore(s,4,"",res);
    return res.size();
}

int main() {
    string s;
    cin>>s;
    vector<string> res;
    cout<<restoreIP(s)<<endl;

}