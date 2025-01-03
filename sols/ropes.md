## Analysis

Assume each piece after the cut has the length $L$, the monotonicity is 

* if we can cut ropes into $K$ pieces with the length $L$, then we can do the same thing for any length that is less than $L$

We need to implement a function $f$ to check if can cut the ropes to $K$ pieces with length $L$, this is basically to look at the number of pieces for each rope and sum them up. 

The caveat of this problem is the length is a floating number, we can use `while(l < r-1)` for the binary search, since

* there are no neighboring in real numbers, e.g. 3 and 4 are adjacent, 3.1 and 3.2 are not.
* the while loop could get stuck since `m = (l+r)/2` could be either `l` or `r`.

The solution here is to repeat the search for a constant times - depending on if the result converges. Usually, 50 times is sufficient.

## Code

```c++
#include <bits/stdc++.h>
using namespace std;

int N, K;
vector<int> ropes;

bool f(double L) {
    int total = 0;
    for (const auto rope: ropes) {
        total += floor(rope / L);
    }
    return total >= K;
}

int main() {
    cin >> N >> K;
    ropes.resize(N);
    for (auto &x: ropes) cin >> x;

    // invariant: f(l) = T, f(r) = F
    double l = 0, r = 1e8;
    for (int k = 0; k < 50; ++k) {
        double m = (l + r) / 2;
        if (f(m)) {
            l = m;
        } else {
            r = m;
        }
    }
    cout << setprecision(10) << l << "\n";
    return 0;
}
```



