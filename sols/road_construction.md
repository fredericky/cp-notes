## Analysis

Quick summary of the problem:

* `N` cities and initially no roads between them
* Every day a new road will be constructed, there will be a total of `M` roads
* A component is a group of cities where there is a route between any two cities using roads
* Find the number of components and the size of the largest component for each day

Standard DSU problem. Please refer to the code and inline comments.

## Code

```c++
#include <bits/stdc++.h>
using namespace std;

struct DSU {
    // p[i] = j: i points j, i.e. i's parent is j
    // in each group, p[root] is a negative number, its absolute value is
    // the size of group
    vector<int> p;
    void init(int N) {
        p.resize(N);
        p.assign(N, -1);
    }
    // find the root of x, the root is the representative of the group
    int find(int x) {
        // path compression
        return p[x] < 0 ? x : p[x] = find(p[x]);
    }
    bool unite(int x, int y) {
        x = find(x), y = find(y);
        // x and y already belong to the same group
        if (x == y) return false;
        // union by rank, always merge smaller group to larger group
        int x_size = -p[x], y_size = -p[y];
        if (x_size < y_size) swap(x, y);
        // merge the group (y) to the group (x):
        // update the group size
        // update the parent of y
        p[x] += p[y];
        p[y] = x;
        return true;
    }

    int size(int x) {
        return -p[find(x)];
    }
};

int N, M;

int main() {
    cin >> N >> M;
    DSU dsu;
    dsu.init(N);
    int groups = N, max_group_size = 1;
    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        if (dsu.unite(a, b)) {
            --groups;
            max_group_size = max(max_group_size, dsu.size(a));
        }
        cout << groups << " " << max_group_size << "\n";
    }
    return 0;
}
```