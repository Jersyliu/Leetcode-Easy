class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a)<len(b):
            a,b=b,a
        a=list(a)[::-1]
        b=list(b)[::-1]
        for i in range(len(a)):
            a[i]=int(a[i])
        for j in range(len(b)):
            b[j]=int(b[j])
        result=''
        for i in range(len(b)):
            a[i]+=b[i]
        for j in range(len(a)-1):
            if a[j]==2:
                a[j+1]+=1
                a[j]=0
            if a[j]==3:
                a[j+1]+=1
                a[j]=1
        if a[len(a)-1]==2:
            a[len(a)-1]=0
            result+='1'
        if a[len(a)-1]==3:
            a[len(a)-1]=1
            result+='1'
        for k in a[::-1]:
            result+=str(k)
        return result