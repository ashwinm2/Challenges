// Remove element without extra memory
public class Solution {
    public int removeElement(int[] nums, int val) {
        int count = 0;
        for(int index = 0; index < nums.length; index++)
        {
            if(nums[index] != val)
            {
                nums[count] = nums[index];
                count += 1;
            }
        }
        return count;
    }
}