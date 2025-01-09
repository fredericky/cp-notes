## Analysis

This problem is to compute the area and perimeter of all connected components. Area is easy, it just counts the number of cells in the connected component. The perimeter is dectected as follows:

* The cell edge next to the boarder
* The cell edge next to empty space

## Code

```c++
#include <bits/stdc++.h>
using namespace std;

int N;
vector<vector<char>> grid;
vector<vector<bool>> visited;
vector<vector<int>> D = {
        {0, 1},
        {0, -1},
        {1, 0},
        {-1, 0},
};

int area, perimeter;

void dfs(int r, int c) {
    // edge next to boarder
    if (r < 0 || r >= N || c < 0 || c >= N) {
        perimeter++;
        return;
    }
    if (visited[r][c]) return;
    // edge next to empty space
    if (grid[r][c] == '.') {
        perimeter++;
        return;
    }
    visited[r][c] = true;
    area++;
    for (int k = 0; k < 4; ++k) {
        dfs(r + D[k][0], c + D[k][1]);
    }
}

int main() {
    freopen("perimeter.in", "r", stdin);
    freopen("perimeter.out", "w", stdout);

    cin >> N;
    grid.resize(N);
    grid.assign(N, vector<char>(N));

    visited.resize(N);
    visited.assign(N, vector<bool>(N));

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> grid[i][j];
        }
    }

    int area_output = 0, perimeter_output = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (!visited[i][j] && grid[i][j] == '#') {
                area = perimeter = 0;
                dfs(i, j);
                if (area > area_output) {
                    area_output = area;
                    perimeter_output = perimeter;
                } else if (area == area_output) {
                    perimeter_output = min(perimeter_output, perimeter);
                }
            }
        }
    }

    cout << area_output << " " << perimeter_output << "\n";
    return 0;
}
```