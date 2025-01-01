## Analysis

This problem is to compute prefix sum in 2D array. First of all, we need to compute the $P[r][c]$ - the sum of all elements from $(0,0)$ to $(r,c)$.

$$
P[r][c] = forest[r][c] + P[r-1][c] + P[r][c-1] - P[r-1][c-1] 
$$

Next, we can compute the sum of elements enclosed by a rectangle by using the above prefix sum.

Rectangle is defined as 

* rows from $r_1$ to $r_2$
* cols from $c_1$ to $c_2$

The answer is

$$
S_{rectangle} = P[r_2][c_2] - P[r_1-1][c_2] - P[r_2][c_1-1] + P[r_1-1][c_1-1]
$$

## Code

```c++
#include <bits/stdc++.h>
using namespace std;

int N, Q;

int main() {
    cin >> N >> Q;
    vector<vector<int>> forest(N + 1, vector<int>(N + 1));
    vector<vector<int>> P(N + 1, vector<int>(N + 1));

    char ch;
    for (int r = 1; r <= N; ++r) {
        for (int c = 1; c <= N; ++c) {
            cin >> ch;
            if (ch == '*') {
                forest[r][c] = 1;
            }
        }
    }

    for (int r = 1; r <= N; ++r) {
        for (int c = 1; c <= N; ++c) {
            P[r][c] = forest[r][c] + P[r - 1][c] + P[r][c - 1] - P[r - 1][c - 1];
        }
    }

    int x1, x2, y1, y2;
    int r1, r2, c1, c2;
    for (int k = 0; k < Q; ++k) {
        cin >> y1 >> x1 >> y2 >> x2;
        // translate them to row and col
        r1 = y1;
        r2 = y2;
        c1 = x1;
        c2 = x2;
        int S = P[r2][c2] - P[r1 - 1][c2] - P[r2][c1 - 1] + P[r1 - 1][c1 - 1];
        cout << S << "\n";
    }
    return 0;
}
```


