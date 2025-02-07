#include <iostream>

using namespace std;

int d[101][101] = { 0, };
int main() {
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n;
    cin >> n;
    d[2][1] = 2;

    for (int i = 3; i <= n; i++) {
        for (int j = 1; j < n; j++) {
            d[i][j] = 2 * d[i - 1][j] + d[i - 1][j - 1] + d[i - 1][j + 1];
            d[i][j] %= 10007;
        }
    }
    int sum = 0;
    for (int i = 1; i < n; i++) {
        sum += d[n][i];
        sum %= 10007;
    }
    cout << sum;
}