#include <iostream>
using namespace std;

int main() {
	int n, x, curr = 0;
	long long res = 0;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> x;
		curr = max(curr, x);
		res += max(curr - x, 0);
	}

	cout << res;
}
