class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if(s1.length()>s2.length()) return false;
        int[] string = new int[26];
        int[] curr = new int[26];
        for(int i=0; i<s1.length(); i++){
            curr[s2.charAt(i)-'a'] = curr[s2.charAt(i)-'a']+1;
            string[s1.charAt(i)-'a'] = string[s1.charAt(i)-'a']+1;
        }

        //build window
        int l = 0;
        int r = s1.length()-1;

        while(r<s2.length()-1){
            if(Arrays.equals(string,curr)) return true;
            curr[s2.charAt(l)-'a'] = curr[s2.charAt(l)-'a'] - 1;
            l++;
            r++;
            curr[s2.charAt(r)-'a']=curr[s2.charAt(r)-'a']+1;
        }
        return Arrays.equals(string,curr);
    }
}
