class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        dic={}
        bull,cow=0,0
        li=[]
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bull+=1
            else:
                li.append(guess[i])
                if secret[i] not in dic:
                    dic[secret[i]]=1
                else:
                    dic[secret[i]]+=1
        for i in li:
            if i not in dic:
                continue
            else:
                if dic[i]>0:
                    dic[i]-=1
                    cow+=1
                    
        return str(bull)+"A"+str(cow)+"B"