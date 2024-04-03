inStr = input("문자열을 입력하세요 : ")
count = len(inStr)
outStr = ""  # outStr을 빈 문자열로 초기화합니다.

for i in range(count):
    outStr += inStr[count - (i + 1)]

print("내용을 거꾸로 출력 --> %s" % outStr)
