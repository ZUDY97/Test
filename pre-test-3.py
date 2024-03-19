num = 12345678

sel = int(input("입력 진수 결정(16/10/8/2):"))

num = input ("값 입력  : ")

if sel == 16 :
        num10 = int(num, 16)
if sel == 10 :
        num10 = int(num, 10)
if sel == 8 :
        num10 = int(num, 8)
if sel == 2 :
        num10 = int(num, 2)

        
print("10진수 ==>", num)
print("16진수 ==> ", hex_num)
print("8진수 ==>", oct_num)
print("2진수 ==> ", bin_num)
