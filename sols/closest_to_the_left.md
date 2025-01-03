## Analysis

The problem is to find a max $i$, where $A[i] \leq x $. 

* Monotonicity: if $A[i] \leq x $, then for all  $j \leq i$, $A[j] \leq x $

Like [Angry Cows](./angry_cows.html), the function $f$ is to check if the given element is less than or equal to $x$


## Code

```c++
#include <bits/stdc++.h>
using namespace std;

int N, K;
vector<int> A;

int main() {
    cin >> N >> K;
    A.resize(N);
    for (auto &x: A) cin >> x;

    for (int i = 0; i < K; ++i) {
        // invariant: A[l] <= x, A[r] > x
        int x;
        cin >> x;
        // add one element to the beginning and the last, to ensure
        // A[l] <= x and A[r] > x
        int l = -1, r = N;
        while (l < r - 1) {
            int m = l + (r - l) / 2;
            if (A[m] <= x) {
                l = m;
            } else {
                r = m;
            }
        }
        // +1 to remove the impact of 1st fake element.
        cout << l + 1 << "\n";
    }
    return 0;
}
```