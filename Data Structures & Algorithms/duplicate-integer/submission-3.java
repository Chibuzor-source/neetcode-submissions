
class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<Integer>();
        for(int number : nums) {
            set.add(number);
        }
        return set.size() != nums.length;
    }
}
