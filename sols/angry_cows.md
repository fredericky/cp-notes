## Analysis

We can approach this problem by trying to understand how $R$ impacts the task. As *R* is increased, it's more likely to have less cows to complete the task. Especially, if $C$ ($C$ <= $K$) cows can complete the task with $R1$, then the same amount of cows can complete the task with $R2$ ($R2 > R1$). This monotonicity is a perfect fit for binary search.

Let's define a function `bool f(int r)` to represent if we can use at most $K$ cows with radius $r$ to complete the task. For the radius sequence $r_1$, $r_2$, ... $r_n$ in ascending order, apply the function, we can get the sequence like $F$, $F$, $F$, $T$, $T$ ..., we would like to know the correponding $r$ of the first $T$.

The challenging part is to implement the function. This is equivalent with if we can place $C$ cows with radius *r* to complete the task, where $C$ <= $K$. We can use a greedy strategy. For a given $r$, we can minimize the cows by minimizing the overlap of areas covered by each cow. Make sure sort the hay bales locations first.


## Code

```c++
#include <bits/stdc++.h>
using namespace std;

int N, K;
vector<int> X;

bool f(int r) {
    int C = 0;
    // The left most hay bale covered by the cow.
    int left_most = 0;
    while (left_most < N) {
        C++;
        int cur = left_most + 1;
        while (cur < N && X[cur] - X[left_most] <= 2 * r) {
            cur++;
        }
        left_most = cur;
    }
    return C <= K;
}

int main() {
    freopen("angry.in", "r", stdin);
    freopen("angry.out", "w", stdout);

    cin >> N >> K;
    X.resize(N);
    for (auto &x: X) cin >> x;

    // Sort the hay bales locations for implementing f.
    sort(X.begin(), X.end());

    // invariant: f(l) = F, f(r) = T, meaning this applies to the whole life-cycle of l or r.
    // this invariant is helpful to decide
    // 1) the initial value of l and r
    // 2) how to update l or r with m
    // 3) the output is l or r
    int l = 0, r = 1e9;

    // l and r are adjacent when the loop is terminated.
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