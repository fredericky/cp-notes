## Analysis

Quick summary of the problem:

* `N` sessions over the past `M` days
* Each session occurred no earlier than $S_i$
* `C` memories, each memory is represented as `(a, b, x)`, meaning session `b` happened at least `x` days after `a`
* Compute the earliest possible date of occurrence for each session

Let's build a graph first

* Node: session
* Edge: for each `(a, b, x)`, an edge is from `a` to `b` and weight is `x`

Initially, $S_i$ is the earliest date for each session. We need to consider more constraints in `C` memories by using topological sorting.

$$
S_b = max(S_b, S_a + x)
$$

## Code

```c++
#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int to, weight;
};

int N, M, C;
vector<vector<Edge>> adj;
vector<int> S;
vector<int> in;

void topo_sort() {
    queue<int> Q;
    for (int i = 0; i < N; ++i)
        if (in[i] == 0) Q.push(i);
    while (!Q.empty()) {
        int cur = Q.front();
        Q.pop();
        for (const auto &edge: adj[cur]) {
            S[edge.to] = max(S[edge.to], S[cur] + edge.weight);
            if (--in[edge.to] == 0) Q.push(edge.to);
        }
    }
}

int main() {
    freopen("timeline.in", "r", stdin);
    freopen("timeline.out", "w", stdout);
    cin >> N >> M >> C;
    adj.resize(N + 1);
    S.resize(N + 1);
    in.resize(N + 1);

    for (int i = 1; i <= N; ++i) cin >> S[i];
    for (int i = 0; i < C; ++i) {
        int a, b, x;
        cin >> a >> b >> x;
        adj[a].push_back({b, x});
        in[b]++;
    }

    topo_sort();

    for (int i = 1; i <= N; ++i) cout << S[i] << "\n";

    return 0;
}
```