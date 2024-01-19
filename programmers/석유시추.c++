int row, col;
int grid[501][501];
int visited[501][501];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
int area = 0;
int check[501];
int ans[501];

void dfs(int x, int y) {
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx < 1 || ny < 1 || nx > row || ny > col) continue;
        if (visited[nx][ny] == 1) continue;
        if (grid[nx][ny] == 0) continue;

        if (check[ny] == 0)
            check[ny] = 1;

        visited[nx][ny] = 1;
        area++;
        dfs(nx, ny);
    }
}
