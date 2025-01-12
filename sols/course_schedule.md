## Analysis

Standard topological sorting problem. There are two ways for topological sorting.

* DFS
* Kahn's algorithm

Also topological sorting definition is useful to help to check if the graph has cycle, please see the `has_cycle` function in the DFS implementation.

## DFS

```c++
#include <bits/stdc++.h>
using namespace std;

int N, M;
vector<vector<int>> adj;
vector<bool> visited;
vector<int> ord;

void dfs(int cur) {
    visited[cur] = true;
    for (const auto nb: adj[cur]) {
        if (!visited[nb]) {
            dfs(nb);
        }
    }
    ord.push_back(cur);
}

// This cycle detection is based on the topological sorting definition.
// i.e. for all edge, we should have ord[from] < ord[to]
bool has_cycle() {
    // check any cycle, build a mapping between node -> order
    vector<int> ind(N);
    for (int i = 0; i < N; ++i) ind[ord[i]] = i;

    // check all edges if ind[from] < ind[to]
    for (int i = 0; i < N; ++i) {
        for (const auto nb: adj[i]) {
            int from = i, to = nb;
            if (ind[from] >= ind[to]) {
                return true;
            }
        }
    }
    return false;
}

int main() {
    cin >> N >> M;
    adj.resize(N);
    visited.resize(N);
    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        // course a is before course b, add an edge from a to b.
        adj[a].push_back(b);
    }

    for (int i = 0; i < N; ++i) {
        if (!visited[i]) {
            dfs(i);
        }
    }

    reverse(ord.begin(), ord.end());

    if (has_cycle()) {
        cout << "IMPOSSIBLE\n";
    } else {
        for (int i = 0; i < N; ++i) {
            if (i > 0) cout << " ";
            cout << ord[i] + 1;
        }
        cout << "\n";
    }
    return 0;
}
```

## Kahn's Algorithm

```c++
#include <bits/stdc++.h>
using namespace std;

int N, M;
vector<vector<int>> adj;
// in-degree for nodes
vector<int> in;
vector<int> ord;

// run Kahn's algorithm to find a topological sorting order
// return false if no order (i.e. has cycle)
// return true if there is an order, the result is in `ord`
bool kahn() {
    queue<int> Q;
    // put all nodes that have zero in-degree to queue
    for (int i = 0; i < N; ++i)
        if (in[i] == 0) Q.push(i);
    while (!Q.empty()) {
        int cur = Q.front();
        Q.pop();
        ord.push_back(cur);
        for (const auto nb: adj[cur]) {
            // decrement in-degree of all neighbors
            // and put those that have 0 in-degree to Q.
            --in[nb];
            if (in[nb] == 0) Q.push(nb);
        }
    }
    return ord.size() == N;
}

int main() {
    cin >> N >> M;
    adj.resize(N);
    in.resize(N);
    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        // course a is before course b, add an edge from a to b.
        adj[a].push_back(b);
        // compute in-degree
        in[b]++;
    }
    if (!kahn()) {
        cout << "IMPOSSIBLE\n";
    } else {
        for (int i = 0; i < N; ++i) {
            if (i > 0) cout << " ";
            cout << ord[i] + 1;
        }
        cout << "\n";
    }

    return 0;
}
```