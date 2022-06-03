class Solution {
    public int shortestDistance(String[] wordsDict, String word1, String word2) {
        List<Integer> word1Indices = new ArrayList<Integer>();
        List<Integer> word2Indices = new ArrayList<Integer>();

        for (int i = 0; i < wordsDict.length; i++) {
            String word = wordsDict[i];
            if (word.equals(word1)) {
                word1Indices.add(i);
            } else if (word.equals(word2)) {
                word2Indices.add(i);
            }
        }

        int shortestDistance = 99999999;
        for (int i = 0; i < word1Indices.size(); i++) {
            for (int j = 0; j < word2Indices.size(); j++) {
                shortestDistance = Math.min(shortestDistance, Math.abs(word1Indices.get(i) - word2Indices.get(j)));
            }
        }

        return shortestDistance;
    }
}
