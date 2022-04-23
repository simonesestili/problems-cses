#include <iostream>
#include <string>
using namespace std;

int main() {
	string s;
	cin >> s;
	char prev = '!';
	int cnt = 0, res = 0;

	for (char c : s) {
		cnt = c == prev ? cnt + 1 : 1;
		prev = c;
		res = max(res, cnt);
	}

	cout << res;
}
