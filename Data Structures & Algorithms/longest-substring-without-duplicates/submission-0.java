class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l = 0;
        HashSet<Character> set = new HashSet<Character>();
        int res = 0;
        for(int r = 0; r < s.length(); r++) {
            char curr = s.charAt(r);
            while(set.contains(curr)) {
                set.remove(s.charAt(l));
                l++;
                
            }
            set.add(curr);
            res = Math.max(res, set.size());
        }
        return res;
    }
}
