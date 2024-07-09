const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = require('fs').readFileSync('./input.txt').toString().trim().split('\n');
const N = parseInt(input.shift());
const S = input[0].split(' ').map(el => parseInt(el));

let maxLength = 0;
let left = 0;
let fruitCount = new Map();

for (let right = 0; right < N; right++) {
    fruitCount.set(S[right], (fruitCount.get(S[right]) || 0) + 1);
    
    while (fruitCount.size > 2) {
        fruitCount.set(S[left], fruitCount.get(S[left]) - 1);
        if (fruitCount.get(S[left]) === 0) {
            fruitCount.delete(S[left]);
        }
        left++;
    }
    
    maxLength = Math.max(maxLength, right - left + 1);
}

console.log(maxLength);