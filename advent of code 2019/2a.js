const fs = require('fs');

const contents = fs.readFileSync(`${__dirname}/2.input.txt`).toString();

const intCodes = contents
    .split(',')
    .map((line) => line.trim())
    .map((line) => parseInt(line));

function addOp(idx1, idx2, targetIdx) {
    intCodes[targetIdx] = intCodes[idx1] + intCodes[idx2];
}

function mulOp(idx1, idx2, targetIdx) {
    intCodes[targetIdx] = intCodes[idx1] * intCodes[idx2];
}

let ptr = 0;
intCodes[1] = 12;
intCodes[2] = 2;
while (true) {
    let op = intCodes[ptr];
    if (op === 1) {
        addOp(intCodes[ptr + 1], intCodes[ptr + 2], intCodes[ptr + 3]);
    } else if (op === 2) {
        mulOp(intCodes[ptr + 1], intCodes[ptr + 2], intCodes[ptr + 3]);
    } else if (op === 99) {
        break;
    } else {
        throw new Error(`op should not be ${op}`);
    }
    ptr += 4;
}
console.log(intCodes[0]);
