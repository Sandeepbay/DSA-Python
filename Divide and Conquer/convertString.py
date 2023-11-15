def convertString(s1,s2,index1,index2):
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return convertString(s1,s2,index1+1,index2+1)
    else:
        deleteOperations = 1 + convertString(s1,s2,index1,index2+1)
        AddOperations = 1 + convertString(s1,s2,index1+1,index2)
        replaceoperations = 1 + convertString(s1,s2,index1+1,index2+1)
        return min(deleteOperations , AddOperations , replaceoperations)
    
print(convertString("table" , "tgfres" , 0 , 0))