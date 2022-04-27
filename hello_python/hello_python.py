
#print("")

#print ("name:\t\t코딩왕\nage:\t\t28\nevent:\t\t개발자\nnationality:\tKorea, Republic of")

#a= int(input("투자금액을 입력해주세요($단위):"))
#b= int(input("예상 수익률을 입력해주세요 (%단위):"))

#print(f"예상되는 수익은{int(a*b*0.01)}$입니다.")


#a= input("첫 번째 값을 입력해 주세요.:")
#b= input("두 번째 값을 입력해 주세요.:")

#print(a==b)

#print("안녕하세요 제 이름은 '한상훈\"입니다.\n감사합니다.")



#a= int(input("투자금액을 입력해주세요($단위):"))
#b= int(input("예상 수익률을 입력해주세요 (%단위):"))

#print(f"예상되는 수익은 ($):\n철수는 {a}$를 투자해 {b}%의 이익을 즉{int(a*b*0.01)}$를 얻게됩니다.")

# python_collection = [list , dictionary, Tuple]

# a= list; 순서가 존재하는 데이터의 나열 0,1,2...
 # 처음에 숫자가 들어가도 스트링이 중간에 들어가도 상관이없고 하나의 변수 로 저장할수 있다.

#atheletes = [
#  "안산" , "오진혁" , 1, True
#]
 #데이터는 콤마로 구분_ 

#print(a_list[0])
#print(a_list[1])
#print(a_list[2])
#print(a_list[3]) [] 대괄호로 쓴다.

#콜론을 통해서 인덱스 범위를 지정할 수 있다, 2는 포함하고 4는 포함하지 않는다
#print(a_list[2:4])
#문자 열도 하나의 나열 문자열도 리스트다.

#print("hello world"[0:6])

#athletes= ["오진혁", "안산 ", "황선우", "서채현"]

#print(len(athletes))

#athletes.append("우상혁")
#athletes.append("김선우")

#athletes_gym =["신재환", "여서정"]
#athletes.extend(athletes_gym)

#athletes.append("기보배")
#narrator=athletes.pop() #가장 마지막 데이터를 제거한다. 결과를 돌려준다.
#gym_gold_medalist = athletes.pop(6) #index6 7번째 데이터를 지운다.

#athletes.append("여홍철")
#athletes.remove("여홍철") #동일한 아이템을 지워준다. 무엇을 제거할지 지정해야한다. 순서대로 확인해서 가장 작은 인덱스를 가진 아이템을 제거한다. 값이 돌려주지 않는다.

#athletes.index("황선우")

#print(athletes.index("황선우"))

#list=[]

#dictionary

#athletes_oh= {
  #"이름":"오진혁",#콤마로 엔트리 혹은 아이템 구분한다.
  #"키":"밸류" #키와 밸류 한줄을엔트리 혹은 아이템이라 부른다
  #"age":"12"}

athlete = {
    "name": "오진혁",
    "event": "archery",
    "age": 40,
    "height": 182,
    "participated": [
        "2012 London Olympics",
        "2020 Tokyo Olympics",
    ],
    "medals": [
        {
            "games": "2012 London Olympics",
            "event": "archery",
            "competition": "men individual",
            "medal": "gold"
        },
        {
            "games": "2012 London Olympics",
            "event": "archery",
            "competition": "men's team",
            "medal": "bronze"
        },
        {
            "games": "2020 Tokyo Olympics",
            "event": "archery",
            "competition": "men's team",
            "medal": "gold"
        }
    ],
}

#athlete["name"]
#athlete.get("name") #밸류를 호출

#athlete.update({"birth":"1981-08-15"}) #키에해당하는 밸류를 갱신

#athlete.pop("birth") # 밸류를 꺼내고 딕셔너리에서 제거

#print(athlete.keys())

#participated_games = athlete["participated"]
#print(participated_games[0])
#print(athlete["medals"][0]["games"])
#print(athlete["medals"][0]["medal"])

#Tuple 순서가 정해진 고정된 데이터 immutable

arhery=("김우진", "안산")

