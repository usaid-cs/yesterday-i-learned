const fs = require('fs');

const contents = fs.readFileSync(`${__dirname}/2.input.txt`).toString();

function tryNounVerb(noun, verb) {
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
    intCodes[1] = noun;
    intCodes[2] = verb;
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
    return intCodes[0];
}

for (let noun = 0; noun < 100; noun++) {
    for (let verb = 0; verb < 100; verb++) {
        if (tryNounVerb(noun, verb) === 19690720) {
            console.log(100 * noun + verb);
        }
    }
}
