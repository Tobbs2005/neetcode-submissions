class Solution {
    public boolean isPalindrome(String s) {
        //two pointers
        int length = s.length();
        int ptr1 = 0;
        int ptr2 = length-1;
        while(ptr1 < ptr2){
            while(!Character.isLetterOrDigit(s.charAt(ptr1)) && ptr1 < ptr2) ptr1++;
            while(!Character.isLetterOrDigit(s.charAt(ptr2)) && ptr1 < ptr2) ptr2--;

            if(Character.toUpperCase(s.charAt(ptr1)) != Character.toUpperCase(s.charAt(ptr2))) return false;
            ptr1++;
            ptr2--;
            
        }
        return true;
    }
}
