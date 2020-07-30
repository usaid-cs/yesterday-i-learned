const fs = require('fs');

const contents = fs.readFileSync('1.input.txt').toString();

const masses = contents
    .split('\n')
    .map((line) => line.trim())
    .map((line) => parseInt(line));

function getFuel(mass) {
    const fuel = Math.floor(mass / 3) - 2;
    if (fuel <= 0) {
        return 0;
    }
    return fuel + getFuel(fuel);
}

let sumOf = 0;
masses.forEach((mass) => {
    if (!isNaN(mass)) {
        sumOf += getFuel(mass);
    }
});

console.log(sumOf);
