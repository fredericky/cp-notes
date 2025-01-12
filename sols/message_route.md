## Analysis

Standard problem of the shortest path in an unweighted graph. We can use BFS to solve it.

* Start from source node and visit other nodes layer by layer
* Track the distance from starting node to every other node

  * `int dist[N]`
  * `dist[0] = 0`
  * `dist[N-1]` is the answer
* To print the shortest path, we need an array 

  * `int parent[N]`
  * `parent[i] = j`, there is a path from `i` to `j`

## Code

```c++
#include <bits/stdc++.h>
using namespace std;

int N, M;
vector<vector<int>> adj;
vector<int> dist;
vector<int> parent;


int main() {
    cin >> N >> M;
    adj.resize(N);
    dist.resize(N);
    parent.resize(N);
    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    dist.assign(N, -1);
    dist[0] = 0;
    queue<int> Q;
    Q.push(0);

    while (!Q.empty()) {
        int cur = Q.front();
        Q.pop();
        for (int nb: adj[cur]) {
            if (dist[nb] == -1) {
                dist[nb] = dist[cur] + 1;
                parent[nb] = cur;
                Q.push(nb);
            }
        }
    }

    if (dist[N - 1] == -1) {
        cout << "IMPOSSIBLE\n";
    } else {
        cout << dist[N - 1] + 1 << "\n";
        vector<int> path;
        for (int x = N - 1; x != 0; x = parent[x]) {
            path.push_back(x);
        }
        path.push_back(0);
        reverse(path.begin(), path.end());
        for (const auto x: path) cout << x + 1 << " ";
    }
    return 0;
}
```