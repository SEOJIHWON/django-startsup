

#1

#print("name:\t\t An San \t\tname:\t\t Kim Jedeok \nage: \t\t 20 \t\t\tage:  \t\t 17 \nevent: \t\t archery \t\tevent: \t\t archery\nnationality: \t Korea, Republic of \tnationality: \t Korea, Republic of")

#2

# name = input("enter name: ")
# age = input("enter age: ")
# event = input("enter event: ")
# nationality = input("enter nationality: ")

# print(f"name:\t\t {name} \nage: \t\t {age} \nevent: \t\t {event} \nnationality:\t {nationality}")


# print("########################################################################")



# name2 = input("enter name: ")
# age2 = input("enter age: ")
# event2 = input("enter event: ")
# nationality2 = input("enter nationality: ")


# print(f"name:\t\t {name} \t\tname:\t\t {name2} \nage: \t\t {age} \t\tage:  \t {age2} \nevent: \t\t {event} \t\tevent: \t\t {event2}\nnationality: \t {nationality} \t\tnationality: \t {nationality2}")

#2-2

# num =int(float(input("enter digit:")))

# con= num*num
# con2=num*num*num



# print(f"{num} squared: {con}")

# print(f"{num} cubed: {con2}")

# num =int(float(input("enter digit:")))

# con= num*num
# con2=num*num*num



# print(f"{num} squared: {con}")

# print(f"{num} cubed: {con2}")


#3
# a = "100 + 21"
# print(a.split())




#4 

# print("Select Action")
# print("1. Create User")
# print("2. List User")
# print("3. Find USer")
# print("4.Remove User")
# print("5.Exit")
# option = input()
# print("#############################################")

# if option == 1 :


#5



# print("1990's".endswith("."))
# print("Hungry.".endswith("."))

# print("Hello".lower())

lines = None


with open('steve-jobs-speech.txt', "r" , encoding='UTF8') as f:
 
 
 
 lines = f.readlines()

word_list = []

word_list.extend(lines[0].split())

word_list.extend(lines[1].split())

word_list.extend(lines[2].split())



word_count_dict = {

}
for word in word_list:
    

   
    word_count_dict[word] = word_count_dict.get(word, 0) + 1
   
# 문자별로 가장 큰 밸류를 가진 키값은 무엇인가

for i in range(5) : 
    max_key = max(word_count_dict, key=word_count_dict.get)
    max_word = word_count_dict.pop(max_key)
    print(max_key, max_word)
    print(f"{i+1}번째{max_key}가 {max_word}번 나왔습니다.")
    

max_key = max(word_count_dict, key=word_count_dict.get)

word_count_dict.pop(str(max_key))

max_key2 = max(word_count_dict, key=word_count_dict.get)

word_count_dict.pop(str(max_key2))

max_key3 = max(word_count_dict, key=word_count_dict.get)

word_count_dict.pop(str(max_key3))

max_key4 = max(word_count_dict, key=word_count_dict.get)

word_count_dict.pop(str(max_key4))

max_key5 = max(word_count_dict, key=word_count_dict.get)











# 테스트용 출력문


#list.extend()
#.split()

