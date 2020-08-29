const fs = require('fs');

const contents = fs.readFileSync(`${__dirname}/3.input.txt`).toString();

const wires = contents.split('\n');

const visitedNodes = [{}, {}];

wires.forEach((wire, idx) => {
    if (!wire.trim()) return;

    const instructions = wire.split(',');

    const instructions2 = instructions.map((value) => [value[0], Number(value.slice(1))]);

    let [currentX, currentY] = [0, 0];

    visitedNodes[idx][[currentX, currentY]] = 1

    instructions2.forEach((instruction) => {
        const [direction, distance] = instruction;

        for (let i = 0; i < distance; i++) {
            if (direction === 'U') {
                currentY -= 1;
            } else if (direction === 'D') {
                currentY += 1;
            } else if (direction === 'L') {
                currentX -= 1;
            } else if (direction === 'R') {
                currentX += 1;
            } else {
                throw new Error('wtf did you do!!');
            }
            if (visitedNodes[idx][[currentX, currentY]]) {
                visitedNodes[idx][[currentX, currentY]] += 1;
            } else {
                visitedNodes[idx][[currentX, currentY]] = 1;
            }
        }
    });

});

const repeatedNodes = [];
for (let x in visitedNodes[0]) {
    if (visitedNodes[1][x] !== undefined) {
        repeatedNodes.push(x);
    }
}

const distances = repeatedNodes.map((repeatedNode) => {
    let [x, y] = repeatedNode.split(',');
    return Math.abs(Number(x)) + Math.abs(Number(y));
});

distances.sort((a, b) => a - b);

// [0] is 0,0
console.log(distances[1]);
