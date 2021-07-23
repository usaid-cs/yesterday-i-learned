/**
 * The knows API is defined in the parent class Relation.
 * isBadVersion(version: number): boolean {
 *     ...
 * };
 */


function assert(a, b, notes = '') {
    if (a !== b) {
        console.log(`${notes}: Expected result to be ${b}, got ${a}`);
    }
}

var solution = function(isBadVersion: any): any {

    return function(n: number): number {
        if (n == 0) {
            return -1;
        }
        var left: number = 1;
        var right: number = n;
        var middle: number;
        while (left <= right) {
            middle = Math.ceil((left + right) / 2);
            if (isBadVersion(middle) && !isBadVersion(middle - 1)) {
                return middle;
            } else if (isBadVersion(middle)) {
                // Bad version occurred on or before that
                right = middle - 1;
            } else {
                // Bad version occurred after that
                left = middle + 1;
            }
        }
        return middle;
    };
};


var tester;
tester = solution(function (version) {
    return ['good', 'bad'][version - 1] == 'bad';
});
assert(tester(2), 2)
tester = solution(function (version) {
    return ['bad'][version - 1] == 'bad';
});
assert(tester(1), 1)
tester = solution(function (version) {
    return ['bad', 'bad'][version - 1] == 'bad';
});
assert(tester(2), 1)
