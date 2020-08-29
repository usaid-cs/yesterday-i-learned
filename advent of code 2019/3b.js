const fs = require('fs');

const contents = fs.readFileSync(`${__dirname}/3.input.txt`).toString();
// const contents = "R75,D30,R83,U83,L12,D49,R71,U7,L72\n" +
//     "U62,R66,U55,R34,D71,R55,D58,R83";

const wires = contents.split('\n');

const visitedNodes = [{}, {}];

wires.forEach((wire, idx) => {
    if (!wire.trim()) return;

    const instructions = wire.split(',');

    const instructions2 = instructions.map((value) => [value[0], Number(value.slice(1))]);

    let [currentX, currentY] = [0, 0];

    visitedNodes[idx][[currentX, currentY]] = 0

    let totalDistance = 0;
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
                visitedNodes[idx][[currentX, currentY]] += totalDistance + i + 1;
            } else {
                visitedNodes[idx][[currentX, currentY]] = totalDistance + i + 1;
            }
        }
        totalDistance += distance;
    });

});

console.log(visitedNodes);

const repeatedNodes = [];
for (let x in visitedNodes[0]) {
    if (visitedNodes[1][x] !== undefined) {
        // console.log(visitedNodes[0][x], visitedNodes[1][x]);
        let num1 = Math.abs(Number(visitedNodes[0][x]));
        let num2 = Math.abs(Number(visitedNodes[1][x]));
        repeatedNodes.push(num1 + num2);
    }
}

repeatedNodes.sort((a, b) => a - b);

console.log(repeatedNodes);

// [0] is 0,0
console.log(repeatedNodes[1]);
