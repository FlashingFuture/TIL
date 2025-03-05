const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = +fs.readFileSync(filePath).toString().trim();

const pr = [1, 3, 5, 7, 9]; // 홀수 리스트

const prime = (num) => {
  if (num === 1) return false;
  if (num === 2) return true;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
};

const dfs = (x, N) => {
  if (N === 1) {
    console.log(x);
    return;
  }

  for (let i = 0; i < 5; i++) {
    const next = x * 10 + pr[i];
    if (prime(next)) {
      dfs(next, N - 1);
    }
  }
};

const solution = () => {
  dfs(2, input);
  dfs(3, input);
  dfs(5, input);
  dfs(7, input);
};

solution();
