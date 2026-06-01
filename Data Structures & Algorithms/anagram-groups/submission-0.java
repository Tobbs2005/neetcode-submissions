class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        for(String s : strs) {
            int[] count = new int[26];
            for(char c : s.toCharArray()){
                count['z'- c] = count['z'- c] + 1;
            }
            String res = Arrays.toString(count);
            map.putIfAbsent(res, new ArrayList<>());
            map.get(res).add(s);

        }
        return new ArrayList<>(map.values());
    }

}
