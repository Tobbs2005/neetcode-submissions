class Solution {
    public int characterReplacement(String s, int k) {
        int l = 0;
        int usedLetters = 0;
        int res = 0;
        HashMap<Character, Integer> map = new HashMap<>();
        int maxUsed=0;
        for(int r = 0; r < s.length(); r++){
            map.put(s.charAt(r), map.getOrDefault(s.charAt(r), 0) + 1);

            maxUsed = Math.max(maxUsed, map.get(s.charAt(r)));
            while((r-l+1) - maxUsed > k){
                map.put(s.charAt(l), map.getOrDefault(s.charAt(l), 0) - 1);
                l++;
            }
            res = Math.max(res, r-l+1);
        }
        return res;
    }
}
