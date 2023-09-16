/*
1. connected componect
2. visit all nodes in graph
3. not too far, big
BFS
*/


#include <iostream>
#include <queue>
#include <vector>

using namespace std;
#define MAX 26

int n, cnt = 0;
string arr[MAX];
bool visited[MAX][MAX] = {0,};
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
vector<int> result;
queue<pair<int, int>> q;


void bfs(int x, int y) {
    q.push({x, y});
    visited[x][y] = true;
    cnt++;

    while(!q.empty()){
        int cx = q.front().first;
        int cy = q.front().second;
        q.pop();

        for(int i=0;i<4;i++){
            int nx= cx + dx[i];
            int ny= cy + dy[i];
            if(0<=nx && 0<=ny && nx<n && ny<n && visited[nx][ny]==false && arr[nx][ny]=='1') {
                q.push({nx, ny});
                visited[nx][ny] = true;
                cnt++;
            }
        }
    }
}

int main(void) {
    cin >> n;

    for(int i=0;i<n;i++) {
        cin >> arr[i];
    }

    for(int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
            if(arr[i][j]=='1' && visited[i][j]==false) {
                cnt = 0;
                bfs(i, j);
                result.push_back(cnt);
            }
        }
    }

    sort(result.begin(), result.end());

    cout << result.size() << "\n";
    for (int i=0;i<result.size();i++) {
        cout << result[i] << "\n";
    }
}