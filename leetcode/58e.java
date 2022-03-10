/**
 * Given a string s consisting of some words separated by some number of spaces,
 * return the length of the last word in the string.
 * A word is a maximal substring consisting of non-space characters only.
 */
class Solution {
    public int lengthOfLastWord(String s) {
        int lastWord = 0;
        boolean isInWord = false;
        for (int i = 0; i < s.length(); i++) {
            char ati = s.charAt(i);
            if (ati == ' ') {
                isInWord = false;
            } else {
                if (isInWord) {
                    lastWord++;
                } else {
                    lastWord = 1;
                }
                isInWord = true;
            }
        }
        return lastWord;
    }
}
