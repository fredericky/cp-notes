## Analysis

This problem is to find the cycle in the undirected graph. The algorithm for the directed graph works for undirected graph as well - [Round Trip II](./round_trip_ii.html).

Alternatively, we can use 2 state for cycle detection on the undirected graph.

## Code

```c++
#include <bits/stdc++.h>
using namespace std;

int N, M;

vector<vector<int>> adj;
vector<bool> visited;
vector<int> parent;

int cycle_start, cycle_end;

// return true if has cycle
bool dfs(int cur, int p) {
    visited[cur] = true;
    for (const auto nb: adj[cur]) {
        if (nb == p) continue;
        if (!visited[nb]) {
            parent[nb] = cur;
            if (dfs(nb, cur)) {
                return true;
            }
        } else {
            // found a cycle
            cycle_start = nb;
            cycle_end = cur;
            return true;
        }
    }
    return false;
}

int main() {
    cin >> N >> M;
    adj.resize(N);
    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        u--;
        v--;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    cycle_start = cycle_end = -1;
    visited.resize(N);
    parent.resize(N);

    bool has_cycle = false;
    for (int i = 0; i < N; ++i) {
        if (visited[i] == 0 && dfs(i, -1)) {
            has_cycle = true;
            break;
        }
    }
    if (has_cycle) {
        vector<int> cycle;
        cycle.push_back(cycle_start);
        for (int v = cycle_end; v != cycle_start; v = parent[v]) {
            cycle.push_back(v);
        }
        cycle.push_back(cycle_start);
        reverse(cycle.begin(), cycle.end());
        cout << cycle.size() << "\n";
        for (const auto node: cycle) {
            cout << node + 1 << " ";
        }
    } else {
        cout << "IMPOSSIBLE\n";
    }
    return 0;
}
```