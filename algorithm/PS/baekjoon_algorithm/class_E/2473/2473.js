// 세 용액
// N <= 5000, N^2 <= 25000000
// 우선 용액을 정렬한 다음
// 두 포인터를 양끝에서 중앙으로 향하게 움직이면서
// 남은 포인터(free)를 전체를 순회시키면 시간초과는 나지 않을것
// 전체를 순회하지 말고 free의 범위에 맞춰서 하면 될듯
const fs = require('fs');
const input = fs.readFileSync('./input.txt').toString().split('\n');
const N = parseInt(input.shift());
const liquids = input.shift().split(' ').map(el => parseInt(el))
liquids.sort((a, b) => a - b);
console.log(liquids);
for (let free=0; free<N; free++) {
    current_free = liquids[free]
    let { start, end } = [0, N - 1];
    while (start <= end) {
        current_sum = liquids[start] + liquids[end] + current_free;
        if (current_sum > 0) {
            end--;
        } else if (current_sum === 0) {

        } else {
            start++;
        }
    }
}