import re
def find(s):
     charRe  = '\w*z.\w*'
     if  re.search(charRe, s):
         return "found a match"
     else :
         return "not matched"    


s= input()
print (find(s) )