// 세 용액
// N <= 5000, N^2 <= 25000000
// 우선 용액을 정렬한 다음
// 두 포인터를 양끝에서 중앙으로 향하게 움직이면서
// 남은 포인터(free)를 전체를 순회시키면 시간초과는 나지 않을것
// 전체를 순회하지 말고 free의 범위에 맞춰서 하면 될듯
// free 로 중앙에 두지 말고 그냥 시작 위치에 맞춰서 for문을 돌면 될듯
const MAX_NUM = 1000000000;
// 문제풀이
const fs = require('fs');
// const input = fs.readFileSync('./input.txt').toString().split('\n');
const input = fs.readFileSync('./dev/stdin').toString().split('\n');
const N = parseInt(input.shift());
const liquids = input.shift().split(' ').map(el => parseInt(el));
liquids.sort((a, b) => a - b);

let min_sum = 3*MAX_NUM + 1;
let answer = [0, 0, 0]
for (let start=0; start < N-2; start++) {
    let middle = start + 1;
    let end = N - 1;
    while (middle < end) {
        const current_sum = liquids[start] + liquids[middle] + liquids[end];
        if (Math.abs(current_sum) < min_sum) {
            answer = [liquids[start], liquids[middle], liquids[end]];
            min_sum = Math.abs(current_sum);
        }

        if (current_sum < 0) {
            middle++;
        } else {
            end--;
        }

    }
}

console.log(answer[0], answer[1], answer[2]);