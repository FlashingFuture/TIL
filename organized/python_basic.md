# Python

- 간결하고 쉬운 문법 / 다양한 응용 분야 / 세계적 규모의 커뮤니티
- 인터프리터 언어

- #### Difference between interpreter and compiler

    - Compile : Runtime 이전에 기계어(Assembly code)로  변환 후 실행

    - interpreter : Runtime 이후에 줄 단위로 프로그램을 해석해 실행


### 표현식(Expression)

- 값 / 변수 / 연산자 등을 조합해 계산되고 결과를 내는 코드 구조

### 문장(Statement)

- 실행 가능한 동작을 표현하는 코드, 표현식을 포함하는 개념

# Data types

- 값의 종류 / 적용 가능한 연산, 동작을 결정하는 **속성**
- [Python Built-in types](https://docs.python.org/3/library/stdtypes.html)
## Numeric
int, float (real), complex (complex)
- float의 유한 정밀도 :
    - 실수(10진수)에 대한 2진수 근삿값을 찾음
    - floating point rounding error 발생
## Sequence
순서를 가지는 data type
- sequence : 값들이 순서대로 저장
- indexing : 값들에 고유한 index 존재
- slicing : index 범위를 조절해 부분적인 값 추출
- length : 저장된 값의 개수(길이) 계산 ( len() 이용 )
- iteration : 저장된 값들을 반복적으로 처리 가능
### text sequence : str (string)
- 문자들의 순서가 있는 변경 불가능한 시퀀스 자료형
- string interpolation : f-string
```bugs = 'roaches'
counts = 13
area = 'living room'
print(f'Debugging {bugs} {counts} {area}')
##Debugging roaches 13 living room
```
### list
여러 개의 값을 순서대로 저장하는 시퀀스 자료형
```python
list1 = []
list2 = [1, 'a', 3]
list3 = [1, 2, 'p', ['hello', 'world', '!']]
print(list3[-1][1][0]) # w
```
- 대괄호로 표기, 어떤 자료형도 저장할 수 있음
- 가변(내부 값이 변경될 수 있음)
### tuple
여러 개의 값을 순서대로 저장하는 **변경 불가능**한 시퀀스 자료형
```python
tuple1 = (1,)
tuple2 = (1, 'a', 3)
```
- 소괄호()로 저장 : 단 하나의 원소를 가지는 튜플은 ```(1,)``` 과 같은 형식으로 표현
- 불변 특성을 이용하여 안전하게 값 전달 / 그룹화 / 다중 할당 등 파이썬 내부 기능에 주로 사용됨
### range
- 연속된 정수 시퀀스를 생성하는 변경 불가능한 시퀀스
- ```range(n)``` 실행 시 0부터 n-1까지의 숫자의 시퀀스 생성

## Non-sequence types
### dict
```python
dict1 = {'key1' : 'value1', 'key2' : 'value2'}
print(dict1['key1']) # value1
```
key-value 쌍으로 이루어진 **순서와 중복이 없는 변경 가능**한 자료형
- key는 변경 불가능한 자료형만 사용 가능
- value는 모든 자료형 사용 가능
- json 형식과 유사한 형태로 표현됨
### set
```python
set1 = {1, 2, 3}
set2 = {3, 4, 2}
print(set1 | set2) # 합집합
print(set1 - set2) # 차집합
print(set1 & set2) # 교집합
```
- 순서와 중복이 없는 변경 가능한 자료형
- 중괄호{}로 표기 : 빈 set는 set()로 선언

## other data types
### None
```python
variable = None
```
- 값이 없음을 표현하는 자료형
### Boolean
```python
bool_1 = True
bool_2 = False
```
## Type conversion
```python
print(3 + 5.0)  # 8.0
print(True + False) # 1
```
- 암시적 형변환 : numeric, boolean type에 대해 같은 형으로 바꿔 서로 연산될 수 있도록 함
```python
print(int('1')) # 1
print(int('3.5')) # ValueError
```
- 명시적 형변환 : 개발자가 직접 형변환
  - str -> integer : 형식에 맞는 숫자만 가능
  - integer -> str : 모두 가능


## Operators

[Python Operator](https://docs.python.org/3/library/operator.html)
- 우선순위에 따른 연산자 정리

|     우선순위    	|             연산자            	|               내용             	|
|:---------------:	|:-----------------------------:	|:------------------------------:	|
|       높음      	|               ()              	|        소괄호   grouping       	|
|                 	|               []              	|        인덱싱,   슬라이싱      	|
|                 	|               **              	|             거듭제곱           	|
|                 	|             +,   -            	|     단항   연산자 양수/음수    	|
|                 	|          *,   /, //, %        	|          산술   연산자         	|
|      	|                          <<, >>   	|        비트 Shift
|      	|                          &  	|        비트 AND         	|
|      	|                          ^  	|        비트 XOR         	|
|      	|                          \|  	|        비트 OR         	|
|     |            +, -               	|          산술   연산자         	|
|                 	|     <,   <=, >, >=, ==, !=    	|          비교   연산자         	|
|                 	|          is,   is not         	|           객체   비교          	|
|                 	|          in,   not in         	|         멤버십   연산자        	|
|                 	|               not             	|           논리   부정          	|
|                 	|               and             	|            논리   AND          	|
|       낮음      	|               or              	|            논리   OR           	|

## Variable
```python
a = 'Hello, world!'
```
변수
- 값을 **참조**하는 이름 : 값이 저장된 객체의 메모리 주소를 가짐
- 변수에 값을 할당할 시 메모리 저장소 생성 / 변수에 저장된 메모리 주소 변경

### Style Guide

- 코드의 일관성과 가독성을 향상시키기 위한 **규칙 / 권장 사항들**
- [Style Guide documentation](https://peps.python.org/pep-0008/)

## 함수(Functions)
특정 작업을 수행하기 위한 재사용 가능한 코드 블록
- 함수를 사용하여 **재사용성**을 높이고 코드의 **가독성, 유지보수성** 향상

### Built-in function
[Built-in function](https://docs.python.org/3/library/functions.html)<br>
파이썬이 기본적으로 제공하는 함수


함수 호출(function call)
```python
function_name(arguments)
```
- 함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드 블록을 실행

### Docstring
```python
def func1(pram1, pram2):
  '''code explanations

  >>> func(1, 2)
  3
  '''
  return pram1 + pram2
```
[What is docstring?](https://peps.python.org/pep-0257/#what-is-a-docstring)<br>
함수를 설명해주는 문자열 리터럴

### Structure of function
```python
def whatup(name): # defined name : whatup, parameter : name
  '''입력된 값 앞에
  인삿말 what's up을 붙여주는 코드
  '''                               # docstring
  greeting = 'what\'s up, ' + name
  return greeting   # body : code of function

```
함수 반환 값(return)
- return 문은 함수의 실행을 종료하고, 결과를 호출 부분에 반환
  - 파이썬에서는 return이 없는 함수는 자동으로 None을 반환
매개변수(parameter)
- 함수를 정의할 때 함수가 받을 값는 나타내는 변수

인자(argument)
- 함수를 호출할 때 실제로 전달되는 값
- 위치 인자(Positional Arguments)
  - 함수 호출 시 인자의 위치에 따라 전달되는 인자
  - 기본 인자 값(Default Argument Values) : <br>함수 정의에서 매개변수에 기본 값을 할당
  ```python
  whatup(name = 'kim')
  ```
  - 키워드 인자(Keyword Arguments) : <br>함수 호출 시 인자의 이름과 값을 전달하는 인자
  ```python
  def sums(*args):
    print(args) # (1, 2, 3)
    print(f'합 : {sum(args)}') # 합 : 6
  ```
  - 임의의 인자 목록(Arbitrary Argument Lists) : <br>정해지지 않은 개수의 인자를 처리하는 인자
  - 매개변수 앞에 *를 붙여 사용하여, 인자들를 tuple로 묶어 처리함
  ```python
  def print_info(**kwargs):
    print(kwagrs)

  print_info(name='Chung', age=27)
  ```
  - 임의의 키워드 인자 목록(Arbitrary Keyword Argument Lists) : <br>정해지지 않은 개수의 키워드 인자를 처리하는 인자
  - 매개변수 앞에 **를 붙여 사용하며, 인자들을 dictionary로 묶어 처리함
  함수 인자 권장 작성순서
  - 위치 -> 기본 -> 가변 -> 가변 키워드

  a = func1(a)

### Scope
함수는 코드 내부에 local scope를 생성하고, 그 외의 공간은 global scope이다.
- global scope : 코드 어디에서나 참조할 수 있는 공간
- local scope : 함수 내부에서만 참조할 수 있는 공간
 - local scope에서 정의한 varible은 local variable

변수의 수명주기(lifecycle)
- 변수의 수명주기는 변수가 선언되는 위치와 스코프에 따라 결정
1. built-in scope
  - 파이썬이 실행된 후 영원히 유지
2. global scope
  - 모듈이 호출 시 생성 / 인터프리터가 끝날 때까지 유지
3. local scope
  - 함수 호출 시 생성 / 함수가 종료될 때까지 유지

이름 검색 규칙(Name Resolution)
- 파이썬에서 이름(식별자)들은 특정 이름공간(namespace)에 저장
- local -> enclosed -> global -> built_in scope 순으로 검색
```python
sum = 39

print(sum)  # 39
print(sum(range(7)))  # TypeError : 'int' object is not callable
```
- global scope에서 built-in scope에 존재하는 이름 사용 시 global scope에 있는 기능만 사용 가능해짐
```python
num = 0 # global variable

def inc():
  global num  # num을 전역변수로 선언
  num += 1

print(num)  # 0
inc()
print(num)  # 1
```
global : 변수의 스코프를 전역 범위로 지정

### Recursive function
재귀함수 : 함수 내부에서 자기 자신을 호출하는 함수
```python
def factorial(n):
  if n <= 1:
  # 종료 조건 : n이 1보다 작거나 같으면 1을 반환
    return 1
  # 재귀 호출 : n에 factorial(n - 1)을 곱한 결과를 반환
  return n * factorial(n - 1)
```
- 재귀함수는 종료 조건을 명확히 / 반복 호출 시 종료 조건을 향해가도록 만들어야 함

### Useful built-in functions
map(function, iterable)
```python
num = [1, 2, 3]
result = map(str, num)

print(result) # <map object at 0x00000239C915D760>
print(list(result)) # ['1', '2', '3']
```
- 순회 가능 데이터구조(iterable)의 모든 요소에 함수를 적용하고 결과를 map object로 반환

zip(*iterables)
```python
men = ['father', 'me']
women = ['mother', 'sister']
family = zip(men, women)

print(family) # 0x000001C76DE58700
print(list(family)) # ['father', 'me', 'mother', 'sister']
```
- 임의의 iterable을 모아 튜플을 원소로 하는 zip object 반환
### lambda
이름 없이 정의되고 사용되는 익명 함수
```python
add = lambda x, y: x + y

result = add(3, 5)
print(result) # 8
```
- 간단한 연산 / 함수를 한 줄로 표현하여 사용
## 
### Packing
여러 개의 값을 하나의 변수에 묶어서 담는 것
- 변수에 담긴 값들은 튜플(tuple) 형태로 묶임

  ```python
  packed_values = 1, 2, 3, 4, 5
  print(packed_values)  # (1, 2, 3, 4, 5)
  ```
### Unpacking
패킹된 변수의 값을 개별적인 변수로 분리하여 할당하는 것

'*'
- 패킹 연산자로써 : 여러 개의 인자를 하나의 튜플로 묶음
- 언패킹 연산자로써 : 시퀀스, iterable을 언패킹하여 함수의 인자로 전달
'**'
- 언패킹 연산자로써 : 딕셔너리의 키-값 쌍을 키워드 인자로 언패킹해서 함수의 인자로 전달

## Module
한 파일로 변수와 함수가 묶여 특정한 기능을 하는 코드가 작성된 파이썬 파일
```python
import math # accessing to module

print(math.pi) # 3.1419653589793
print(math.sqrt(4)) # 2.0
``` 
- Ex. math : 수학 관련 변수와 함수가 작성된 모듈
- Operator '.'(dot) : 점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아 참조하는 연산자
```python
from math import pi

print(pi) # 3.1419653589793
print(sqrt(4))  # NameError: name 'sqrt' is not defined
```
- from을 활용해 모듈에서 특정 요소만 import 가능
- 서로 다른 모듈이 같은 이름의 함수를 제공할 경우 마지막에 import된 이름으로 대체

패키지(Package)
- 관련된 모듈들을 한 디렉토리에 모은 것
- 모듈들의 이름공간을 분리해 충돌을 방지하고 모듈을 효율적으로 관리 / 재사용하기 위해 사용

파이썬 표준 라이브러리
[The Python Standard Library](https://docs.python.org/3/library/index.html)
- 파이썬과 함께 제공되는 모듈과 패키지의 모음

PIP(Package Installer of Python)
- 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템
```bash
pip install requests
```
```python
import requests

url = "https://apisite.com/api/version/users"
response = requests.get(url).json()

print(response)
```
- requests를 설치하고 import해 기능 사용이 가능해짐
```bash
pip list
```
- pip list를 통해 설치된 패키지 확인 가능

## Control Statement
제어문 : 코드의 실행 흐름을 제어하는 데 사용되는 구문
- **조건**에 따라 코드 블록을 실행하거나 **반복**적으로 코드를 실행함

### Conditional Statement
조건문 : 주어진 조건식을 평가하여 결과가 참(True)인 경우에만 코드 블록을 실행함
```python
if (x > 10):  # 조건 1
  print(x > 10) # code block 1
elif (x < 0): # 조건 2 : 조건 1이 만족되지 않았을 경우 평가
  print(x < 0) # code block 2
else:         # 위의 조건이 모두 False였을 경우 실행
  print(0 < x < 10) # code blcok 3
```
- 조건식을 위에서부터 순차적으로 비교

### Loop Statement
반복문 : 주어진 코드 블록을 여러 번 반복해서 실행하는 구문
for
```python
iterable = ['A', 'B', 'C']
for variable in iterable:  # for 변수 in 반복 가능한 객체
  print(variable) # code block

"""
A
B
C
"""
```
- 임의의 시퀀스의 항목들을 그 시퀀스에 들어 있는 순서대로 반복
- 반복 횟수가 명확하게 정해져 있는 경우 유용

while
```python
a = 3

while a > 0:
  print(a)
  a -= 1

print("finish")

"""
3
2
1
"""
```
- 주어진 조건식이 참(True)인 동안 코드 블록을 반복 실행 : 조건식이 거짓(False)가 될 때까지 반복
- 반복 횟수가 불명확 / 조건에 따라 종료해야 될 때 유용


break
```python
number = int(input('0을 입력 시 무한루프 탈출 : '))
while True:
  if number = 0:
    print('0 입력 확인')
    break
```
- 반복문을 즉시 중지하고 해당 반복문을 탈출

continue
```python
for number in range(1, 11):
  if number % 2 == 1:
    continue
  print(number)  # 짝수만 출력

"""
2
4
6
8
10
"""
```
- 현재 반복문의 남은 코드를 건너뛰고 다음 반복을 실행함
## 
### list comprehension
```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2)
```
```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num**2 for num in numbers]
```
- 더 간결하고 효율적으로 새로운 리스트 생성 가능
- 가독성이 떨어질 수 있음에 유의

### pass
아무런 동작도 수행하지 않고 넘어감
```python
def func1():
  pass
```
### enumerate
iterable 객체의 요소를 인덱스와 함께 반환하는 함수
```python
cities = ['서울', '대전', '광주', '구미', '부울경']

print(list(enumerate(cities)))

# [(0, '서울'), (1, '대전'), (2, '광주'), (3, '구미'), (4, '부울경')]
```

## Data Structure
데이터를 효과적으로 관리할 수 있는 구조
- 각 데이터 구조(str, list, dict, etc..)의 **메서드** 호출을 통해 다양한 기능을 활용
## method
객체에 속한 함수
- 객체의 상태 조작 / 동작 수행
- 파이썬에서 클래스 내부에 정의됨
  - 클래스는 타입을 표현하는 방법
```python
print(help(list)) # list 자료형에 대한 도움말
```
- help 함수를 통해 파이썬 내장 클래스(내장 자료형)의 메서드 확인 가능
```python
a = [1, 2, 3] # list type a 선언
a.append(4) # 객체.메서드() 형태로 메서드 호출
```
```객체(클래스).메서드()``` 의 형태로 사용됨

[Python built-in types](https://docs.python.org/3/library/stdtypes.html#str)
- 모든 파이썬 내장 클래스(자료형)들의 메서드 확인 가능


## sequence data structure
### string
**문자열 탐색 / 검증 메서드** 
|        메서드      	|                                         설명                                        	|
|:------------------:	|:-----------------------------------------------------------------------------------:	|
|      s.find(x)     	|     x의   첫 번째 위치를 반환. 없으면,   -1을 반환                                  	|
|      s.index(x)    	|     x의   첫 번째 위치를 반환. 없으면,   오류 발생                                  	|
|     s.isalpha()    	|     알파벳 문자 여부      *단순 알파벳이 아닌 유니코드 상 Letter (한국어도 포함)    	|
|     s.isupper()    	|     대문자 여부                                                                     	|
|     s.islower()    	|     소문자   여부                                                                   	|
|     s.istitle()    	|     타이틀   형식 여부                                                              	|

**문자열 조작 메서드**
- 문자열은 불변이기 때문에 새 문자열을 반환함
- [, count] 와 같은 표기는 선택 인자를 나타내는 것으로, [Extended Backus-Naur form](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_formview=msvc-170)에 따름(Python 문법이 아님!)

|                  메서드                 	|                                              설명                                            	|
|:---------------------------------------:	|:--------------------------------------------------------------------------------------------:	|
|       s.replace(old,   new[,count])     	|     바꿀 대상 글자를 새로운 글자로 바꿔서 반환                                               	|
|             s.strip([chars])            	|     공백이나 특정 문자를 제거                                                                	|
|     s.split(sep=None,   maxsplit=-1)    	|     공백이나 특정 문자를 기준으로 분리                                                       	|
|       'separator'.join([iterable])      	|     구분자로 iterable을   합침                                                               	|
|              s.capitalize()             	|     가장   첫 번째   글자를   대문자로   변경                                                	|
|                 s.title()               	|     문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로,      나머지는 소문자로 변환    	|
|                 s.upper()               	|     모두   대문자로 변경                                                                     	|
|                 s.lower()               	|     모두   소문자로 변경                                                                     	|
|               s.swapcase()              	|     대↔소문자 서로 변경                                                                      	|

### list
**리스트 값 추가 / 삭제 메서드**

|          메서드         	|                                                   설명                                                  	|
|:-----------------------:	|:-------------------------------------------------------------------------------------------------------:	|
|        **L.append(x)**      	|     리스트   마지막에 항목 x를   추가                                                                   	|
|        L.extend(m)      	|     Iterable m의   모든 항목들을 리스트 끝에 추가 (+=과   같은 기능)                                    	|
|     L.insert(i,   x)    	|     리스트   인덱스 i에 항목 x를 삽입                                                                   	|
|        L.remove(x)      	|     리스트   가장 왼쪽에 있는 항목(첫 번째)   x를   제거     항목이 존재하지 않을 경우,   ValueError    	|
|          **L.pop()**        	|     리스트   가장 오른쪽에 있는 항목(마지막)을   반환 후 제거                                           	|
|         **L.pop(i)**        	|     리스트의 인덱스 i에   있는 항목을 반환 후 제거                                                      	|
|         L.clear()       	|     리스트의 모든 항목 삭제                                                                             	|


**리스트 탐색 / 정렬 메서드**
|               문법              	|                                   설명                                 	|
|:-------------------------------:	|:----------------------------------------------------------------------:	|
|     L.index(x,   start, end)    	|     리스트에   있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환    	|
|            L.reverse()          	|     리스트의 순서를 역순으로 변경 (정렬 X)|
|             L.sort()            	|     리스트를 정렬 (매개변수   이용가능)                                	|
|            L.count(x)           	|     리스트에서 항목   x의 개수를 반환                                  	|


## Copy
파이썬에서는 데이터 분류(type)에 따라 복사 유형이 달라짐

### Assignment(할당)
```python
original_list = [1, 2, 3]
copied_list = original_list
print(original_list, copied_list) # [1, 2, 3] [1, 2, 3]

copied_list[0] = 'Py'
print(original_list, copied_list) # ['Py', 2, 3] ['Py', 2, 3]
```
할당(=) 연산자를 통해 객체에 대한 객체 참조를 복사함
### Shallow copy(얕은 복사)
```python
original_list = [1, 2, 3]
copied_list = original_list[:]  # slicing을 통해 새로운 객체를 복사하여 생성

copied_list[0] = 'Py'
print(original_list, copied_list) # [1, 2, 3] ['Py', 2, 3]
```
생성된(복사된) 객체는 원본 객체와 독립적으로 존재함
```python
original_list = [1, 2, [1, 2]]
copied_list = original_list[:]

copied_list[2][0] = 'Py'
print(original_list, copied_list) # [1, 2, ['Py', 2]] [1, 2, ['Py', 2]]
```
- 객체 내부에 변경 가능한 객체가 또 존재할 경우 그 객체에 대한 객체 참조를 복사(할당)함
### Deep copy(깊은 복사)
```python
import copy

original_list = [1, 2, [1, 2]]
deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2][0] = 'Py'
print(original_list, deep_copied_list) # [1, 2, [1, 2]] [1, 2, ['Py', 2]]
```
- 내부에 중첩된 객체까지 새로운 객체를 참조하도록 생성(복사)함

## Non-sequence Data Structure

### set
**항목 추가 / 제거 메서드**
|           메서드          	|                                설명                               	|
|:-------------------------:	|:-----------------------------------------------------------------:	|
|          s.add(x)         	|     세트 s에 항목   x를 추가. 이미   x가 있다면 변화 없음         	|
|          s.clear()        	|     세트 s의   모든 항목을   제거                                 	|
|         s.remove(x)       	|     세트 s에서   항목 x를 제거. 항목   x가 없을 경우 Key error    	|
|           s.pop()         	|     세트 s에서   랜덤하게 항목을 반환하고,   해당 항목을 제거     	|
|        s.discard(x)       	|     세트 s에서   항목 x를 제거                                    	|
|     s.update(iterable)    	|     세트 s에   다른 iterable 요소를   추가                        	|

**집합 메서드**
|              메서드            	|                                         설명                                       	|         연산자        	|
|:------------------------------:	|:----------------------------------------------------------------------------------:	|:---------------------:	|
|      set1.difference(set2)     	|        set1에는 들어있지만 set2에는      없는   항목으로 세트를 생성 후 반환       	|      set1   – set2    	|
|     set1.intersection(set2)    	|           set1과 set2 모두   들어있는 항목으로      세트를   생성 후 반환          	|     set1   & set 2    	|
|       set1.issubset(set2)      	|               set1의 항목이 모두 set2에 들어있으면      True를   반환              	|     set1   <= set2    	|
|      set1.issuperset(set2)     	|               set1가 set2의   항목을 모두 포함하면      True를   반환              	|     set1   >= set2    	|
|         set1.union(set2)       	|     set1 또는 set2에(혹은   둘 다) 들어있는      항목으로   세트를 생성 후 반환    	|     set1   \| set2    	|

### dictionary
**값 추가 / 반환 / 제거 메서드**
|            메서드           	|                                                                                설명                                                                              	|
|:---------------------------:	|:----------------------------------------------------------------------------------------------------------------------------------------------------------------:	|
|           D.clear()         	|     딕셔너리 D의   모든 키/값 쌍을 제거                                                                                                                          	|
|           **D.get(k)**          	|     키 k에   연결된 값을 반환 (키가 없으면 None을 반환)                                                                                                          	|
|         **D.get(k,   v)**       	|     키 k에   연결된 값을 반환하거나 키가 없으면 기본 값으로 v를 반환                                                                                             	|
|           **D.keys()**          	|     딕셔너리 D의   키를 모은 객체를 반환                                                                                                                         	|
|          **D.values()**         	|     딕셔너리 D의   값을 모은 객체를 반환                                                                                                                         	|
|           **D.items()**         	|     딕셔너리 D의   키/값 쌍을 모은 객체를 반환                                                                                                                   	|
|           D.pop(k)          	|     딕셔너리 D에서   키 k를 제거하고 연결됐던 값을 반환 (없으면   오류)                                                                                          	|
|         D.pop(k,   v)       	|     딕셔너리 D에서   키 k를 제거하고 연결됐던 값을 반환 (없으면   v를 반환)                                                                                      	|
|        D.setdefault(k)      	|     딕셔너리 D에서   키 k와 연결된 값을 반환                                                                                                                     	|
|     D.setdefault(k,   v)    	|     딕셔너리 D에서   키 k와 연결된 값을 반환     k가   D의 키가 아니면 값 v와   연결한 키 k를 D에   추가하고 v를 반환                                            	|
|        D.update(other)      	|     other 내 각 키에 대해 D에   있는 키면 D에 있는 그 키의 값을 other에 있는 값으로 대체.     other에 있는 각 키에 대해 D에   없는 키면 키/값 쌍을 D에   추가    	|

## Hash table
해시 함수를 사용해 변환한 값을 색인(index)로 key와 value를 저장하는 자료구조
- 해시(Hash) : 임의의 크기의 데이터를 고정된 크기의 값으로 바꾸는 것
- 해시 함수 : 임의의 길이의 데이터를 입력받아 고정된 길이의 데이터(해시 값)을 출력하는 함수
- 데이터 검색을 더 빠르게 함

### hash table in set / dictionary
set의 요소 / dict의 key는 해시 함수를 통해 해시 값으로 변환되어 해시 테이블에 저장됨
- set의 요소가 정수인 경우 그 값을 그대로 해시 값으로 사용
- 문자열은 가변적인 길이 때문에 해시 값이 실행 시마다 다르게 계산됨
- set.pop() is **arbitrary**, NOT random

hash table의 값은 변해서는 안됨(무결성 유지)
- 가변 데이터(list)는 hash할 수 없음

## Procedural Programming
절차 지향 프로그래밍 : 프로그램을 '데이터' / '절차' 로 구성하는 프로그래밍 패러다임
- 함수(절차) 호출과 코드의 흐름이 중요
- Software Crisis : HW의 발전과 함께 계산용량 / 문제의 복잡성이 급격히 커짐에 따라 절차지향 프로그래밍에 문제 발생
(절차 안에 하나라도 문제가 있으면 절차 전체가 동작하지 않음)

## Object Oriented Programming
객체 지향 프로그래밍 : 데이터와 해당 데이터 조작 메서드를 하나의 객체로 묶어 관리하는 프로그래밍 패러다임

- **객체 지향은 절차 지향과 대조되는 개념이 아닌** 절차 지향을 기반으로 객체라는 개념을 도입해 상속 / 코드 재사용성 / 유지보수성 등에서 이점을 갖는 패러다임임

## Class
파이썬에서 자료형(type)을 표현하는 방법
```python
class str(Sequence[str]):
    @overload
    def __new__(cls, object: object = ...) -> Self: ...
    @overload
    def __new__(cls, object: ReadableBuffer, encoding: str = ..., errors: str = ...) -> Self: ...
    @overload
    def capitalize(self: LiteralString) -> LiteralString: ...
    @overload
    ...
```

## Object
클래스에서 정의한 내용을 메모리에 할당한 것으로 **속성(변수)**과 **행동(메서드)**으로 구성된 모든 것
- 넓은 개념으로 메모리에 할당된다면 모두 객체라고 할 수 있음
- 인스턴스 : 클래스로 만든 객체
  - 하나의 객체는 특정 자료형(type)의 인스턴스임

객체의 특징
- 타입(type) : 어떤 연산자(operator)와 조작(method)가 가능한가?
- 속성(attribute) : 어떤 상태(데이터)를 가지는가?
- 조작법(method) : 어떤 행위(함수)를 할 수 있는가?

```python
class Person:
    # attribute
    blood_color = 'red'
    # constructor function
    def __init__(self, name):
        self.name = name  # instance variable

    def breathing(self):
        return f'{self.name} is breathing.'
    
# creating instance
human1 = Person('Kim')

# calling method
print(human1.breathing()) # Kim is breathing

# access to attribute 
print(human1.blood_color) # red

# calling method
print(human1.breathing())
```
생성자 함수(constructor function) : ```__init__```
- 객체를 생성할 때마다 자동으로 호출되어 객체를 초기화

인스턴스 변수 : ```self.~```
- 인스턴스마다 별도로 유지되는 변수

인스턴스와 클래스 간의 이름공간(namespace)
- 인스턴스를 만들 시 인스턴스 객체에 독립적인 이름 공간 생성
- 특정 속성 접근 시 인스턴스 객체 내부 -> 클래스 내부 순으로 탐색
- 독립적인 이름공간을 이용해 클래스와 인스턴스는 다른 객체들과의 상호작용에서 충돌 / 영향 없이 독립적으로 동작할 수 있음

클래스 변수
```python
class Circle():
  pi = 3.14

  def __init__(self, r):
    self.r = r

c1 = Circle(5)
c2 = Circle(10)
  ...
```
```python
c2.pi = 5
print(Circle.py)  # 3.14
print(c1.py)  # 3.14
print(c2.py)  # 5
```
- 클래스 전체에 적용되는 변수
- ```클래스명.클래스변수``` 형식으로만 변경 가능

### instance method
인스턴스 메서드 : 인스턴스의 상태를 조작하거나 동작을 수행
```python
class Myclass():

  def instance_method(self, arg1, ...):
    pass
```
- 반드시 첫 번째 매개변수로 인스턴스 자신(self)를 전달받음

### constructor method
생성자 메서드 : ```__init__``` 매직 메서드로 객체가 생성될 때 자동으로 호출되는 메서드
- 객체들의 초기값을 설정

### class method
클래스 메서드 : 클래스가 호출하는 메서드
- 클래스 변수 조작 / 클래스 레벨에서의 동작 수행
```python
class Myclass:

  @classmethod
  def class_method(cls, arg1, ...)
    pass
```
- @classmethod 데코레이터를 사용해 정의
- 호출 시 첫 번째 인자로 호출하는 클래스(cls) 전달
- 상속 시 해당 클래스만 조작할 수 있도록 이용(```클래스명.메서드``` 사용 시 상속된 클래스 때문에 기능 이용이 안됨)

### static method
정적 메서드 : 클래스, 인스턴스와 관계없이 동작하는 메서드
- @staticmethod 데코레이터를 사용하여 정의
- 필수 매개변수가 없음 : 객체 상태 / 클래스 상태를 수정하지 않고 기능(동작)만을 위한 메서드

**각 메서드는 OOP 패러다임에 따라 목적에 맞게 설계된 것이기에 목적에 맞는 메서드만 사용해야 함**

### magic method
특정 상황에 자동으로 호출되는 메서드
- ```__```(Double underscore)가 있는 메서드는 특수 동작을 위해 만들어진 메서드

### decorator
다른 함수의 코드를 유지한 채 수정 / 확장하기 위해 사용되는 함수
```python
def my_decorator(func):
    def wrapper():
        # 함수 실행 앞에 수행할 작업
        print('before function')
        # 함수 호출
        result = func()
        # 함수 실행 뒤에 수행할 작업
        print('after function')
        return result

    return wrapper
```
```python
@my_decorator
def my_function():
    print('func()')

my_function()
"""
before function
func()
after function
"""
```

## Inheritance
상속 : 기존 클래스의 속성과 메서드를 물려받아 새 하위 클래스를 생성하는 것
- 코드 재사용성을 늘려 중복된 코드를 줄일 수 있음
- 부모 / 자식 클래스 간 계층 구조를 형성해 더 구체적인 클래스를 만들 수 있음
- 문제가 발생할 경우 해당 클래스만 수정하면 되어 유지 보수가 용이함
```python
class Stick:
    def __init__(self, damage):
        self.damage = damage

    def attack(self):
        print(f'damage : {self.damage}')

class Axe(Stick):
    def __init__(self, stick_damage, rock_damage):
        self.damage = stick_damage + rock_damage
```
```python
a = Stick(10)
b = Axe(10, 30)
a.attack()
b.attack()
"""
damage : 10
damage : 40
"""
```

```python
super()
```
부모 클래스 객체를 반환하는 내장 함수
- ```super()```를 사용해 다중 상속

### multiple inheritance
다중 상속 : 둘 이상의 상위 클래스로부터 상속받는 것

다이아몬드 문제(diamond problem)
- 클래스 B, C가 A에서 상속되고, 클래스 D가 B, C에서 상속될 때 상속 순서의 문제
- 파이썬에서는 MRO(Method Resoulution Order) 알고리즘 사용
    - 깊이 우선, 왼쪽에서 오른쪽으로 중복 없이 클래스를 검색
    - ```super()```가 MRO를 기반으로 호출될 메서드를 결정하여 자동으로 호출

```python
class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')


class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')


class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()  # self.value_a = 'ParentA'
        self.value_c = 'Child'

    def show_value(self):
        super().show_value()    # Value from ParentA: ParentA
        print(f'Value from Child: {self.value_c}')  # Value from Child: Child


child = Child()
child.show_value()
```

super 호출 시 call stack
```python
class A:
    def __init__(self):
        print('A Constructor')


class B(A):
    def __init__(self):
        super().__init__()
        print('B Constructor')


class C(A):
    def __init__(self):
        super().__init__()
        print('C Constructor')


class D(B, C):
    def __init__(self):
        super().__init__()
        print('D Constructor')


obj = D()

print(D.mro())
"""
A Constructor
C Constructor
B Constructor
D Constructor
[<class '__main__.D'>, 
<class '__main__.B'>, 
<class '__main__.C'>, 
<class '__main__.A'>, 
<class 'object'>]
"""
```
- ```mro()``` : 해당 인스턴스가 어떤 부모 클래스를 가지는지 확인하는 메서드
- super()는 MRO 상에서 다음으로 탐색할 클래스의 인스턴스로, 코드 재사용성을 늘려줌


## Errors and Exceptions
버그(bug) : 소프트웨어에서 발생하는 오류 또는 결함
디버깅(debugging) : 버그를 찾아내고 수정하는 과정, 프로그램의 오작동 원인을 식별하여 수정하는 작업 
- print 활용(코드를 bisection으로 나누기), 개발환경 기능 활용, python tutor 활용

### Error
에러 : 프로그램 실행 중 발생하는 예외 상황
Syntax Error : 구문(문법)이 올바르지 않은 경우 발생
  - Invalid syntax, assign to literal, EOL(End of Line, EOF(End of File))
Exception : 프로그램을 실행했을 때 감지되는 에러<br>
[Pyhon Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- Built-in Exceptions : 파이썬에서 이미 정의된 예외 상황의 처리를 위해 사용되는 클래스
- ZeroDivisionError, NameError, TypeError, ValueError, IndexError, KeyError, ModuleNotFoundError, ImportError, KeyboardInterrupt, 
IndentationError 등

### User-defined Exception
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')

# 0으로 나눌 수 없습니다.
```
try-except 구조를 사용해 예외 처리
- try 블록 : 예외가 발생할 수 있는 코드
- except 블록 : 예외가 발생했을 때 처리할 코드

- 내장 예외 클래스는 상속 계층구조를 가지기 때문에 반드시 하위 클래스를 먼저 확인하는 구조로 작성해야 함

as
```python
my_list = []

try:
    number = my_list[3]
except IndexError as error:
  print(f'{error} 발생')

# list index out of range 발생
```

### EAFP & LBYL
```python
my_dict = {}
# try-except
try:
    result = my_dict['a']
    print(result)
except KeyError:
    print('Key가 존재하지 않습니다.')

# if-else
if 'key' in my_dict:
    result = my_dict['a']
    print(result)
else:
    print('Key가 존재하지 않습니다.')
```
EAFP(Easier to Ask for Forgiveness than Permission)
- 예외처리를 주임으로 코드를 작성하는 방식(try-except)
- 예외 상황을 예측하기 어려울 경우 유용
LBYL(Look Before You Leap)
- 값 검사를 중심으로 코드를 작성하는 방식(if-else)
- 코드의 예측 가능성이 높지만 더 길고 복잡해질 수 있음