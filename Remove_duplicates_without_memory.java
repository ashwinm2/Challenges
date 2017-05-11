// Remove duplicates without memory
public class Solution {
    public int removeDuplicates(int[] nums) {
        int pos = 0;
        int prev = Integer.MAX_VALUE;
        for(int index = 0; index < nums.length; index++)
        {
            if(prev != nums[index])
            {
                nums[pos] = nums[index];
                pos += 1;
            }
            prev = nums[index];
        }
        
        return pos;
    }
}