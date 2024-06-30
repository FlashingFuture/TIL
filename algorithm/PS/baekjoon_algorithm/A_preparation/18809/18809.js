const readline = require('readline')
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})
const input = []
rl.on('line', (line) => {
  input = line.split(' ')
  rl.close();
})
rl.on('close', () => {
  console.log(input)
  process.exit();
})