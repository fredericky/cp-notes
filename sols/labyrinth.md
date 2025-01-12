## Analysis

This problem is the 2D version of shortest path in an unweighted graph. Please look at [Message Route](./message_route.html) first.

## Code

```c++
// https://cses.fi/problemset/task/1193

#include <bits/stdc++.h>
using namespace std;

struct P {
    int r, c;
};

int N, M;
vector<vector<char>> grid;
vector<vector<int>> dist;
vector<vector<int>> parent;

P start, target;

int D[4][2] = {
        {1, 0},
        {-1, 0},
        {0, 1},
        {0, -1},
};

// character representation of direction, consistent with D[4][2].
char CD[4] = {'D', 'U', 'R', 'L'};

int main() {
    cin >> N >> M;
    grid.resize(N);
    grid.assign(N, vector<char>(M, '?'));
    dist.resize(N);
    dist.assign(N, vector<int>(M, -1));
    parent.resize(N);
    parent.assign(N, vector<int>(M, -1));

    for (int r = 0; r < N; ++r) {
        for (int c = 0; c < M; ++c) {
            cin >> grid[r][c];
            if (grid[r][c] == 'A') start = {r, c};
            else if (grid[r][c] == 'B')
                target = {r, c};
        }
    }

    dist[start.r][start.c] = 0;
    queue<P> Q;
    Q.push(start);

    while (!Q.empty()) {
        P cur = Q.front();
        Q.pop();
        for (int k = 0; k < 4; ++k) {
            int nr = cur.r + D[k][0], nc = cur.c + D[k][1];
            // out of grid
            if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
            // hit th wall
            if (grid[nr][nc] == '#') continue;
            // visited before
            if (dist[nr][nc] != -1) continue;

            dist[nr][nc] = dist[cur.r][cur.c] + 1;
            parent[nr][nc] = k;
            Q.push({nr, nc});
        }
    }

    if (dist[target.r][target.c] != -1) {
        cout << "YES\n";
        cout << dist[target.r][target.c] << "\n";
        vector<char> path;
        P p = target;
        while (p.r != start.r || p.c != start.c) {
            int k = parent[p.r][p.c];
            path.push_back(CD[k]);
            // undo the move
            p.r -= D[k][0];
            p.c -= D[k][1];
        }
        reverse(path.begin(), path.end());
        for (const auto d: path) cout << d;
        cout << "\n";
    } else {
        cout << "NO\n";
    }
    return 0;
}
```