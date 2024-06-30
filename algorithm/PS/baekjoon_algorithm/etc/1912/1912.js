const fs = require('fs');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const input=fs.readFileSync('/dev/stdin').toString().split('\n');

const n = parseInt(input.shift())
// n과 크기가 같은 dp을 선언하고
// 해당 위치까지 이어지는 최댓값을 dp에 저장해주면서
// 자연스럽게 dp로 풀이
const arr = input[0].split(' ').map(el => parseInt(el))
let maxSum = arr[0]
for (let i=1; i<n; i++) {
  arr[i] = Math.max(arr[i], arr[i] + arr[i - 1])
  maxSum = Math.max(maxSum, arr[i])
}
console.log(maxSum)