#include <iostream>
#include <algorithm>

using namespace std;

int arr[9][9];
int max_num = -1

void Input()
{
	for (int i = 0;i < 9;i++) {
		for (int j = 0; j < 9; j++) {
			cin >> arr[i][j];
		}
	}
	return 0;
}

void Solution()
{
	int max_arr[9];
	for (int i = 0;i < 9;i++) {
		max_arr[i] = *max_element(arr[i], arr[i] + 9);
	}
	max_num = *max_element(max_arr, max_arr + 9);
	cout << max_num;
	return 0;
}

int main() 
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	Input();
	Solution();
	return 0;
}

