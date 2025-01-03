## Analysis

Monotonicity: if a square with side length $X$ can hold the given $n$ rectangles, then any squares that the side is greater than $X$ can hold them too.

Now, the work is to implement a function $f$ to check if a square with side $X$ can hold $n$ rectangles. Since the rectangles can not be rotated, we can count the number of rectangles by considering both directions of the square

$$
\frac{X}{w} \times \frac{X}{h}
$$

## Code

```c++
#include <bits/stdc++.h>
using namespace std;

using LL = long long;

LL W, H, N;

bool f(LL X) {
    return (X / W) * (X / H) >= N;
}

int main() {
    cin >> W >> H >> N;

    // invariant: f(l) = F, f(r) = T
    LL l = 0, r = 1;
    // we can leverage f to get the max r.
    while (!f(r)) r *= 2;
    while (l < r - 1) {
        LL m = l + (r - l) / 2;
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