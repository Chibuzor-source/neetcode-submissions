class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
    List<List<Integer>> bigList = new ArrayList<>();
    if(nums.length < 3) return bigList;
    Arrays.sort(nums);
    if(nums[0] > 0) return bigList;
    for(int start = 0; start < nums.length; start++) {
        if(start > 0 && nums[start] == nums[start - 1]) continue;
        int left = start + 1, right = nums.length - 1;
        while(left < right) {
        int sum = nums[start] + nums[left] + nums[right];
        if(sum > 0) {
            right--;
        } else if (sum < 0) {
            left++;
        } else {
            bigList.add(Arrays.asList(nums[start], nums[left], nums[right]));
            while(left < right && nums[left] == nums[left + 1]) left++;
            while(left < right && nums[right] == nums[right - 1]) right--;
            left++;
            right--;
        }
      }
      
    }
    return bigList;

    }
}
