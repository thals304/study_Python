# Python - Basic

### **print()**

- value을 출력
- sep : 출력되는 value들 사이 분리 기호
- end : 출력 문자열 마지막 문자
    - 기본 값 : 줄바꿈 (\n)

**print (value, sep=‘ ’, end=‘\n’, …)**

### 데이터 타입

**type(자료)**

**주요 데이터 타입(type)**

- **`int`** (정수): Integer(정수)의 약어이며, 정수를 나타내는 자료형
- **`float`** (실수): Floating point의 약어이며, 소수점이 있는 숫자를 나타내는 자료형
- **`str`** (문자열): 문자를 나타내는 자료형입니다. 작은 따옴표 혹은 큰 따옴표로 감싸져 있음
- **`bool`** (참/거짓): 참 또는 거짓을 나타내는 자료형입니다. True, False에서 T와 F는 반드시 대문자로 표기해야 함
- 아무것도 아닌 **`None`** 타입 : 말 그래도 아무 것도 아닌 흔히 Null 값을 넣는다고도 함

**타입 변경**

- **`float()`** : 타입을 float형으로 변환하기 위한 함수
- **`int()`**: 타입을 int형으로 변환하기 위한 함수
- **`bool()`** : 타입을 bool형으로 변환하기 위한 함수

### **리스트 (List) 생성**

**시퀀스, 집합형 자료구조**

| 분류 | 타입 | 특징 | 예시 |
| --- | --- | --- | --- |
| 시퀀스(sequence) | 리스트(list) | 순서가 있고, 가변(mutable) | [1, 2, 3] |
| 시퀀스(sequence) | 튜플(tuple) | 순서가 있고, 불변(immutable) | (1, 2, 3) |
| 세트(set) | 세트(set) | 순서가 없고, 중복을 허용하지 않음 | {1, 2, 3} |
| 맵(map) | 딕셔너리(dictionary) | 순서가 없고, key/value 쌍으로 이루어짐 | {‘a’: 1, ‘b’: 2, ‘c’: 3} |

리스트는 데이터의 요소를 순차적으로 파악하는데 용이한 자료형

리스트는 다양한 메서드(method) 혹은 함수를 지원하며 메서드를 활용하여 요소를 추가, 삭제 및 변경할 수 있음

**메서드(method)** : 객체(object)가 포함하는 함수 혹은 기능

**리스트 생성 방법**

```python
empty_list = []
empty_list = list()
```

리스트는 **`[]`** 혹은, **`list()`** 함수를 활용하여 생성할 수 있음

**값을 포함한 리스트 생성 방법**

```python
  value_list = [1,2,3,4,5]
```

리스트를 생성하며 값을 포함하기 위해서는 **`[]`** 괄호 내에 포함할 값을 함께 작성

### **리스트 규칙**

- list는 다양한 type의 데이터를 집합으로 가짐
- list안에 list도 허용
- list는 순서(order)의 개념이 존재

### **리스트 관련 함수**

- **`.`** 점 연산자로 함수를 실행할 수 있음
- 함수는 어떤 작업을 수행하는 코드를 모아 이름을 붙인 것

자세한 내용은 추후 함수 단원에서 배웁니다.

**리스트에 값 추가하기 : append()**

```python
mylist = []
mylist.append(값)
```

`append()`는 리스트에 값을 맨 뒤에 추가

`append()`로 값을 추가할 때는 중복된 값을 추가할 수 있으며, 추가한 순서가 유지됨됨

**리스트에 값 추가하기 : insert()**

```python
mylist = []
mylist.insert(index, 값)
```

`insert()`는 지정한 index에 값을 추가

**리스트 값 제거하기 : remove()**

```python
mylist = [1,2,3]
mylist.remove(제거할 값)
```

리스트에서 **첫 번째로** 나오는 해당 값을 삭제

**리스트에서 요소 꺼내기 : pop()**

```python
mylist = [1,2,3]
mylist.pop(index)
```

인덱스의 요소를 반환하고, 해당 요소는 삭제

**리스트 요소 개수 세기 : len()**

```python
len(리스트)
```

전체 항목의 개수를 반환

// 리스트 크기 출력할 때  print(len(리스트))

**리스트 값 정렬하기 : sort()**

