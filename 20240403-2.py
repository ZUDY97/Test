
ss = 'Phython'

sslen = len(ss)

for i in range (0, sslen) :
    print (ss[i] + '$', end = '')
    


inStr, outStr = "Phython", ""

strlen = len(inStr)

for i in range (0, strlen) :
    outStr += inStr [strlen - (i+1)]
print("내용을 거꾸로 출력 --> %s" % outStr)




inStr = "파이썬##CookBook$$$@@@열공중1234"
OutStr = inStr

remove_list = ["##", "$$$", "@@@", "CookBook", "열공중", "1234"]

for word in remove_list:
    OutStr = OutStr.replace(word, "")

print("원래 문자열 ==> " + '[' + inStr + ']')
print("삭제 문자열 ==> " + '[' + OutStr + ']')
