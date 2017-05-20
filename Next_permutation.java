// Next permutation
public class Solution {
    public int[] nextPermutation(int[] nums) 
    {
        int prev = Integer.MIN_VALUE;
        int index = nums.length - 1;
        while(index >= 0)
        {
            if(prev > nums[index])
            {
                int length = nums.length;
                int jndex = fetch(nums, index, length);
                // System.out.println("Before " + nums[index] + " " + nums[jndex]);
                nums[index] += nums[jndex]; 
                nums[jndex] = nums[index] - nums[jndex]; 
                nums[index] -= nums[jndex];
                // System.out.println("After " + nums[index] + " " + nums[jndex]);
                int[] temp = compute(Arrays.copyOfRange(nums, index + 1, length));
                for(int i = 0; i < temp.length; i++)
                {
                    index += 1;
                    nums[index] = temp[i];    
                }
                index = -2;
            }
            else
            {
                prev = nums[index];
                index -= 1;
            }
        }
        
        if(index != -2)
        {
            Arrays.sort(nums);
        }
        return nums;
    }
    
    public int fetch(int[] bisect, int index, int length)
    {
        int jndex = length - 1;
        while(bisect[jndex] <= bisect[index])
        {
            jndex -= 1;
        }
        return jndex;
    }
    
    public int[] compute(int[] bisect)
    {
        Arrays.sort(bisect);
        return bisect;
    }
    
    
}