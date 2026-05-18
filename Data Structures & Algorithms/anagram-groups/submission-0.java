class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> wordMap = new HashMap<>();
        for(String str : strs) {
            int [] charCount = new int [26];
            for(char c : str.toCharArray()) {
                charCount[c - 'a']++;
            }
            String key = Arrays.toString(charCount);
            wordMap.putIfAbsent(key, new ArrayList <>());
            wordMap.get(key).add(str);
        }
        
        return new ArrayList<>(wordMap.values());
    }
}
