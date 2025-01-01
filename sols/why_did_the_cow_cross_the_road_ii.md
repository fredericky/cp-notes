## Analysis

We can get an array with elements 0 and 1 - working(1), broken(0). To minimize the broken signals to repair, we need to find an subarray

* Length is $K$
* Has the largest sum $S$ (i.e. has the most working signals)

The answer is $K - S$.

## Code

```c++
#include <bits/stdc++.h>
using namespace std;

int N, K, B;
int main() {
    freopen("maxcross.in", "r", stdin);
    freopen("maxcross.out", "w", stdout);
    cin >> N >> K >> B;
    vector<int> signals(N + 1, 1);
    int id;
    for (int i = 0; i < B; ++i) {
        cin >> id;
        signals[id] = 0;
    }
    vector<int> P(N + 1);
    for (int i = 1; i <= N; ++i) {
        P[i] = P[i - 1] + signals[i];
    }
    // max_sum: number of working signals
    int max_sum = INT_MIN;
    // compute P[i+K] - P[i] = sum(i+1, i+K)
    for (int i = 0; i <= N - K; ++i) {
        max_sum = max(max_sum, P[i + K] - P[i]);
    }
    cout << K - max_sum << "\n";
    return 0;
}
```