const lower = 146810;
const upper = 612564;

function isValid(password) {
    return hasSixDigits(password) &&
        withinRange(password) &&
        hasTwoAdjacentDigits(password) &&
        neverDecreases(password);
}

function getDigits(password) {
    return password.toString().split('').map(Number);
}

function hasSixDigits(password) {
    // A bit pointless. We already know the bounds.
    return password.toString().length === 6;
}

function withinRange(password) {
    return password >= lower && password < upper;
}

function hasTwoAdjacentDigits(password) {
    const digits = getDigits(password);
    // Why do you even need this... strings can be accessed by index
    return digits[0] === digits[1] ||
        digits[1] === digits[2] ||
        digits[2] === digits[3] ||
        digits[3] === digits[4] ||
        digits[4] === digits[5];
}

function neverDecreases(password) {
    const digits = getDigits(password);
    return digits[0] <= digits[1] &&
        digits[1] <= digits[2] &&
        digits[2] <= digits[3] &&
        digits[3] <= digits[4] &&
        digits[4] <= digits[5];
}

let count = 0;
for (var i = lower; i <= upper; i++) {
    if (isValid(i)) {
        count += 1;
    }
}
console.log(count);
