
class CarClass : #클래스의 정의
    count = 0  #<함수와 동일한 들여쓰기의 변수를 지정한것

    
    def __init__(self, name, color, fuel, efficiency, mileage):
        self.name= name
        self.color= color
        self.fuel= fuel
        self.efficiency= efficiency
        self.mileage= mileage
        CarClass.count += 1

    def drive(self, miles):
        fuel_usage= int(miles / self.efficiency)

        if fuel_usage ==0 :
            fuel_usage +=1 
        if self.fuel < fuel_usage:
            print("insufficient fuel")
            return
        self.fuel-=fuel_usage
        self.mileage +=miles

car = CarClass("A6","silver",30,13,16000)      #인스턴스 클래스의 정의로 만들어진 
print(car.fuel)
car.drive(200)
print(car.fuel)


# print(car, "name")
# print(car, "color")
# print(car,"fuel")
# print(car,"efficiency")
# print(car,"mileage")

# isinstance(10,int) 인수가 인수의  타입이 동일하면 True를 반환
# type(10) 어떤 타입인지
                 

car_1 = {
    "name" :"a6" ,
    "color":"silver" ,
    "fuel" : 30 ,
    "efficiency": 13,
    "mileage" : 140000,

}

car_2 = {
    "name": "N20",
    "color": "silver",
    "fuel": 80,
    "efficiency": 9,
    "mileage": 160000,
}

def drive(car, miles):
    fuel_usage = int(miles/car["efficiency"])

    if fuel_usage==0 :
        fuel_usage +=1

    if car["fuel"] < fuel_usage:
        print("insufficient fuel")

    car["fuel"] -= fuel_usage 
    car["mileage"] +=miles

drive(car_1, 200) 

# print(car_1["fuel"])
# print(car_1["mileage"])


   
class ListStub:

    def __init__(self):
        self.list = []

    def append(self, item) :
        self.list.append(item)

    def extend(self, item_list) :
        self.list.extend(item_list)
    def pop(self) :
        return self.list.pop()

    def sum(self) :
        sum=0
        for item in self.list:
            sum+=item
        return sum
    
a=[1,2,3]
a= ListStub()
a.append