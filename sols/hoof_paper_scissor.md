## Analysis

Since Bessie only switches at most once, the counting can be divided as two halves. Take the first half as example. For the first half, we need to query the number of wins by two things:

* the first $X$ games
* gesture 

 We can use 3 prefix sums for answering the query, one gesture each. 

 Sample input:

 $$
 P, P, H, P, S
 $$

 Results if Bessies uses the gesture for all games

 * $H$ - $[0, 0, 0, 0, 1]$
 * $S$ - $[1, 1, 0, 1, 0]$
 * $P$ - $[0, 0, 1, 0, 0]$

The prefix sum:
 * $H$ - $[0, 0, 0, 0, 1]$
 * $S$ - $[1, 2, 2, 3, 3]$
 * $P$ - $[0, 0, 1, 1, 1]$


Similiarly, we can use the above 3 prefix sum to query the number of wins for the second half
* the last $N-X$ games
* gesture

There are N ways to separate the N games as two halves. For each way, we need to compute the max of two halves. The final answer is the max of N ways.


## Code

```c++
#include <bits/stdc++.h>
using namespace std;

int N;
vector<int> H, P, S;

int main() {
    freopen("hps.in", "r", stdin);
    freopen("hps.out", "w", stdout);
    cin >> N;
    H.resize(N + 1);
    P.resize(N + 1);
    S.resize(N + 1);
    for (int i = 1; i <= N; ++i) {
        char c;
        cin >> c;
        if (c == 'H') P[i]++;
        else if (c == 'P')
            S[i]++;
        else if (c == 'S')
            H[i]++;
        H[i] += H[i - 1];
        P[i] += P[i - 1];
        S[i] += S[i - 1];
    }
    int max_wins = 0;
    for (int i = 1; i <= N; ++i) {
        // first i games
        int first = max({H[i], P[i], S[i]});
        // rest of N-i games
        int second = max({H[N] - H[i], P[N] - P[i], S[N] - S[i]});
        max_wins = max(max_wins, first + second);
    }
    cout << max_wins << "\n";
    return 0;
}
```