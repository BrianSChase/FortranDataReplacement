
import re

TestString = "aaa if(Arr(x,y,z) .eq. stuff) ar(a)"
Var = "Target"
Type = 'MainType%SubType%SubSubType'

#Want to do MainType(x)%SubType(y)%SubSubType(z)


FindResult = ''

#Find whole array
FindResult = re.findall('arr\([a-z]*\,[a-z]*\,[a-z]*\)', TestString, re.IGNORECASE)
print(FindResult)

#Separate array from indexing
IndexFind = ''
IndexFind = re.findall('\([a-z]*\,[a-z]*\,[a-z]*\)', FindResult[0], re.IGNORECASE) 
print(IndexFind)

#Break the array into 3 parts
Index1 = ''
Index2 = ''
Index3 = ''
i = 1
for x in IndexFind[0]:
    if x == '(' or x == ',' or x == ')' or x == '\n' or x == '':
        pass
    elif i == 1:
        Index1 = x
        i = i + 1
    elif i == 2:
        Index2 = x
        i = i + 1
    elif i == 3:
        Index3 = x
print(Index1)
print(Index2)
print(Index3)

#Assemble final result
FinalResult = ''
i = 1
for x in Type:
    if x == '%' and i == 1:
        i = i + 1
        FinalResult = FinalResult + '(' + Index1 + ')' + '%'
    elif x == '%' and i == 2:
        FinalResult = FinalResult + '(' + Index2 + ')' + '%'
    else:
        FinalResult = FinalResult + x
FinalResult = FinalResult + '(' + Index3 + ')'

print(FinalResult)




