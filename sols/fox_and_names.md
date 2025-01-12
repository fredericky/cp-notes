## Analysis

* Compare each pair of consecutive strings to determine the order for one pair of letters. For example:

    * `axcd` and `axbe`: `c` is before `b` in the modified alphabet
    * `abc` and `abcde`: the longer string has greater order
    * `aa` and `a`: invalid input and output `Impossible`

* Create an edge between the above pair of letters
* Run the topological sorting

## Code

```c++
#include <bits/stdc++.h>
using namespace std;

const int ALPHABET_SIZE = 26;

int N;
vector<string> names;
vector<vector<int>> adj;
vector<int> in;
vector<int> ord;

// return false if input is not valid, e.g. s1 = "aa", s2 = "a"
bool validate_and_add_edge(const string &s1, const string &s2) {
    int L = min(s1.length(), s2.length());
    int k = 0;
    while (k < L && s1[k] == s2[k]) k++;
    if (k < L) {
        int from = s1[k] - 'a', to = s2[k] - 'a';
        adj[from].push_back(to);
        in[to]++;
        return true;
    } else {
        return s1.length() <= s2.length();
    }
}

void topo_sort() {
    queue<int> Q;
    for (int i = 0; i < ALPHABET_SIZE; ++i)
        if (in[i] == 0) Q.push(i);
    while (!Q.empty()) {
        int cur = Q.front();
        Q.pop();
        ord.push_back(cur);
        for (const auto nb: adj[cur]) {
            if (--in[nb] == 0) Q.push(nb);
        }
    }
}


int main() {
    cin >> N;
    names.resize(N);
    adj.resize(ALPHABET_SIZE);
    in.resize(ALPHABET_SIZE);
    for (auto &name: names) cin >> name;
    for (int i = 1; i < N; ++i) {
        if (!validate_and_add_edge(names[i - 1], names[i])) {
            cout << "Impossible\n";
            return 0;
        }
    }
    topo_sort();
    if (ord.size() != ALPHABET_SIZE) {
        cout << "Impossible\n";
    } else {
        for (const auto x: ord) cout << (char) (x + 'a');
        cout << "\n";
    }
    return 0;
}
```