// const n = parseInt(require('fs').readFileSync('./input.txt').toString().trim());
const n = parseInt(require('fs').readFileSync('/dev/stdin').toString().trim());

// DP 의 기본은 점화식!
const dp = new Array((1001)).fill(0);
dp[1] = 1;
dp[2] = 2;
// n > 2 | dp[n] = dp[n - 1] + dp[n - 2]
for (let i=3; i<=n; i++) {
  dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
}

console.log(dp[n]);