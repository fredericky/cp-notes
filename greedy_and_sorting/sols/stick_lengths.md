## Analysis

The given elements can be considered as the coordinates on *X* axis. The problem is reframed as to find a coordinate such that the sum of the distances between the choice and other coordinates is minimized. Obviously, the choice is the median.

## Code

```c++
#include <bits/stdc++.h>
using namespace std;

using LL = long long;

int main() {
    int N;
    cin >> N;
    vector<LL> P(N);
    for (auto &x: P) cin >> x;
    sort(P.begin(), P.end());
    LL median = P[N / 2];
    LL total_cost = 0;
    for (const auto x: P) {
        total_cost += abs(x - median);
    }
    cout << total_cost << "\n";
    return 0;
}
```

