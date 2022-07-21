menu = 0
friends = []
while menu != 6:
    print('(9):--------연락처 관리 ----------')
    print('1. 연락처 입력\n2. 연락처 출력\n3. 연락처 조회\n4. 연락처 수정\n5. 연락처 삭제\n6.종료')

    menu = int(input('메뉴를 선택하시오: '))
    if menu == 1:
        name = input('이름을 입력하시오: ')
        phone = input('전화번호를 입력하시오: ')
        email = input('이메일을 입력하시오: ')
        friend = {'name': name, 'phone': phone, 'email':email}
        friends.append(friend)
    
    elif menu == 2:
        if len(friends) == 0:
            print('저장된 연락처가 없습니다.')
        
        else: 
            for f in friends:
                for key in f:
                    print(key, ':', f[key])
    
    elif menu == 3:
        print('1. 이름 검색')
        print('2. 전화번호 검색')
        print('3. 이메일 검색')
        c = int(input('검색할 종류를 선택하시오: '))
        if c == 1:
            _name = input('이름: ')
            for f in friends:
                if _name in f['name']:
                    for key in f:
                        print(key, ':', f[key])
        
        elif c == 2:
            _phone = input('전화번호: ')
            for f in friends:
                if _phone in f['phone']:
                    for key in f:
                        print(key, ':', f[key])
        
        elif c == 3:
            _email = input('이메일: ')
            for f in friends:
                if _email in f['email']:
                    for key in f:
                        print(key, ':', f[key])
        
    elif menu == 4:
        _name = input('수정할 연락처 이름을 입력하시오: ')
        for f in friends:
            if _name in f['name']:
                n = int(input('1. 이름, 2. 연락처, 3. 이메일: '))
                if n ==1:
                    new_name=input('수정할 이름: ')
                    f['name'] = new_name
                elif n ==2:
                    new_phone=input('수정할 연락처: ')
                    f['phone']=new_phone
                elif n==3:
                    new_email = input('수정할 이메일: ')
                    f['email'] = new_email

    elif menu == 5:
        _name = input('삭제할 연락처 이름을 입력하시오: ')
        for f in friends:
            if _name in f['name']:
                friends.remove(f)
            else:
                print('연락처 없음')
                