// Obviously the optimal solution
class Solution {
    public int romanToInt(String s) {
        int ans = 0;
        int maxIdx = s.length() - 1;
        for (int i = 0; i <= maxIdx; i++) {
            char c = s.charAt(i);
            char nextChar = '-';
            if (i < maxIdx) {
                nextChar = s.charAt(i + 1);
            }
            switch (c) {
                case 'M':
                    ans += 1000;
                    break;
                case 'D':
                    ans += 500;
                    break;
                case 'C':
                    if (nextChar == 'D') {
                        ans -= 100;
                    } else if (nextChar == 'M') {
                        ans -= 100;
                    } else {
                        ans += 100;
                    }
                    break;
                case 'L':
                    ans += 50;
                    break;
                case 'X':
                    if (nextChar == 'L') {
                        ans -= 10;
                    } else if (nextChar == 'C') {
                        ans -= 10;
                    } else {
                        ans += 10;
                    }
                    break;
                case 'V':
                    ans += 5;
                    break;
                case 'I':
                    if (nextChar == 'V') {
                        ans -= 1;
                    } else if (nextChar == 'X') {
                        ans -= 1;
                    } else {
                        ans += 1;
                    }
                    break;
            }
        }
        return ans;
    }
}
