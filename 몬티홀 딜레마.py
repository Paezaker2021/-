import random
import os #cmd 멈춤
import math

#1이 나오면 성공, 그 외의 숫자가 나오면 실패

i=0
success=0
fail=0
t=0

print("\n")
print("\n")
print("\'몬티홀 딜레마\'")
print("\n")
print("\n")
print("당신이 한 게임 쇼에 참여하여 세 문들 중 하나를 고를 기회를 가졌다고 생각해봐라.")
print("\n")
print("한 문 뒤에는 자동차가 있으며, 다른 두 문 뒤에는 염소가 있다. 당신은 1번 문을 고르고,")
print("\n")
print("문 뒤에 무엇이 있는지 아는 사회자는 염소가 있는 3번 문을 연다. 그는 당신에게 \"2번 문을 고르고 싶습니까?\"라고 묻는다.")
print("\n")
print("당신의 선택을 바꾸는 것은 이득이 되는가?")
print("\n")
print("="*35)
print("\n")
print("\'몬티홀 딜레마\' 파이썬 확률 프로그램에 오신 것을 환영합니다.\n아래에 양수를 입력해주세요. 권장하는 숫자는 10의 배수 - 특히 1000, 10000, 100000을 권장합니다.\n로딩 중 숫자 표기가 어긋납니다. 이 점 참고 부탁드립니다.")
tries=int(input("입력 : "))

for i in range (tries):         #tries 만큼 실행

    sel_number= True
    picknumbera=0
    picknumberb=1
    picknumberc=2
    removenumber=0
    removenumberresult=0
    t=t+1

    print(tries,"번 중",t,"번 실행 중...\t|||\t참 : ",success," / 거짓 : ",fail," / 참 확률 :",round((success/tries)*100,2))
    
    while sel_number:           #a,b,c에 서로 다른 값을 지정함

        a=random.randint(1,3)
        b=random.randint(1,3)
        c=random.randint(1,3)


        if a!=b and a!=c and b!=c:
            sel_number=False


    pick=[a,b,c]                #배열 지정 및 1차 거르기



    if pick[0]==1:
        real=0
    elif pick[1]==1:
        real=1
    elif pick[2]==1:
        real=2

    picknumber=random.randint(0,2)
    picknumbera=pick[picknumber]

    for removenumber in range (3):

        if removenumber!=picknumber and removenumber!=real:
            removenumberresult=removenumber
            

        else:
            removenumber=removenumber+1


    del pick[removenumberresult]
    
    


    if pick.index(picknumbera)==0:
        picknumberb=1
    elif pick.index(picknumbera)==1:
        picknumberb=0

        
    if pick[picknumberb]==1:
        success+=1
        continue

    else:
        fail+=1
        continue

print("="*40)
print("최종 결과 - 참 :",success," / 거짓 :",fail," / 참 확률 :",(success/tries)*100)
os.system("pause")  
