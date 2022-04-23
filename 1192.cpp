#include <iostream>
#include <string>
#include <vector>
using namespace std;

int n, m;
int DIRS[5] = {0, 1, 0, -1, 0};

void dfs(string mat[], int r, int c) {
	if (r < 0 || r >= n || c < 0 || c >= m || mat[r][c] == '#') return;
	mat[r][c] = '#';
	for (int i = 0; i < 4; i++)
		dfs(mat, r + DIRS[i], c + DIRS[i+1]);
}

int rooms(string mat[]) {
	int count = 0;
	
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			count += mat[i][j] == '.';
			dfs(mat, i, j);
		}
	}

	return count;
}

int main() {
	string input;
	cin >> n >> m;
	string mat[n];
	for (int i = 0; i < n; i++) {
		cin >> input;
		mat[i] = input;
	}
	
	cout << rooms(mat);
	return 0;
}
