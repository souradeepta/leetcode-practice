import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> comp = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int compliment = target - nums[i];
            if (comp.containsKey(compliment)) {
                return new int [] {
                    comp.get(compliment), i
                };
            }
            else{
                comp.put(nums[i], i);
            }
        }
        return null;
    }
}