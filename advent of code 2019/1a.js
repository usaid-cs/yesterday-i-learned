const fs = require('fs');

const contents = fs.readFileSync('1.input.txt').toString();

const masses = contents
    .split('\n')
    .map((line) => line.trim())
    .map((line) => parseInt(line));

let sumOf = 0;
masses.forEach((mass) => {
    if (!isNaN(mass)) {
        sumOf += Math.floor(mass / 3) - 2;
    }
});

console.log(sumOf);
