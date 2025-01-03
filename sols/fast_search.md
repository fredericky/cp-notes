## Analysis

We can leverage **upper_bound** and **lower_bound** in STL to solve this problem.

* **upper_bound(x)**: return the position of the first element that is greater than $x$
* **lower_bound(x)**: retutnr the position of the first element that is greater than or equal to $x$

## Code

```c++
#include <bits/stdc++.h>
using namespace std;

int N, K;
vector<int> A;

int main() {
    cin >> N;
    A.resize(N);
    for (auto &x: A) cin >> x;
    sort(A.begin(), A.end());

    cin >> K;
    for (int i = 0; i < K; ++i) {
        int L, R;
        cin >> L >> R;
        auto left = lower_bound(A.begin(), A.end(), L);
        if (left == A.end()) {
            // all elements are less than L
            cout << 0 << " ";
        } else {
            auto right = upper_bound(A.begin(), A.end(), R);
            cout << right - left << " ";
        }
    }
    cout << "\n";
    return 0;
}
```