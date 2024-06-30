const readline = require('readline')
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})
let input;
rl.on('line', (line) => {
  input = line;
  rl.close();
})
rl.on('close', () => {
  // DP 풀이 : 크기 N짜리 배열을 선언하여 1부터 해당 위치를 찾아가면 된다
  const N = parseInt(input);
  const DP = new Array(N + 1).fill(0);
  DP[1] = 0
  for (i=2; i<=N; i++) {
    DP[i] = DP[i - 1] + 1
    if (i % 2 == 0) {
      DP[i] = Math.min(DP[i], DP[i / 2] + 1)
    }
    if (i % 3 == 0) {
      DP[i] = Math.min(DP[i], DP[i / 3] + 1)
    }
  }
  console.log(DP[N])
  process.exit();
})