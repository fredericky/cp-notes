## Analysis

Since the problem is related to subarray sum, it worth trying prefix sum. Let's look at prefix sum definition.

$$
P[i] = \sum_{k=0}^{i} a_k
$$

$$
sum(i, j) = \sum_{k=i}^{j} a_k = P[j]-P[i-1]
$$

When the subarray sum $sum(i, j)$ is divisible by $n$, it means 

$$
(P[j]-P[i-1]) \% n = 0
$$

This implies $P[j] \% n$ and $P[i-1] \% n$ should be identical, so remainders can be canceled out. 

Let's look at the sample input

$$
[3, 1, 2, 7, 4]
$$

The corresponding prefix sum is 

$$
[3, 4, 6, 13, 17]
$$

The remainders after being divided by $n$ (which is 5)

$$
[3, 4, 1, 3, 2]
$$

There are two $3$, meaning the subarray $[1,2,7]$ is divisible by 5.

The algorithm is to count the number of prefix sum that have the same remainder as below

* $r = 0$, $c_0$
* $r = 1$, $c_1$
* ...
* $r = n-1$, $c_{n-1}$

For each non-zero $c_i$, it can contribute ${c_i \choose 2} = \frac{c_i * (c_i-1)}{2}$ to the total. $c_0$ is special, since $c_0=1$ can contribute to the total as well.

## Code

```c++
#include <bits/stdc++.h>
using namespace std;

using LL = long long;

int N;
vector<LL> counters;

int main() {
    cin >> N;
    counters.resize(N - 1);
    // handle c_0 = 0.
    counters[0] = 1;
    LL sum = 0, x = 0;
    for (int i = 0; i < N; ++i) {
        cin >> x;
        sum += x;
        // sum could be negative
        int r = (sum % N + N) % N;
        counters[r]++;
    }
    LL total = 0;
    for (const auto &c: counters) {
        total += c * (c - 1) / 2;
    }
    cout << total << "\n";
    return 0;
}
```