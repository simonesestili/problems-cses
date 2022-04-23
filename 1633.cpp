#include <iostream>
using namespace std;

int main() {
	int n, m = 1000000007;
	cin >> n;

	int dp[n+1] = {};
	dp[0] = 1;
	for (int i = 1; i <= n; i++) {
		for (int d = 1; d <= 6 && i - d >= 0; d++) {
			dp[i] = (dp[i - d] + dp[i]) % m;
		}
	}

	cout << dp[n];
}
