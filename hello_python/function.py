# def print_hello_world() :
#     print ("Hello, World!")

# print_hello_world()


# def say_hello(name):
#     print(f"hello {name}")

# say_hello("kim")



# name = input("your name: ")
# year = input("your year: ")


# def calculate_age(name, year):
#     print(f"hello, {name} , You are {2022-year +1}s old")


# calculate_age(name, int(year))



# def read_athlete_data(athlete):
    
#     print
    
#     if type(athlete) == type(dict()):
        
#         print("athlete info") #.get 함수는 none을 반환하기 때문에 
#         print(f"name: {athlete.get('name')}")
#         print(f"event: {athlete.get('event')}")
#         print(f"age: {athlete.get('age')}")
#         print(f"height: {athlete.get('height')}")

#     else :
#         print ("Wrong Input")


# athlete_oh = {
#      "name":"Oh Jin Hyek",
#      "event": "Archery",
#      #"age": 40,
#      "height":188
# }

# read_athlete_data(athlete_oh)
# read_athlete_data("string")

# year = int(float(input("입력하샘")))

# def is_leap_year(year) :

#     result = False
#     if year % 4 ==0:
#         result = True
#         if year % 100 == 0 and year % 400 != 0 :
#             result = False
#         elif year % 400 == 0 :
#             result = True
#     else:
#         pass

#     return result
    

# is_leap = is_leap_year(year)
    
# if is_leap == True :
#             print(f"{year}is leap year")
# else : 
#             print(f"{year}is not leap year")


# name_1 = input("enter name: ")
# age_1 = input("enter age: ")
# event_1 = input("enter event: ")
# nation_1 = input("enter nationality: ")

 
# def create_fuction() :


#     name_1 = input("enter name: ")
#     age_1 = input("enter age: ")
#     event_1 = input("enter event: ")
#     nation_1 = input("enter nationality: ")

#     althlete = {}

#     althlete.update({"name": name_1, "age": age_1})
#     althlete.update({"age": age_1})
#     althlete.update({"event": event_1})
#     althlete.update({"nationality": nation_1})

#     return althlete



# def factorial(n) :
    
#    if n == 0 or n == 1 :
#         return  1
#     elif n ==int and n >1 :
#         return factorial(n-1) * n
    



# def fibonacci(n):
#      #n번째는 피보나치 수열의 수를 반환

#     if n ==1 or n ==2 :
#         return 1
#     elif n> 2:
#         return fibonacci(n-1) + fibonacci(n-2)
   
#사용자오류 제한하기

# user_input = input("input user number:")

# try :
#     user_number = int(user_input)

#     print(f"user number is {user_number}")

# except ValueError  as e :
#     print("Invalid Input") 




# list = []
#     list.append({dict})

# print(f"name:\t\t\t{name_1}")
# print(f"age:\t\t\t{age_1}")
# print(f"event:\t\t\t{event_1}")
# print(f"nationality:\t{nation_1}")
# print("################################################################")
# name_2 = input("enter name: ")
# age_2 = input("enter age: ")
# event_2 = input("enter event: ")
# nation_2 = input("enter nationality: ")

# print(f"name:\t\t\t{name_2}\t\t\t\tname:\t\t\t{name_1}")
# print(f"age:\t\t\t{age_2}\t\t\t\t\tage:\t\t\t{age_1}")
# print(f"event:\t\t\t{event_2}\t\t\t\tevent:\t\t\t{event_1}")
# print(f"nationality:\t{nation_2}\tnationality:\t{nation_1}")



# def calculate_age(name, born_year, current_year=2022) :
#     print(f"hello {name}! Youre {current_year-born_year+1}years old.")

# calculate_age("park", 1990, )

def create_car (name, brand="현대",engine = "gasolin", passenger=5 ):
    return{
        "name": name,
        "brand":brand,
        "engine":engine,
        "passengers":passenger
    }

print(create_car("소나타"))

print(create_car("k4","기아"))

print(create_car("소나타", engine="LPG"))
print(create_car("소나타", passenger=7))
print(create_car("소나타", engine="경유", passenger=7) )