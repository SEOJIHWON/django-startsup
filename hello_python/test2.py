# user_profile = {
#    "user_id" : "seongduck",
#    "pw" : "password"
# }


# login_state = False
# login_try = 0

# # True and not login_state

# while login_try <5 and not login_state :


#     password = input("input password : ")

#     if password == user_profile["pw"] :
#         print("login success")
#         login_state = True
        
        

#     else : 
#         print("login failed")

#     #login_try = login_try+1
#         login_try +=1


# if not login_state :
#     print("account locked")

# loan = int(input("input loan:"))
# pay = int(input("every month :"))

# if not pay >0 :
#     print("you hve to repay at least some")
#     exit(-1)

# month = 0

# while loan > 0 :
#     loan -= pay
#     month += 1

#    print(f"finish repay after {loan})



# i=0 

# while i < 100 :
#     print (f"i is currenlty : {i},")
     
#     i +=1

# print("end loop")


#for variable_name in <sequential data> :

# menus = ["chicken","pizza","beer"]


# for menu in menus:
#     print(f"We have {menu}.")

# print ("They are fantastic!")

# spelling = ""

# word = "fantastic"

# for char in word :
#     spelling += char + ", "

# print(f"{word} is spelled : {spelling [:-2]}.")


# for i in range(10) : 
#     print (i)

# for  i in range (1,11) :
#     print(i)

# [1,3,5,7,9]
# for  i in range (1,11,2) :
#     print(i)

# [(0,chicken),(1,pizza),(2,beer)]
 #enumerate() 는 튜플로 이뤄진 리스트가 반환된다.
# for (idx, item )in enumerate(menus) :
#     print (f"{idx +1 } : {item} ")

# print(enumerate(menus))


#break

# user_profile = {
#    "user_id" : "seongduck",
#    "pw" : "password"
# }


# login_state = False
# login_try = 0

# # True and not login_state

# while login_try <5 and not login_state :
    

#     password = input("input password : ")

#     if password == user_profile["pw"] :
#         print("login success")
#         login_state = True
        
        

#     else : 
#         print("login failed")

#     #login_try = login_try+1
#         login_try +=1


# if not login_state :
#     print("account locked")



#continue 반복문의 남은 과정을 스킵하고 다시 진행


# from tenize import group


people = [{"vaccinated": True , "sex" : "female" },{"vaccinated":False}]
group_count = 0

for person in people :

    if person["vaccinated"] and person["sex"]=="male" :
        continue

     group_count +=1 

print(group_count)

while True :
    for i in range(10) :
        while True :
            break

        if i> 5:
            break