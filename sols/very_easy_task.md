## Analysis

Monotonic function $f(t) = T$, means if can print $n$ copies with $t$ seconds. We can use greedy strategy to compute the number copies printed in $t$ seconds.

* Print another copy with the printer that has the smaller printing time
* Print more copies by using two printers 


## Code

```c++
#include <bits/stdc++.h>
using namespace std;

int N, X, Y;

// can print n copies within t seconds
bool f(int t) {
    int time_another_copy = min(X, Y);
    if (t < time_another_copy) return false;
    int remaining_time = t - time_another_copy;
    return 1 + remaining_time / X + remaining_time / Y >= N;
}

int main() {
    cin >> N >> X >> Y;

    // Invariant: f(l) = F, f(r) = T
    // the upper bound of time needed is use the printer with smaller printing time to print N copies.
    int l = 0, r = min(X, Y) * N;
    while (l < r - 1) {
        int m = l + (r - l) / 2;
        if (f(m)) {
            r = m;
        } else {
            l = m;
        }
    }
    cout << r << "\n";
    return 0;
}
```