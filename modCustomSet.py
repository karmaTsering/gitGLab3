"""
Description: THis program create set intersection, union, 
"""
class CustomSet:
    
    def __init__(self, tmp1):
        """
        __author__="Karma Gurung"
        __date__="4/27/16"
        Description: This
        Pre-condition:
        Post-condition:
        
        """
        self._setList=[]
        for el in tmp1:
            if el not in self._setList:
               self._setList.append(el)


    def unionSet(self, set,tmp2):
        """
        __author__="Karma Gurung"
        __date__="4/27/16"
        Description:
        Pre-condition:
        Post-condition:
        
        
        newSet=[]
        Set=[]
        for el in tmp1:
            newSet.append(el)

        for el in tmp2:
            newSet.append(el)

        for el in newSet:
            if el not in Set:
                Set.append(el)

        return Set
        """
       
        result = Set()
        for i in self:
            result.add(i)
        for i in set:
            result.add(i)
        return result
        
    def intersectionSet(tmp1,tmp2):
        """
        __author__="Karma Gurung"
        __date__="4/27/16"
        Description:
        Pre-condition:
        Post-condition:
        """
        newSet=[]
        Set=[]
        for el in tmp1:
            newSet.append(el)

        for el in tmp2:
            newSet.append(el)

        for el in newSet:
            if el in Set:
                Set.append(el)

        return Set

    def __str__(self):
        """
        __author__="Karma Gurung"
        __date__="4/27/16"
        Description:
        Pre-condition:
        Post-condition:
        """
        
        tmp=','.join(str(el) for el in self._setList)
        outPut="{"+tmp+"}"
        return outPut
