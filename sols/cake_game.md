## Analysis

Let's start from the simple cases.

* N = 2: Bessie: $a_1$ + $a_2$, Elsie: 0
* N = 4: Bessie takes two in the middle, Elsie takes the rest

From the above, we should have observations below

* Bessie takes $\frac{N}{2}$ turns, Elsie takes $\frac{N}{2}-1$ turns
* $\frac{N}{2}-1$ cakes taken by Elsie are leftmost and rightmost cakes, i.e. prefix and suffix of the cakes array

Next, we should go deep on how Bessie impacts the Elsie cakes. Let's make it simple. If without Bessie, Elsie takes either prefix or suffix or both. In general, assume the prefix length is $L_1$ and the suffix length is $L_2$, the optional answer for Elsie is

$$
X = max(\sum_{i=1}^{L1} a_i + \sum_{i=N-L_2+1}^{N} a_i)
$$

Let's have Bessie into the play, how does she impact Elsie's cakes? The answer is Bessie can help Elsie take more or equal but can't make Elsie take less than X, i.e. if both play optimally, Elsie takes $X$ and Bessie takes the rest.

To compute $X$, we can use prefix sum to have linear time complexity. 


## Code

```c++
#include <bits/stdc++.h>
using namespace std;

using LL = long long;

vector<LL> cakes;
int N;

void solve() {
    vector<LL> prefix(N + 1);
    for (int i = 1; i <= N; ++i) {
        prefix[i] = prefix[i - 1] + cakes[i];
    }
    vector<LL> suffix(N + 1);
    for (int i = N - 1; i >= 0; --i) {
        suffix[i] = suffix[i + 1] + cakes[i + 1];
    }
    LL elsie = 0;
    for (int prefix_len = 0; prefix_len <= N / 2 - 1; ++prefix_len) {
        int suffix_len = N / 2 - 1 - prefix_len;
        elsie = max(elsie, prefix[prefix_len] + suffix[N - suffix_len]);
    }
    LL bessie = prefix[N] - elsie;
    cout << bessie << " " << elsie << "\n";
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        cin >> N;
        cakes.resize(N + 1);
        for (int i = 1; i <= N; ++i) cin >> cakes[i];
        solve();
        cakes.clear();
    }
    return 0;
}
```