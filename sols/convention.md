## Analysis

Quick summary:

* $N$ cows, cow $i$ arrrives at time $t_i$
* $M$ buses
* Each bus can hold up to $C$ cows
* A cow's waiting time: departure time $-$ arrival time

Question: the smallest possible value of maximum waiting time.

Monotonic function: $f(t) = T$, means we can use at most $M$ buses to accommodate $N$ cows and maximum waiting time of all cows is $t$. Obviously, the sequence of applying f to all possible $t$ is like $F, F, F, T, T, T$. The answer is the first $t$ that has $f(t) = T$.

We can use greedy strategy to compute the least buses (denote as $B$) to accommodate $N$ cows, return true if $B \leq M$. 

* Take as many cows as possible for each bus while keeping the bus capacity $C$ and maximum waiting time $t$

## Code

```c++
#include <bits/stdc++.h>
using namespace std;

int N, M, C;

vector<int> arrivals;

bool f(int max_waiting_time) {
    int B = 1;
    int left_most = 0, cur = 1;
    while (cur < N) {
        bool exceed_max_waiting_time = arrivals[cur] - arrivals[left_most] > max_waiting_time;
        bool exceed_bus_capacity = cur - left_most + 1 > C;
        if (exceed_max_waiting_time || exceed_bus_capacity) {
            left_most = cur;
            B++;
        }
        ++cur;
    }
    return B <= M;
}

int main() {
    freopen("convention.in", "r", stdin);
    freopen("convention.out", "w", stdout);
    cin >> N >> M >> C;

    arrivals.resize(N);
    for (auto &arrival: arrivals) cin >> arrival;
    sort(arrivals.begin(), arrivals.end());

    // invariant: f(l) = F, f(r) = T
    int l = 0, r = 1e9;
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