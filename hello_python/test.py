# #1번

# import pstats


# num1 = input()
# num2 = input()

# if num2 > num1 :
#     print ("num2이 num1 보다 큽니다.")
# elif num1 ==num2 :
#     print ("num1과 num2는 같은 수 입니다.")
# else :
#    pass


#2번

num1 = input()
num2 = input()
cal = input()

if cal == "+" :
    print (int(num1)+int(num2))
elif cal == "/" :
    print (int(num1)/int(num2))
else :
  pass

print(cal)

# #3번

# price = input("상품금액을 입력하세요:")

# if price >= 1000000 :
#    tax= price * 0.15
# elif  price <1000000 and price >=500000 :
#    tax = price * 0.1
# elif  price <500000 :
#    tax = price * 0.05
# else :
#     pass

# print(f"세금은{tax}원입니다.")

# #4번

date = input ("몇년도 ?")


if int(date)%28 ==9 or int(date)%28 ==3 :
    print(f"{date}년 1월 1일은 토요일")
elif int(date)%28 ==10 or int(date)28 ==8 :
    print(f"{date}년 1월 1일은 일요일")
elif int(date)%28 ==3 :
    print(f"{date}년 1월 1일은 월요일")
elif int(date)%28 ==9 or int(date)%28 ==4 :
    print(f"{date}년 1월 1일은 화요일")
elif int(date)%28 ==11  or int(date)%28 ==5 :
    print(f"{date}년 1월 1일은 목요일")
elif int(date)%28 ==0  or int(date)%28 ==2:
    print(f"{date}년 1월 1일은 금요일")
    
else :
    pass
