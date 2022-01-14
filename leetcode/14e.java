class Solution {
    public String longestCommonPrefix(String[] strs) {

        StringBuilder sb = new StringBuilder();
        List<String> foo = List.of(strs);  // How to convert an array to a List

        // https://stackoverflow.com/a/20999230/1558430 (read the comments)
        List<Integer> lengths = foo.stream()  // Turn a list into a stream
            .map(String::length)  // Apparently that already lets you turn a string into its length
            .collect(Collectors.toList());  //  Turns the stream back into a list

        // So Arrays.sort() sorts arrays, and Collections.sort() sorts collections (which lists are)
        Collections.sort(lengths);
        int shortest = lengths.get(0);  // [0] is not a thing, because Gosling doesn't ever see it being useful https://stackoverflow.com/a/78086/1558430

        for (int i = 0; i < shortest; i++) {
            char current = strs[0].charAt(i);  // Again, anyString[0] is way too simple and intuitive and we can't have that
            for (String str: strs) {
                if (str.charAt(i) != current) {
                    return sb.toString();
                }
            }
            // How to turn a char into a string
            // Character.toString(c) is the same as String.valueOf(c)
            // because the latter simply calls the former.
            // https://stackoverflow.com/a/3335766/1558430
            sb.append(String.valueOf(current));
        }

        return sb.toString();
    }
}
