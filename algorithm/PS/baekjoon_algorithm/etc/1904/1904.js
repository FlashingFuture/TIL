const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
let N;
rl.on('line', (line) => {
    N = parseInt(line);
})
rl.on('close', () => {
    // 점화식을 세워보자
    // N = 1 일 때 1개
    // N = 2 일 때 2개
    // N = 3 일 때의 경우 1 + 2 = 3
    // N = 4 일 경우 2 + 3 = 5
    const dp = new Array(1000001).fill(0);
    dp[1] = 1;
    dp[2] = 2;
    for (let i = 3; i <= N; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2]) % 15746;
    }
    const answer = dp[N]
    console.log(dp[N]);
    process.exit();
})