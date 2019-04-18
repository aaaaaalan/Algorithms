#806

class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        
        arphabet = [chr(i) for i in range(97,123)]
        
        units = 0
        lines = 1
        for s in S:
            i = arphabet.index(s)
            w = widths[i]
            
            if units + w > 100:
                units = 0
                lines += 1
                
            units += w

        return [lines, units]
            
        