```python
mylist = [1,3,2]
mylist.sort()
```

- 리스트의 요소를 순서대로 정렬 **(오름차순)**
- 내부적으로 정렬

```python
mylist = [1,3,2]
mylist.sort(reverse = True)
```

역정렬 (reverse order) = 내림차순도 가능 (reverse = True를 지정)

**리스트 확장하기 : extend()**

```python
mylist = [1,3,2]
mylist.extend(확장할 리스트)
```

// 확장할 리스트가 [4,5] 형식으로 들어가야 함

### **인덱싱(indexing) : 색인**

리스트는 인덱싱을 통해 각 요소의 값을 가져올 수 있음

예를 들어, my_list = [‘P’ , ‘Y’, ‘T’, ‘H’, ‘O’, ‘N’] 일 경우 리스트는 다음과 같이 색인할 수 있음

| ‘P’ | ‘Y’ | ‘T’ | ‘H’ | ‘O’ | ‘N’ |
| --- | --- | --- | --- | --- | --- |
| 0 | 1 | 2 | 3 | 4 | 5 |
| -6 | -5 | -4 | -3 | -2 | -1 |
- 인덱스는 0번부터 시작
- 파이썬은 음수 인덱싱(역수 인덱싱)을 지원

### **슬라이싱(Slicing) : 범위 추출**

**`[start:stop:step]`** 을 명시하여 리스트의 부분을 추출할 수 있음

**슬라이싱의 활용**

- **`[:]`** : 전체를 추출할 수 있음
- **`[start:]`** : 시작 index부터 끝까지 추출
- **`[:end]`** : 처음부터 **end 전**까지 추출
- **`[start:end]`** : start부터 **end 전**까지 추출

**indexing에 step 활용하기**

인덱싱에 step을 활용하여 부분적인 값 추출이 가능

```python
list[start:stop:step]
```

- step은 몇 칸씩 건너 뛰는지 지정
- step을 음수로 지정하면, 역순으로 확인

### **튜플 (tuple)**

- 리스트(list)는 가변(mutable)하는 객체(object)이지만, **튜플(tuple)은 불변(immutable)한 객체**

- 가변 객체는 요소에 대한 수정, 삭제, 변경 등이 가능하지만, 불변 객체는 **요소에 대한 수정, 삭제, 변경이 불가**

**튜플 생성하기**

```python
ex = tuple(1,2)
ex = 1,2
```

- **`tuple()`**, **`()`** 로 생성
- 혹은 **`,`** 로 생성할 수 있음

**단일 요소를 가진 튜플 생성하기**

```python
ex = 9,
ex = 9
```

- 단일 요소를 생성할 때는 반드시 **`,`** 를 붙여줌
- `(9,)`과 `(9)`는 다른 자료구조임을 꼭 알고 있어야 함

**튜플 언패킹 (unpacking)**

```python
one, two, three = 1,2,3
```

- 튜플로 여러 변수에 값을 한 번에 할당할 수 있음

### **튜플 (tuple)의 활용**

- 튜플 자료형은 요소의 추가, 삭제, 변경 등을 허용하지 않음

**튜플 요소의 조회**

```python
ex_tuple = (4,5)
print(ex_tupe[1]) # 인덱스 0(값: 4) 조회Copy
```

- 리스트와 동일하게 인덱스를 통한 요소 조회를 지원

**튜플 크기 조회**

```python
ex_tuple = (4,5)
print(len(ex_tuple))# 튜플 크기(크기: 2) 조회Copy
```

- 리스트와 동일하게 **`len()`**함수를 통해 크기 확인을 지원

**튜플 타입 변환**

```python
ex_tuple = (4,5)
print(list(ex_tuple))# tuple을 list로 변환

ex_list = [1,2,3]
print(tuple(ex_list))# list를 tuple로 변환Copy
```

- tuple형을 list형으로, list형을 tuple형으로 변환할 수 있음

- tuple형은 요소의 추가 및 삭제가 불가능하지만, list형은 요소의 추가 삭제가 가능

- 따라서, list로 type을 변경하면 요소의 추가 및 삭제가 가능 / list형에서 요소를 추가 및 삭제한 후 다시 tuple형으로 변경할 수 있음

### **세트(set)의 생성과 add()**

**시퀀스, 집합형 자료구조**

