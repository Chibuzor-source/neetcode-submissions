class Solution {
    public boolean isAnagram(String s, String t) {
      if(s.length() != t.length()) return false;
      Map<Character, Integer> countS = new HashMap<>();
      Map<Character, Integer> countT = new HashMap<>();
      for(int i = 0; i < s.length(); i++){
        char chS = s.charAt(i);
        char chT = t.charAt(i);
        if(countS.containsKey(chS)) {
            int num1 = countS.get(chS);
            countS.put(chS, num1 + 1);
        } else {
            countS.put(chS, 1);
        }
        if(countT.containsKey(chT)){
            int num2 = countT.get(chT);
            countT.put(chT, num2 + 1);
        } else {
            countT.put(chT, 1);
        }
      }
      return countT.equals(countS);
    }
}
