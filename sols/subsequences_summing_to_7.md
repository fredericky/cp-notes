## Analysis

This problem is similar to [Subarray Divisibility](./subarray_divisibility.html). Instead of counting the eligible subarrays, this problem is asking the length of the longest subarray. Therefore, we need to keep track of the first position for each remainder to compute the longest eligible subarray length. Also, we don't have to consider the negative sum for this problem.

## Code

```c++
#include <bits/stdc++.h>
using namespace std;

using LL = long long;

int N;
// key: reminder, value: 1st position
map<int, int> first;

int main() {
    freopen("div7.in", "r", stdin);
    freopen("div7.out", "w", stdout);
    cin >> N;
    first[0] = 0;
    LL sum = 0, x = 0;
    int max_length = 0;
    for (int i = 0; i < N; ++i) {
        cin >> x;
        sum += x;
        int r = sum % 7;
        if (first.count(r)) {
            max_length = max(max_length, i - first[r]);
        } else {
            first[r] = i;
        }
    }
    cout << max_length << "\n";
    return 0;
}
```