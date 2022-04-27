# archery_mixed= ("안산","김우진")
# archery_mixed_woman, archery_mixed_man = archery_mixed #tuple 을 unpack 자신이 들고있는 데이터를 여러 변수에 할당 할 수 있음

#print(archery_mixed_man)
#print(archery_mixed_woman)


#연습문제 1

user_id = ['love77', 'hani900','random123']
user_id.append('hooni')
print(user_id)

#연습문제 2
user_id = ['love77','hani900','random123','hooni']
user_id.pop(3)
print(user_id)

#연습문제 3

#user_id.index("hooni")
#print(user_id.index("hooni")) 

#연습문제 4

numbers = [1,3,10,2,4,8,7,6]
print(numbers.sort())

#

#연습문제 1

school = {
 "class_a":{
 "student_1":{
 "name":"Mike",
 "marks":{
 "physics":70,
 "history":80
 }
 }
 }
}


changed = school["class_a"]["student_1"]["marks"]["history"]
changed = 95
print(school["class_a"]["student_1"]["marks"]["history"])
#school["class_a"]["student_1"]["name"]["marks"]=95
#school.get["class_a".get[]].update



#print(["school"])

#연습문제2 

student = {
 "name": "hooni",
 "class": 9,
 "marks": 75
}

student.remove("name")
print(student)

#연습문제 3

user_oh = {
 "name": "오진혁",
 "event": "archery",
 "age": 40,
 "height": 182,
}

keys = list(user_oh.keys())  
values = list(user_oh.values())

print(f"오진혁 선수의 key 값은",{keys},"이고 values 값은", {values},"입니다.")


#연습문제 1
a = 1
b = 3

print(f)

#ath