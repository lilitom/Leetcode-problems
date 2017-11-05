class Solution{
    
    public:
        int climbStairs(int n)
        {
            int f=1;
            int g=0;
            while (n--)
            {
                f+=g;
                g=f-g;
            }
            return f;
        }
    
    
}