class Solution {
    public boolean isSubsequence(String s, String t) {
        if (s.length() == 0) {
            return true;
        }
        if (t.length() == 0) {
            return false;
        }

        int ptrs = 0;

        for (int ptrt = 0; ptrt < t.length(); ptrt++) {
            if (s.charAt(ptrs) == t.charAt(ptrt)) {
                ptrs += 1;
                if (ptrs >= s.length()) {
                    return true;
                }
            }
        }
        return false;
    }
}
