#include <iostream>
using namespace std;

int main() {
    int n, input;
    cin >> n;

    int res = n;
	for (int i = 1; i < n; i++) {
		cin >> input;
		res ^= i ^ input;
	}

	cout << res;

    return 0;
}
