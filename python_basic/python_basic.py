### 코테를 위한 Python 다시 공부
# 자료형
print(1)
print(3.14)
print('hello world')
print(True)
print(False)
print('3.14') # '' 안에 숫자를 출력하면 문자열
print('\n')

# 변수 : 어떤 값을 저장하는 변수
# 변수 선언 : 변수 이름 = 값
envelope1 = 10000
envelope2 = 20000
envelope3 = '파이팅'

print(envelope1)
print(envelope2)
print(envelope3)
print('\n')

# 변수 이름
# 문자, _로 시작 
# 문자, 숫자, _로 구성
# 공백 x, 특수문자 x
# 대소문자 구분
# 키워드(예약어) x
# 소문자 단어, _로 구분된 단어들 (권장)

# 형 변환
# int() -정수로 , float() - 실수로, str() - 문자로

num = int(float('2.5')) # 실수로 변경한 뒤에 정수로 변경해야 함 바로 int('2.5')로 하면 안됨
print(num) 
print('\n')

# 연산자
# 산술 연산자 
print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)  # 나누기
print(5 % 2)  
print(5 // 2) # 몫
print(5 ** 2) # 거듭제곱
print('\n')

# 비교 연산자 (True, False로 결과 출력)
print(5 > 2)
print(5 >= 2)
print(5 < 2)
print(5 <= 2)
print(5 == 2)
print(5 != 2)
print('\n')

# 논리연산자
print(3 < 5 and 7 < 5)
print(3 < 5 or 7 < 5)
print(not 3 < 5)
print('\n')

# 멤버 연산자
print('c' in 'cat')
print('c' not in 'cat')
print('\n')

# 불리안 형변환
# 값이 있으면 True, 없으면 False로 변환

# 문자 자료형
print(bool('a'))
print(bool(' '))
print(bool(''))   # '' : 값 없음
print('\n')

# 숫자 자료형
print(bool(1))
print(bool(-2))
print(bool(0))    # 0 : 값 없음

print(bool(None)) # None : 값 없음
print('\n')

# 인덱스와 슬라이싱
'''
    인덱스 
        - 몇 번째부터 시작
        - 파이썬 문자열, 리스트에서 사용
        - 0부터 시작
        - 마지막 값을 (-1로 보기도 함)
    
    슬라이싱
        - 잘라주는 역할
        - [x : y] : 인덱스 x부터 y 직전까지 자름 (y 포함 x)
        - [x :]   : x부터 끝까지
        - [: y]   : 처음부터 y 직전까지
        - [ : ]   : 처음부터 끝까지
'''
lang = 'PYTHON'
print(lang[0])
print(lang[-1])
print(lang[1:6])
print(lang[1 :])
print(lang[: 4])
print('\n')

# 문자열 처리
print(len('python'))
print('\n')

# 문자열 메소드
'''
    메소드(Method)
        - 클래스 내에 정의된 어떤 동작, 기능을 하는 코드들의 묶음
    문자열 메소드
        - 문자열.메소드()
        ex) 문자열.lower() : 문자열의 모든 문자를 소문자로 변환
            문자열.upper() : 문자열의 모든 문자를 대문자로 변환
            문자열.capitalize() : 문자열의 첫 문자만 대문자로 변환
            문자열.title() : 각 단어들의 첫 글자만 대문자로 변환
            문자열.swapcase() : 대소문자를 뒤바꿈
            문자열.split() : 문자열을 띄어쓰기 단위로 나누어 리스트 형태로 반환
            문자열.count('단어') : '단어'가 몇 번 쓰였는지 count
            문자열.startwith('단어') : 문자열이 '단어'로 시작하는지 확인(결과는 불리언으로 나옴)
            문자열.endswith('단어') : 문자열이 '단어'로 끝나는지(결과는 불리언으로 나옴)
            문자열.strip('단어') : 문자 앞 뒤로 불필요한 '단어' 제거 (단어를 아무것도 쓰지 않으면 공백 제거됨)
            문자열.replace('단어1','단어2') : 단어1을 단어2로 바꿈
            문자열.find('단어') : 특정 '단어'가 인덱스 기준으로 어디에 있는지 알려줌
            문자열.center('문자열 길이', '단어') : 다른 문자들 사이 기존 문자열 넣기

            // 이 외에 다른 문자열 메서드는 '파이썬 내장형'을 검색해서 공부하기
     ''' 

# 문자열 포맷
'''
    문자열 출력 방식
        - 방법1) print(문자열1 + 문자열2)
        - 방법2) print(문자열1 , 문자열2)
        - 방법3) 문자열 포맷 : {} + format 
                              {숫자} + format
                              f-string (파이썬 3.6 이상)
'''  
python = '파이썬'
java = '자바'
print(python + ' ' + java)
print(python, java)

print('개발 언어에는 ' + python + ',' + java + ' 등이 있어요.')
print('개발 언어에는', python , ',', java, '등이 있어요.')
print('개발 언어에는 {}, {} 등이 있어요.'.format(python,java))
print('개발 언어에는 {1}, {0} 등이 있어요.'.format(python,java))
print(f'개발 언어에는 {python}, {java}등이 있어요.')
print('\n')

# 탈출 문자 
'''
    탈출 문자
        - 역슬래시(\)와 특정 문자(숫자)의 조합으로 표현할 수 없는 기능이나 문자를 표시
        - 큰 따옴표 \" , 작은 따옴표 \'
        - 역슬래시 \\
        - 줄바꿈 \n
'''

print('하지만 \'나만 당할 순 없지\'라는 생각에 \"엄청 쉽지\" 라고 했다.')
print('C:\\Users\\pythonCoding')
print('파이썬은\n너무\n재밌어요.')
print('\n')

# 리스트
'''
    리스트
        - 서로 관련 있는 연속적인 데이터들 관리하는데 사용
        - 리스트 = [값1, 값2, 값3,...] 
        - 값 중복 허용 , 숫자/불리언/문자열 등 뭐든지 다 넣는 것 가능, 빈 리스트 생성 가능
        - list[인덱스] : 인덱스에 해당하는 값 출력 (리스트는 순서가 보장됨)
        > 슬라이싱도 가능 list[인덱스1 : 인덱스2] (리스트 형태로 출력)
        - 리스트에 포함되어 있는지 확인 : in 사용 (불리언으로 출력)
        - 리스트에 몇 개의 데이터가 있는지 확인 : len
        - 리스트 값 수정 : list[인덱스] = 수정할 값
        - 리스트 값 추가 : list.append('데이터')
        - 리스트 값 삭제 : list.remove('데이터')
        - 리스트 확장(다른 리스트를 더하려면) : list.extend(다른 list)
    '''

my_list = ['오예스' , '몽쉘', '초코파이', '초코파이']
any_list = [1, 2, 3.14, True, False, '아무거나']
empty_list = []

print(my_list[0])
print(my_list[0 : 2])
print('몽쉘' in my_list)
print(len(my_list))

my_list[0] = '오예스'
print(my_list)

my_list.append('몽쉘통통')
print(my_list)

my_list.remove('오예스')
print(my_list)

your_list = ['빅파이' , '오뜨']
my_list.extend(your_list)
print(my_list)
print('\n')

# 튜플
'''
    튜플
        - 튜플 = (값1, 값2,..)
        - 한 번 만들고 나면 수정/추가/삭제 불가
        - 읽기 전용 리스트
        - 중복 허용, 숫자/불리언/문자열 등 뭐든지 다 넣는 것 가능
        - 인덱스 (순서 보장) , 슬라이싱 가능
        - 포함 여부 in 가능, 길이 len 사용 가능 + count(), index()
        - 패킹 , 언패킹(* 사용 > *는 리스트로 출력!)
'''
my_tuple = ('오예스', '몽쉘', '초코파이') # 패킹
(pie1, pie2, pie3) = my_tuple # 언패킹

numbers = (1,2,3,4,5,6,7,8,9,10)
(one, two, *others) = numbers # others는 리스트!!
print('\n')

# 세트
'''
    세트
        - 순서 X, 중복 X
        - 세트 = {값1, 값2,...}
        - .intersection() : 교집합
        - .union() : 합집합
        - .difference() : 차집합
        - .add('데이터') : 값 추가
        - .remove('데이터') : 값 제거
        - .clear()  : 모든 값 제거 (값이 비어있는 set()이 됨)
        - del set변수 : 세트 완전 삭제 
        '''     
A = {'돈까스', '보쌈', '제육덮밥'}
B = {'짬뽕' , '초밥', '제육덮밥'}
print(A.intersection(B))
print(A.union(B))
print(A.difference(B))

A.add('닭갈비')
print(A)

A.remove('제육덮밥')
print(A)

A.clear()
print(A)

del A
# print(A)
print('\n')

# 딕셔너리
'''
    딕셔너리 (key, value)
        - key 중복 X
        - 딕셔너리 = {key1:value1, key2:value2,...}
        - 딕셔너리['key'] : 키에 대한 value 출력 (없는 key에 접근하면 error)
        - 딕셔너리.get()  : 없는 key에 접근하면 None 출력
        - 딕셔너리['key'] = value : 특정 key의 value 값 수정/추가
        - 딕셔너리.update({'key1' : valueA, 'key2' : valueB}) : 여러 개의 key에 해당하는 값 수정/추가
        - 딕셔너리.pop('key') : 특정  key의 value 삭제
        - 딕셔너리.clear() : 모든 데이터 삭제
        - 딕셔너리.keys() : 어떤 key들이 있는지
        - 딕셔너리.values() : 어떤 vlaue들이 있는지
        - 딕셔너리.items()  : 어떤 key, value들이 있는지
        '''

person = {
    '이름'   : '아무개',
    '나이'   : 13,
    '키'     : 130,
    '몸무게' : 30
}

print(person.keys())
print(person.values())
print(person.items())
print(person['이름'])
print(person['나이'])
print(person.get('별명'))
person['키'] = 140
person.update({'키' : 141 , '몸무게' : 36})
person.pop('몸무게')
person.clear()
print('\n')

# 자료형 비교
'''
    여러 값들을 순서대로 관리해야 되는 경우 = 리스트
    값이 바뀔 일이 없거나, 바뀌면 안되는 경우 = 튜플
    값의 존재 여부가 중요, 중복 안되는 경우 = 세트
    key를 통해 효율적으로 데이터를 관리하고 싶은 경우 = 딕셔너리
'''
# 자료형 변환
'''
    튜플도 수정, 추가, 제거 가능하려면?
     - list로 형변환 (list에서 tuple로 형변환 가능)
    리스트 중복 값을 제거하려면?
     - set로 형변환 (set에서 list로 형변환 가능)
    리스트 중복값을 제거하면서 순서를 보장하고 싶다면? 
     - 딕셔너리로 형변환 dict.fromkeys() (딕셔너리를 list로 형변환 가능)
    '''
change_list = list(my_tuple)
change_list.append('오뜨')
my_tuple = tuple(change_list)
print('\n')

change_set = set(my_list)
my_list = list(change_set)
print(my_list)
print('\n')

change_dict = dict.fromkeys(my_list)
print(change_dict)
my_list = list(change_dict)
print(my_list)
print('\n')

# if / if-else / elif 조건문
'''
    if 조건:
       true일 때 문장
    다음 문장
--------------------------------
    if 조건:
        true일 때 문장
    else:
        false일 때 문장
    다음 문자
---------------------------------
    // elif는 얼마든지 넣을 수 있음
    if 조건1:
        조건1이 true일 때 문장
    elif 조건2:
        조건1이 false & 조건2가 true일 때 문장
    else:
        조건1,2가 모두 false일 때 문장
    다음 문장
'''
today = '일요일'
if today == '일요일':
    print('게임 한 판')
print('공부 시작')
print('\n')

if today == '화요일':
    print('게임 한 판')
else:
    print('폰 5분만')
print('공부 시작')
print('\n')

if today == '일요일':
    print('게임 한 판')
elif today == '토요일':
    print('폰 5분만')
else:
    print('물 한 잔')
print('공부 시작')
print('\n')

# if 중첩
'''
    if 조건1:
        true일 때 문장
        if 조건2:
            true일 때 문장
    다음 문장

'''
yellow_card = 0
foul = True
if foul:
    yellow_card += 1
    if yellow_card == 2:
        print('경고 퇴장')
    else:
        print('조심')
else:
    print('주의')
print('\n')

# for 반복문
'''
    for 변수 in 반복 범위 또는 대상:
        반복 수행 문장
    ----------------------------------
    반복 범위
    range(stop) : 0 이상 ~ 'stop' 미만
    range(start, stop) : start 이상 stop 미만
    range(start, stop, step) : start 이상 stop 미만 step만큼 증가
    -----------------------------------
    반복 대상
    - 리스트 , 튜플 , 딕셔너리
    - 문자열
    (정수는 반복 대상으로 쓰일 수 없음)
'''
for x in range(10):
    print('팔 벌려 뛰기 해')

print('\n')

for x in range(10):
    print(f'팔 벌려 뛰기 {x}회')

print('\n')

for_list = [1,2,3]
for x in for_list:
    print(x)

for_tuple = (1,2,3)
for x in for_tuple:
    print(x)

for_dict = {'이름': '김아무', '나이' : 7, '키' : 120}
for v in for_dict.values():
    print(v)

for k in for_dict.keys():
    print(k)

for k,v in for_dict.items():
    print(k,v)

print('\n')

for_str = 'apple'
for x in for_str:
    print(x)

print('\n')

# while
'''
    while 조건:
        반복 수행 문장
'''
max = 25 # 최대 허용 무게
weight = 0 # 현재 캐리어 무게
item = 3 # 각 짐의 무게

while weight + item <= max:
    weight += item
    print('짐을 추가합니다')
print(f'총 무게는 {weight}입니다')
print('\n')

# break (반복문 탈출)
drama = ['시즌1', '시즌2', '시즌3', '시즌4', '시즌5']
for x in drama:
    if  x == '시즌3':
        print('재미 없대, 그만 보자')
        break
    print(f'{x} 시청')
print('\n')

# continue (어떤 동작을 건너 뛰고 싶을 때)
for x in drama:
    if x == '시즌3':
        print('재미 없대, 건너뛰자')
        continue
    print(f'{x} 시청')
print('\n')

# python 들여쓰기(indent) 매우 중요!

# 리스트 컴프리헨션 
'''
    리스트 컴프리헨션
     - 리스트에서 필요한 정보를 뽑아내거나 값을 바꿔 새로운 리스트로 만드는 방법
     - new_list = [변수 활용 for 변수 in 반복대상 if 조건] 
'''
products = ['JOA-2020', 'JOA-2021', 'SIRO-2021' , 'SIRO-2022']
recall = [] # 리콜 대상 제품 리스트
for p in products:
    if p.startswith('SIRO'): # 제품명이 SIRO로 시작하는가
        recall.append(p)
print(recall)

comprehension_recall = [p for p in products if p.startswith('SIRO')]
print(comprehension_recall)
print('\n')

# 함수
'''
    함수
        - 어떤 동작을 수행하는 코드들의 묶음
        - 여러 곳에서 사용되는 코드는 하나의 함수로
    함수 정의
     def 함수명():
        수행할 문장
    함수 호출
     함수명()
'''
def show_price(): # 함수 정의
    print('커트 가격은 10000원 입니다')

show_price() # 함수 호출
print('\n')

# 전달값
'''
    def 함수명(전달값):
        수행할 문장
    
    전달값 = 파라메타
        - 여러 개 사용 가능(콤마로 구분)
        - 함수 내에서만 사용
'''
def show_price(customer):
    print(f'{customer} 고개님')
    print('감성 커트 가격은 15000원 입니다')

customer1 = '나아무개'
show_price(customer1)
print('\n')

# 반환값
'''
    def 함수명(전달값):
        수행할 문장
        return 반환값
    
    반환값
        - 여러 개 반환 가능 (콤마로 구분, 튜플)
        - 반환되는 즉시 함수 탈출
'''
def get_price(is_vip): # 함수 정의
    if is_vip == True:
        return 10000 # 단골 손님
    else:
        return 15000 # 일반 손님

price = get_price(True) # 함수 호출
print('\n')

# 기본값
'''
    def 함수명(전달값 = 기본값):
        수행할 문장
    
    기본값
        - 전달값의 기본이 되는 값
'''
def get_price(is_vip = False): 
    if is_vip == True:
        return 10000 # 단골 손님
    else:
        return 15000 # 일반 손님

price1 = get_price(True)
price2 = get_price()
print('\n')

# 키워드값 : 전달값의 대상을 정해주는 것
def get_price(is_vip = False, 
              is_birthday = False,
              is_membership = False,
              card = False,
              review = False,
              first_time = False):
    return

price = get_price(review = True)
print('\n')

# 가변인자
'''
    - 전달값 개수가 바뀔 수 있는 인자
    - 전달값이 많으면 마지막 하나에서만 사용 가능
'''
# def visit(today, customer1, customer2 ...)
def visit(today, *customers): # 튜플 형태로 받음
    print(today)
    for customer in customers:
        print(customer)

visit('2022.06.10', 'aaa')
visit('2022.06.10', 'aaa', 'bbb')
print('\n')

# 지역변수
def secret():
    message = '이건 비밀' # 지역변수

# print(message) # 함수 안에서만 사용할 수 있는 지역변수

# 전역변수
message = '전역변수'

print(message) # 전역변수는 어디에서나 사용 가능

def no_secret():
    global message # 전역변수가 있으면 그걸 사용하고 없으면 지역변수 사용하겠다는 의미(수정 가능)
    # message = '이러면 다시 지역변수가 됨'
    print(message)
print('\n')

# 사용자 입력
name = input('예약자분 성함이 어떨게 되나요?')
print(name)
num = input('총 몇분이세요?') # str(문자열)로 데이터가 저장됨
if int(num) > 4: # 에러 발생 # 데이터 타입 불일치로 형변환 이용
    print('죄송하지만 저희 식당은 최대 4분까지만 예약 가능합니다.')

print('\n')

# 파일입출력
'''
    open(파일명, 열기모드, encoding='인코딩')
    <열기 모드>
    r : read
    a : append
    w : write
'''
f = open('list.txt', 'w', encoding='utf8') # 쓰기 모드로 파일 열기
f.write('김xx\n') # 문장 입력
f.write('정xx\n')
f.write('허xx\n')
f.close() # 파일 닫기 (필수)

f = open('list.txt', 'r', encoding='utf8') # 읽기 모드로 파일 열기
contents = f.read() # 파일 내용 다 읽어오기
print(contents)
f.close()

# 한 줄씩 읽어오기
f = open('list.txt', 'r', encoding='utf8')
for line in f:
    print(line, end='')
f.close()
print('\n')

# with : 블럭 벗어나면 자동으로 파일 닫음
# with 파일 쓰기
with open('list.txt', 'w', encoding='utf8') as f:
    f.write('hello\n')
    # f.close() 없어도 됨

# 클래스
'''
    클래스 
        - 설계도 + 설명서
        - 여러 변수/기능 포함시킬 수 있음
        - 클래스를 통해 만들어지는 제품 = 객체(object) = 클래스의 인스턴스
        - 형식   
            class 클래스명:
                정의
        - 서로 다른 두 멤버 변수는 서로 다른 값을 가질 수 있음
        - 멤버 변수는 없을 수도 있고 여러 개 있을 수도 있음
        - 특정 객체에 별도의 변수를 따로 추가하게 된다면 다른 객체에는 영향을 미치지 않음
        - self(객체 자기 자신)
            - 메소드를 정의할 때 처음 전달값은 반드시 self
            - 객체를 통해 메소드를 호출할 때 self 부분에 해당하는 전달값은 따로 명시 X
            - 메소드 내에서는 self.name과 같은 형태로 멤버변수 사용
'''
class BlackBox: 
    def __init__(self, name, price): # 메소드 # 객체가 생성될 때 자동으로 실행
        self.name = name   # 멤버변수
        self.price = price # 멤버변수
    
    def set_travel_mode(self, min):
        print(f'{self.name} {min} 분 동안 여행 모드 ON')

b1 = BlackBox('까망이', 2000000) # b1 객체
print(isinstance(b1, BlackBox))  # b1이 BlackBox의 인스턴스인지 확인하는 문장
print(b1.name, b1.price)
b1.nickname = '1호' # 특정 객체에 별도의 변수 추가
b1.set_travel_mode(20) # 메소드 실행 
BlackBox.set_travel_mode(b1, 20) # 위에 코드와 같은 결과
print('\n')

# 상속
'''
    - 부모 클래스 = 슈퍼 클래스 super() : 자식 클래스에서 부모 클래스의 메소드를 호출하기 위해 사용
    
     +) 다중 상속
     (클래스1, 클래스2,...)

'''
class TravelBlackBox(BlackBox): # BlackBox - 부모 클래스, TravelBlackBox - 자식 클래스
    def __init__(self, name, price, sd): # 부모 클래스 메소드를 사용 + 확장
        # BlackBox.__init__(self, name, price)
        super().__init__(name, price) # self는 쓸 필요 없음
        self.sd = sd

b2 = TravelBlackBox('하양이', 1000000)
b2.set_travel_mode(10)

class MailSender:
    def send(self):
        print('메일 발송')

class VideoBlackBox(BlackBox, TravelBlackBox, MailSender): # 다중 상속
    def make(self):
        print('추억용 여행 영상 제작')


b3 = VideoBlackBox('노랭이', 500000, 64)
b3.make()
b3.send()

# 메소드 오버라이딩(Overriding) : 부모 클래스의 메소드를 재정의
class AdvancedTravelBlackBox(VideoBlackBox):
    def set_travel_mode(self, min):
        print(str(min) + '분 동안 여행 모드 ON')
        self.make()
        self.send()

# pass : 클래스의 뼈대만 만들어 놓고 하나씩 메소드의 실제 동작을 구현할 수 있음
# for, while, 함수에서도 사용 가능 (if문은 X)
class A:
    def __init__(self):
        pass
    def record(self):
        pass
    def stop(self):
        pass
    def format(self):
        pass

# 예외 처리
'''
    try:
        수행 문장
    except:
        에러 발생 시 수행 문장
    else:
        정상 동작 시 수행 문장
    finally:
        마지막으로 수행할 문장 (에러 여부 상관 없이 항상 수행)
'''
num1 = 1
num2 = 0 # 에러 발생으로 except, finally 구문이 실행됨
try:
    result = num1 / num2
    print(f'연산 결과는 {result}입니다')
except ZeroDivisionError:
    print('0으로 나눌 수 없어요')
except TypeError:
    print('값의 형태가 이상해요')
except Exception as err: # 어떤 에러인지 확인 가능 
    print('에러가 발생했어요', err) 
else:
    print('정상 동작했어요')
finally:
    print('수행종료')

'''
    error 종류
    - except ZeroDivisionError > 0으로 나눌 수 없음
    - except TypeError > 값의 형태가 이상함
'''

# 모듈
'''
    모듈
        - 하나의 파이썬 파일 (.py)
        - 변수, 함수, 클래스 등 포함
    사용 방법
    1) import 모듈 > 모듈 전체를 가져옴
    2) from 모듈 import 변수,함수 또는 클래스 > 모듈 중 필요한 것만 가져옴

    ex) goodjob.py
         def say():
            print('참 잘했어요')
        
        새로운 파일
        (방법1)import goodjob
                goodjob.say()
        (방법2) from goodjob import say
                        say()
     - random
'''
import random
random_list = ['가위', '바위', '보']
print(random.choice(random_list))

# 패키지
'''
    패키지
        - 모듈이 여러 개 모인 것
     ex) goodCoding 파일
         goodjob.py
         def say():
            print('참 잘했어요')
         goodbye.py
         def bye():
            print('또 만나요')

          새로운 파일   
          (방법1) import goodCoding.goodjob
                  goodCoding.goodjob.say()

          (방법2) from goodCoding import goodbye
                  goodbye.bye()
            
          (한 번에 같이 쓰기) 
          from goodCoding import goodjob, goodbye
          goodjob.say()
          goodbye.bye()
'''
