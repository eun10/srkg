from ast import Num

class Calculator : # 부모에게 상속받으면 부모클래스의 것을 ()로 받음?
    sum = 100 # 클래스 변수 100
    def __init__(self):  # 첫번째 매개변수는 self로 쓰기. self에는 자신의 주소값을 받음(9행의 주소를 받음). self를 선언하긴 하지만 없는듯 하용
        self.result = 0 # 인스턴스 변수
    def add(self,num): # num은 지역변수 # 함수 안에서 self 안 붙고 쓰는 함수
        self.result +=num # num값 받은 것을 인스턴스 변수에 더한다 # num은 지역변수
        return self.result
# 인스턴스 변수 : 자기 값을 자기가 가짐. 객체별로 따로 저장
# 설계도 # 클래스에는 값과 함수(메소드)가 묶여 있음 
# 함수는 기능단위로 묶어 놓은 것
# 값이랑은 떨어져있어서 맞는 값을 넣어줘야 하고 
# 자기에게 필요한 값은 자기가 가지고 있음
# 

cal1 = Calculator() # call 변수에는 class로 만들어진 객체의 주소
cal2 = Calculator()
cal1.result = 2
cal2.result = 9

print(cal1.result)
print(cal2.result)
print(Calculator.sum)
Calculator.sum = 2001 # self가 붙지 않는 클래스 변수 : 클래스당 하나. # 클래스에 어떤 값을 하나만 정해두고 사용해야 할 때 
print(cal1.sum)
print(cal2.sum)
#인스턴스 변수는 객체마다 다른 값 # 클래스당 하나

cal1.add(3)
cal1.add(4)
print(cal1.result)
print(cal2.result)

class FourCal(Calculator):
    def sub(self,num) :
        self.result -= num
        return self.result

cal3 = FourCal()
cal4 = FourCal()

cal3.add(5) 
print(cal3.result)