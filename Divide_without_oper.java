// Divide without */
public class Solution {
    public Integer[] compute(int numerator, int denominator)
    {
        int count = 0;
        try
        {
            while(numerator - denominator >= 0)
            {
                numerator -= denominator;
                count += 1;
            }
        }
        catch (Exception e)
        {
            System.out.println(e.getMessage());
            count = Integer.MAX_VALUE;
        }
        Integer[] nums = {count, numerator};
        return nums;
    }
    
    public int divide(int dividend, int divisor) {
        int flag = 1;
        if(dividend < 1)
        {
            flag = -1;
            if(dividend == -2147483648) return Integer.MAX_VALUE;
            else
            {
                dividend = dividend - dividend - dividend;
            }
        }
        
        if(divisor < 1)
        {
            flag = flag - flag - flag; 
            if(divisor == -2147483648) return 0;
            else
            {
                divisor = divisor - divisor - divisor;
            }
        }
        
        if(divisor > dividend) return 0;
        
        // System.out.println(dividend + " " + divisor);
        Integer[] total = compute(dividend, divisor);
        return total[0] * flag;
    }
}

