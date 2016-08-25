class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        string=list(s)
        vowel='aeiouAEIOU'
        vowels=[]
        index=[]
        result=''
        for i in range(len(string)):
            if string[i] in vowel:
                vowels.append(string[i])
                index.append(i)
        re=vowels[::-1]
        for j in range(len(index)):
            string[index[j]]=re[j]
        for k in string:
            result+=str(k)
            
        return result