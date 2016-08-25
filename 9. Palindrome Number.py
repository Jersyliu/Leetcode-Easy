class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        i=0
        while 10**i<=x:
            i+=1
        for k in range(1,i//2+1):
            if (x//10**(i-(2*k-1)))==(x%10):
                x=x%(10**(i-(2*k-1)))
                x=x//10
            else:
                return False
        if x<10:
            return True
            
            
            
'''
int len=1;
    for (len=1; (x/len) >= 10; len*=10 );

    while (x != 0 ) {
        int left = x / len;
        int right = x % 10;

        if(left!=right){
            return false;
        }

        x = (x%len) / 10;
        len /= 100;
    }
    return true;
}
'''