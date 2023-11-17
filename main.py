class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price #이름과 가격을 속성으로 가지는 Beverge 클래스를 정의

    def calculate(self,number):
        totalprice = self.price * number
        return totalprice #전체 가격을 계산하는 calculate함수 정의

Coffee = Beverage("커피", 3000)
Greentea = Beverage("녹차", 2500)
IceTea = Beverage("아이스티", 3000) #3가지 음료메뉴의 이름과 가격 생성

while True:
    selected_beverage = input("음료를 골라주세요")
    if selected_beverage =="커피":
        break
    elif selected_beverage =="녹차":
        break
    elif selected_beverage =="아이스티":
        break
    else:
        print("음료를 골라주세요")
        #정확한 음료이름을 집어넣었을때만 수량을 입력하는 단계로 넘어갈수 있는 while문 생성

number = int(input("음료 갯수를 선택해주세요")) #음료의 수량을 입력받을 input()함수

Beverage_choice = None #선택한 음료의 초기값을 None으로 설정
if selected_beverage == "커피":
    Beverage_choice = Coffee
elif selected_beverage == "녹차":
    Beverage_choice = Greentea
elif selected_beverage == "아이스티":
    Beverage_choice = IceTea #선택한 음료 정보를 Beverage_choice에 대입

totalprice = Beverage_choice.calculate(number)
print(f"총 가격은 {totalprice} 입니다") #전체 가격을 계산해준 뒤 총 가격을 알려주는 문장출력

#Q.음료를 한 종류가 아닌 여러종류 음료를 선택하고 싶은 경우에 어떤 코드를 추가해야 하는지 궁금합니다