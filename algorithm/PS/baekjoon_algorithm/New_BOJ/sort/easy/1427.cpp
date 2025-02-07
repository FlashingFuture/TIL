#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(void)
{
	string N;
	cin >> N;
	sort(N.begin(), N.end(), greater<char>());

	cout << N << endl;

	return 0;
}