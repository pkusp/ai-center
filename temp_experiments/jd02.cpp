#include <queue>
#include <cstring>
#include <iostream>
using namespace std;

const int N = 1001;
int color[N], graph[N][N];

bool bfs(int s, int n) {
    queue<int> q;
    q.push(s);
    color[s] = 1;
    while(!q.empty()) {
        int from = q.front();
        q.pop();
        for(int i = 1; i <= n; i++) {
            if(graph[from][i] && color[i] == -1) {
                q.push(i);
                color[i] = !color[from];
            }
            if(graph[from][i] && color[from] == color[i])
                return false;
        }
    }
    return true;
}

int main() {
    int group,n, m, a, b, i;
    memset(color, -1, sizeof(color));
    cin>>group;
    while(group--){
        cin>>n>>m;
        for(i = 0; i < m; i++) {
            cin >> a >> b;
            graph[a][b] = graph[b][a] = 1;
        }
        bool flag = false;
        for(i = 1; i <= n; i++)
            if(color[i] == -1 && !bfs(i, n)) {
                flag = true;
                break;
            }
        if(flag)
            cout << "NO" <<endl;
        else
            cout << "YES" <<endl;
    }
    return 0;

}