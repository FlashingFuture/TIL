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
|                 	|             +,   -            	|          산술   연산자         	|
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