## Analysis

Let's start from a simple case, only count for Jerseys(3). To leverage prefix sum for counting, we need to convert the input as 0 or 1, then the sum is the count.

Sample input:

$$
[2, 1, 1, 3, 2, 1]
$$

Convert the input only for Jerseys(3):

$$
[0, 0, 0, 1, 0, 0]
$$

Prefix sum for Jerseys(3):

$$
[0, 0, 0, 1, 1, 1]
$$

Repeat the same thing for other two breed ID types.


## Code

```c++
#include <bits/stdc++.h>
using namespace std;

int N, Q;
vector<vector<int>> P;

int main() {
    freopen("bcount.in", "r", stdin);
    freopen("bcount.out", "w", stdout);
    cin >> N >> Q;
    P.resize(4);
    P.assign(4, vector<int>(N + 1));

    int breed_id;
    for (int i = 1; i <= N; ++i) {
        cin >> breed_id;
        for (int k = 1; k <= 3; ++k) {
            if (k == breed_id) {
                P[breed_id][i] = P[breed_id][i - 1] + 1;
            } else {
                P[k][i] = P[k][i - 1];
            }
        }
    }
    int l, r;
    for (int i = 0; i < Q; ++i) {
        cin >> l >> r;
        for (int k = 1; k <= 3; ++k) {
            // no trailing spaces.
            if (k >= 2) cout << " ";
            cout << P[k][r] - P[k][l - 1];
        }
        cout << "\n";
    }
    return 0;
}
```