#1번

# A = [1,25,30,6,2,99,10,11,31,32,5]

# A.sort()



# for index in A   :
    

#      if index >13 :
        
          


      

   

#2번

# for _ in range(10) :
#   print("*1*")

#3번 


# count = int(input("지각한 시간은 몇 분 입니까?:"))

# if count <=5 :
#     for _ in range(10) :
#       print("다시는 지각을 안하겠습니다.") 

# elif count <=10 and count > 5:
#     for _ in range(19) :
#          print("다시는 지각을 안하겠습니다.") 

# elif count <=30 and count > 10:
#     for _ in range(29) :
#          print("다시는 지각을 안하겠습니다.") 

# elif count > 30 :
#     for _ in range(50) :
#          print("다시는 지각을 안하겠습니다.") 
#          if  _%10 ==0 :
#              print("/")


#4번



# i=""

# for _ in range(10) :
#     i  = i+"*"
#     print(i)


#5번 

i = 1
j = "*"
x = " "

for i in range(1) :
   
    if     i <7 :
            print (x*(1+(5-i)),j*(1+(i-1)*2))
            
    if i>=7 :
             print(x*(1+(i-7)),j*(7+(i-8)*-2)) 