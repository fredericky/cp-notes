## Analysis

Two DFS searches

* Start from an arbitrary node `a` and find the furthest node `b` - `b` is actually one of diameter ends.
* Start from node `b` and find the furthest node `c` - `c` is actually another diameter end
* Diameter is the distance between node `b` and `c`

## Code

```c++
#include <bits/stdc++.h>
using namespace std;

int N;
vector<vector<int>> adj;

int max_dist;

int node;

void dfs(int cur, int parent, int d) {
    for (const auto nb: adj[cur]) {
        if (nb != parent) {
            dfs(nb, cur, d + 1);
        }
    }
    if (d > max_dist) {
        max_dist = d;
        node = cur;
    }
}

int main() {
    cin >> N;
    adj.resize(N);

    for (int i = 0; i < N - 1; ++i) {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    max_dist = 0;
    dfs(0, -1, 0);

    max_dist = 0;
    dfs(node, -1, 0);

    cout << max_dist << "\n";

    return 0;
}
```