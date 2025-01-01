## Analysis

The subarray sum 

$$
sum(i, j) = P_j - P_{i-1} = x
$$
i.e. 
$$
P_j-x=P_{i-1}
$$

To count the subarrays with the sum as $x$, we can use a map to count the occurrences of $P_{i-1}$, and for each $P_j$ to see the number of occurrences of $P_j-x$. These two things can be done in one pass.

## Code

```c++
#include <bits/stdc++.h>
using namespace std;

using LL = long long;

int N, x;
map<LL, LL> counters;

int main() {
    cin >> N >> x;
    vector<LL> P(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> P[i];
        P[i] += P[i - 1];
    }
    LL result = 0;
    counters[0] = 1;
    for (int i = 1; i <= N; ++i) {
        if (counters.count(P[i] - x)) {
            result += counters[P[i] - x];
        }
        counters[P[i]]++;
    }
    cout << result << "\n";
    return 0;
}
```