## Analysis

Quick summary of the problem:

* Given a graph consisting `N` nodes and `M` edges
* Some edges are directed, others are undirected
* The question is to ask if possible to assign directions to those undirected edges and the resulting graph has no cycle

We can look at the subgraph that has directed edges and related nodes first. If that subgraph has cycle, then print `NO`. If that subgraph has no cycle, we should print `YES`, since 

* For all edges in the subgraph, we have `ord[from] < ord[to]`
* For all undirected edges, we can always find an appropriate order for the nodes that are not in the subgraph.

## Code

```c++
#include <bits/stdc++.h>
using namespace std;

int N, M;
vector<vector<int>> adj;
vector<pair<int, int>> all_edges;
vector<int> in;
vector<int> ord;

void solve() {
    cin >> N >> M;
    adj.resize(N);
    in.resize(N);
    for (int i = 0; i < M; ++i) {
        int t, a, b;
        cin >> t >> a >> b;
        a--;
        b--;
        // directed edge
        if (t == 1) {
            adj[a].push_back(b);
            in[b]++;
        }
        all_edges.push_back({a, b});
    }
    // kahn's algorithm.
    queue<int> Q;
    for (int i = 0; i < N; ++i)
        if (in[i] == 0) Q.push(i);
    while (!Q.empty()) {
        int cur = Q.front();
        Q.pop();
        ord.push_back(cur);
        for (const auto nb: adj[cur]) {
            if (--in[nb] == 0) Q.push(nb);
        }
    }
    if (ord.size() != N) {
        cout << "NO\n";
    } else {
        cout << "YES\n";
        // build a mapping between node and order
        vector<int> ind(N);
        for (int i = 0; i < N; ++i) ind[ord[i]] = i;
        for (const auto &[from, to]: all_edges) {
            if (ind[from] < ind[to]) {
                cout << from + 1 << " " << to + 1 << "\n";
            } else {
                cout << to + 1 << " " << from + 1 << "\n";
            }
        }
    }
}

void clean_up() {
    adj.clear();
    all_edges.clear();
    in.clear();
    ord.clear();
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        solve();
        clean_up();
    }
    return 0;
}
```