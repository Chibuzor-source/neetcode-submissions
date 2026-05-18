
class Solution {
    public boolean hasDuplicate(int[] nums) {
       Set<Integer> h = new HashSet<>();
       for(int j : nums){
        if(h.contains(j)) {
            return true;
        } else {
            h.add(j);
        }
       }
       return false;
    }
}
