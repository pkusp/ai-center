# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: bytedance03.py
@time: 2018/9/9 上午11:13

这一行开始写关于本文件的说明与解释
"""


class Solution {
public vector < string > restoreIpAddresses(string & s) {
// Write your code here
int n = s.length();
vector < string > buf;
vector < string > result;
visit(s, 1, 0, n, buf, result);


return result;
}
private
void
visit(string & s, int
index, int
begin, int
n, vector < string > & buf, vector < string > & result)
{
if (begin >= n | | index > 4)
    {
return;
}

if (index == 4)
{
if (n - begin > 3)
    {
return;
}
string
temp = s.substr(begin);
if (n - begin < 3 | | temp <= "255")
{
if ((n - begin) > 1 & & s[begin] == '0')
    {
return;
}
buf.push_back(temp);
string
a;
for (int i = 0; i < 3; i++)
{
a += buf[i] + ".";
}
a += buf[3];
result.push_back(a);
buf.pop_back();
}

return;
}

for (int len = 1; len <= 3; len++)
{
    if (len == 1)
        {
            buf.push_back(s.substr(begin, len));
        visit(s, index + 1, begin + len, n, buf, result);
        buf.pop_back();
        }
        else if (len == 2)
            {
            if (s[begin] == '0')
            {
        continue;
        }
        else
        {
        string
        temp = s.substr(begin, 2);
        buf.push_back(temp);
        visit(s, index + 1, begin + len, n, buf, result);
        buf.pop_back();
    }
    }
    else
    {
    if (s[begin] == '0')
    {
    continue;
    }
    else
    {
    string
    temp = s.substr(begin, 3);
    if (temp <= "255")
        {
            buf.push_back(temp);
        visit(s, index + 1, begin + len, n, buf, result);
        buf.pop_back();
        }
        }
        }
        }
        }
