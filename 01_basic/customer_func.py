# 함수
import re


def insertData(custlist) : 
    customer={'name':'','gender':'',"email":'',"birthyear":''}
    customer['name']=input("이름을 입력하세요 : ")
    while True:
            customer['gender']=input("성별(M/m 또는 F/f)을 입력하세요 : ")
            customer['gender']=customer['gender'].upper()
            if customer['gender'] in ('M','F'):
                break
    while True: # 중복되지 않게 입력
        regex = re.compile('^[a-z][a-z0-9]{4,10}@[a-zA-Z]{2,6}[.][a-zA-Z]{2,3}$')
        while True:
            customer['email']=input("이메일을 입력하세요 : ") 
            golbang = regex.search(customer['email'])
            if golbang:
                break
            else:
                print('"@"를 포함한 정확한 이메일을 써주세요')

        check=0
        for i in custlist:
            if i['email']==customer['email']:
                check=1
            
        if check==0:
            break
        print('중복되는 이메일이 있습니다.')    

    while True:
        customer['birthyear']=input("출생년도 4자리를 입력해주세요 : ")
            
        if len(customer['birthyear']) == 4 and customer['birthyear'].isdigit():
            break

    print(customer)
    custlist.append(customer)
    print(custlist)
    page=len(custlist)-1   
    print(page)
    return page # 1) 값을 반환 2) 종료
        # 리스트가 클래스로 되어있다? 
        # custlist(객체)는 주소값이, page는 값이 넘어옴
        # 주소는 변경사항 return 안 해도 됨(같은 주소에 작업을 했기 때문에)
        # 값은 변경사항을 return으로 받아야함
        # 다시 
        
def curData(custlist,page) :
    if page >= 0:   # 데이터가 있음
        print("현재 페이지는 {}쪽 입니다".format(page + 1)) 
        print(custlist[page])
    else:
        print("입력된 정보가 없습니다.")

def preData(custlist,page) :
    if page <= 0:
            print('첫 번 째 페이지이므로 이전 페이지 이동이 불가합니다')
            print(page)
    else:
        page -= 1
        print("현재 페이지는 {}쪽 입니다".format(page + 1))
        print(custlist[page])
    return page # 호출한 파일에 변경된 page 값을 보내줌

def nextData(custlist,page) :
    if page >= len(custlist)-1:
            print('마지막 페이지이므로 다음 페이지 이동이 불가합니다')
            print(custlist[page])
    else:
        page += 1
        print("현재 페이지는 {}쪽 입니다".format(page + 1))
        print(custlist[page])
    return page 


def deleteData(custlist) :
    choice1 = input('삭제하려는 고객 정보의 이메일을 입력하세요.')
    delok = 0
    for i in range(0,len(custlist)): # 데이터 개수만큼 반복
        if custlist[i]['email'] == choice1:
            print('{} 고객님의 정보가 삭제되었습니다.'.format(custlist[i]['name']))
            del custlist[i]
            print(custlist)
            delok = 1
            break
    if delok == 0:      # 지워지지 않으면
            print('등록되지 않은 이메일입니다.')
            print(custlist)
    return len(custlist)-1
        
def updateData(custlist) :
    while True:
        choice1=input('수정하시려는 고객 정보의 이메일을 입력하세요 : ') 
        idx=-1
        for i in range(0,len(custlist)):
            if custlist[i]['email'] == choice1:  
                idx=i  # 위치값을 넣어줌
                break
        if idx==-1:  # 변화가 없음 수정하지 못함
            print('등록되지 않은 이메일입니다.')       
            break
                        
        choice2=input('''
        다음 중 수정하실 정보를 골라주세요 
                name, gender, birthyear
        (수정할 정보가 없으면 'exit' 입력)
        ''')
        if choice2 in ('name','gender','birthyear'):
            custlist[idx][choice2]=input('수정할 {}을 입력하세요 :'.format(choice2))
            break
        elif choice2 =='exit':
            break
        else:
            print('존재하지 않는 정보입니다.')
            break

        # 수정이라 page의 값은 그대로이므로 return 필요 x
        
        # 데이터와 데이터를 처리하는 함수를 함께 가지고 있다?