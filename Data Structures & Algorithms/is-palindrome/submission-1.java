class Solution {
    public boolean isPalindrome(String s) {
        String p = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        for(int i = 0, j = p.length() - 1; i <= j; i++, j--) {
            if(p.charAt(i) != p.charAt(j)) {
                return false;
            }
        }
        return true;
    }
}