| 분류 | 타입 | 특징 | 예시 |
| --- | --- | --- | --- |
| 시퀀스(sequence) | 리스트(list) | 순서가 있고, 가변(mutable) | [1, 2, 3] |
| 시퀀스(sequence) | 튜플(tuple) | 순서가 있고, 불변(immutable) | (1, 2, 3) |
| 세트(set) | 세트(set) | 순서가 없고, 중복을 허용하지 않음 | {1, 2, 3} |
| 맵(map) | 딕셔너리(dictionary) | 순서가 없고, key/value 쌍으로 이루어짐 | {‘a’: 1, ‘b’: 2, ‘c’: 3} |
- 세트는 순서가 보장 되지 않음
- 세트는 요소의 **중복을 허용하지 않음**.

**세트 생성하기**

```python
exset = set()
exset = {}
```

세트는 **`set()`**혹은 **`{}`** 를 활용하여 생성할 수 있음

**세트에 값 추가하기**

```python
exset.add(값)
```

**`add()`**를 활용하여 세트에 값을 추가할 수 있음

**교집합 (intersection)**

- 교집합은 집합 A와 B가 주어졌을 때 공통된 요소
- **`&`** 기호나 **`intersection()`** 메서드를 활용하여 교집합을 구할 수 있음

**합집합 (union)**

- 합집합은 집합 A와 B가 주어졌을 때 집합 A, B 요소 모두를 포함
- **`|`**기호나 **`union()`** 메서드를 활용하여 합집합을 구할 수 있음

**차집합 (difference)**

- 두 집합에서, 하나의 집합에 포함되고 다른 집합에는 포함되지 않는 모든 원소의 집합.
- 연산자를 활용하거나 **`difference()`** 메서드를 활용하여 구할 수 있음

### **딕셔너리(dictionary) 생성 및 조회**

딕셔너리는 다음과 같은 특징을 가지고 있음

- 순서를 가지지 않음
- 키(key)와 값(value)의 쌍으로 이루어져 있음
- type은 dict로 표시 
- key를 사용하여 값을 조회할 수 있음
- 딕셔너리는 **수정, 삭제, 추가가 가능**

**딕셔너리 생성**

```python
ex_dict = dict() # 빈 딕셔너리 생성
ex_dict = {'a': 1, 2: 3} # 값을 포함한 딕셔너리 생성
```

- 딕셔너리는 여러 타입의 key를 가질 수 있음

**딕셔너리 값 조회**

```python
print(ex_dict['a'])# key 'a' 의 value(값 : 1) 조회
```

- key를 지정하여 딕셔너리 값(value)을 조회할 수 있음

**딕셔너리의 key 조회하기**

```python
mydict.keys()
```

- 모든 key를 조회할 수 있습니다. 하지만, 조회된**`dict_keys`**는 리스트(list)가 아님

이는 객체(object)로 생성되는데, 따라서 이를 list로 변경하기 위해서는 **`list()`**로 타입 변환을 하면 됨

**딕셔너리의 value 조회하기**

```python
mydict.values()
```

모든 value를 조회할 수 있음

**딕셔너리의 key-value 조회하기**

```python
mydict.items()
```

모든 key, value를 조회할 수 있습니다. 이 때, key, value는 튜플로 묶여서 조회됩니다.

**딕셔너리 값 다중 업데이트**

```python
ex_dict = {'a':1, 'b':2}

change_dict = {'c':3, 'd':4}

ex_dict.update(change_dict)# ex_dict의 key와 value들을 change_dict의 key와 value로 변경
```

**`update()`** 를 통해 값을 한꺼번에 업데이트 할 수 있음

**딕셔너리 값 변경**

```python
ex_dict = {'a':1, 'b':2}

change_dict = {'c':3, 'd':4}

ex_dict['a'] = 0 # ex_dict의 key 'a'의 value를 0으로 변경
```

key 값에 새로운 값(value)를 대입하여 값을 변경할 수 있음

**딕셔너리 key 제거**

```python
**ex_dict = {'a':1, 'b':2}

ex_dict.pop('a')#   key 'a' 를 제거하는 동시에 제거되는 key의 value를 반환
```

**`pop()`** 에 key를 지정하여 값을 제거할 수 있음

제거되는 값의 value를 반환

