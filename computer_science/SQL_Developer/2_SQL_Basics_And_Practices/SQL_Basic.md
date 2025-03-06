# SQL 기본

## Data Control Language

DCL: 데이터베이스에 접근하고 객체들을 사용하도록 권한을 주고 회수하는 명령어

```sql
SELECT [ALL/DISTINCT] 컬럼명, 컬럼명, ...
FROM 테이블명;
```

- ALL: Default 옵션, 중복된 데이터가 있어도 모두 출력
- DISTINCT: 중복된 데이터가 있는 경우 1건으로 처리하여 출력

```sql
WHERE 컬럼명 비교연산자 [문자/숫자/표현식] 비교컬럼명(JOIN 사용 시)
```

- NULL 값과의 연산은 NULL을 리턴
- NULL 값과의 비교연산은 거짓(FALSE) 리턴

| 연산자 종류      | 연산자           | 설명                                   |
| ---------------- | ---------------- | -------------------------------------- |
| 비교 연산자      | =                | 두 값이 같으면 참                      |
| 비교 연산자      | !=               | 두 값이 다르면 참                      |
| 비교 연산자      | >                | 왼쪽 값이 크면 참                      |
| 비교 연산자      | <                | 왼쪽 값이 작으면 참                    |
| 비교 연산자      | >=               | 왼쪽 값이 크거나 같으면 참             |
| 비교 연산자      | <=               | 왼쪽 값이 작거나 같으면 참             |
| SQL 연산자       | BETWEEN          | 특정 범위 내에 값이 포함되면 참        |
| SQL 연산자       | IN               | 특정 목록 내에 값이 포함되면 참        |
| SQL 연산자       | LIKE             | 비교 문자열과 일치하면 참              |
| 논리 연산자      | AND              | 두 조건이 모두 참이면 참               |
| 논리 연산자      | OR               | 두 조건 중 하나라도 참이면 참          |
| 논리 연산자      | NOT              | 조건이 거짓이면 참                     |
| 부정 비교 연산자 | != (<>, ^= 동일) | 두 값이 다르면 참                      |
| 부정 비교 연산자 | IS NOT NULL      | NULL이 아닌 값을 가지면 참             |
| 부정 SQL 연산자  | NOT IN           | 특정 목록 내에 값이 포함되지 않으면 참 |
| 부정 SQL 연산자  | NOT LIKE         | 특정 패턴과 일치하지 않으면 참         |

### GROUP BY 절과 HAVING 절의 특성

- GROUP BY 절을 통해 소그룹별 기준을 정한 후 SELECT 절에 집계 함수 사용
- 집계 함수의 통계 정보는 NULL 값을 가진 행을 제외하고 수행
- GROUP BY 절에서는 SELECT 절과 달리 ALIAS 명을 사용할 수 없음
- 집계 함수는 WHERE 절에 올 수 없음(GROUP BY 절보다 WHERE 절이 먼저 수행됨)
- WHERE 절은 GROUP으로 나누기 전에 행들을 미리 제거함
- HAVING 절을 통해 GROUP By 절의 기준 항목이나 소그룹 집계 함수를 이용한 조건을 표시할 수 있음

## DUAL 테이블의 특성

DUAL 테이블: Oracle에서 제공하는 단순 연산, 함수 테스트, 상수 반환 등에 사용되는 가상 테이블

- 단일 행과 단일 열로 구성됨
- 사용자 SYS가 소유하며 모든 사용자가 액세스 가능한 테이블
- SELECT ~ FROM ~ 의 형식을 갖추기 위한 DUMMY 테이블
- DUMMY라는 문자열 유형의 컬럼에 'X'라는 값이 들어 있는 행을 1건 포함

| 함수 종류 | 함수명                            | 설명                                       |
| --------- | --------------------------------- | ------------------------------------------ |
| 문자 함수 | UPPER(str)                        | 문자열을 대문자로 변환                     |
| 문자 함수 | LOWER(str)                        | 문자열을 소문자로 변환                     |
| 문자 함수 | INITCAP(str)                      | 문자열의 첫 글자를 대문자로 변환           |
| 문자 함수 | LENGTH(str) / LEN                 | 문자열의 길이를 반환                       |
| 문자 함수 | SUBSTR(str, s, n) / SUBSTRING     | 문자열에서 s번째 위치부터 n개 문자 추출    |
| 문자 함수 | CONCAT(str1, str2)                | 두 문자열을 연결                           |
| 문자 함수 | TRIM(str)                         | 문자열의 앞뒤 공백 제거                    |
| 문자 함수 | REPLACE(str, old, new)            | 특정 문자열을 다른 문자열로 치환           |
| 숫자 함수 | ROUND(num, n)                     | 소수점 n자리까지 반올림                    |
| 숫자 함수 | TRUNC(num, n)                     | 소수점 n자리까지 버림                      |
| 숫자 함수 | CEIL(num)                         | 주어진 숫자보다 크거나 같은 최소 정수 반환 |
| 숫자 함수 | FLOOR(num)                        | 주어진 숫자보다 작거나 같은 최대 정수 반환 |
| 숫자 함수 | ABS(num)                          | 절대값 반환                                |
| 숫자 함수 | MOD(a, b)                         | a를 b로 나눈 나머지 반환                   |
| 날짜 함수 | SYSDATE                           | 현재 시스템 날짜 반환                      |
| 날짜 함수 | CURRENT_DATE                      | 현재 세션의 날짜 반환                      |
| 날짜 함수 | ADD_MONTHS(date, n)               | 특정 날짜에 n개월 추가                     |
| 날짜 함수 | MONTHS_BETWEEN(date1, date2)      | 두 날짜 간 개월 수 반환                    |
| 날짜 함수 | NEXT_DAY(date, '요일')            | 특정 날짜의 다음 해당 요일 반환            |
| 변환 함수 | TO_CHAR(value, format)            | 숫자 또는 날짜를 문자형으로 변환           |
| 변환 함수 | TO_NUMBER(str)                    | 문자열을 숫자로 변환                       |
| 변환 함수 | TO_DATE(str, format)              | 문자열을 날짜형으로 변환                   |
| 일반 함수 | NVL(expr1, expr2)                 | NULL 값을 다른 값으로 대체                 |
| 일반 함수 | NVL2(expr1, expr2, expr3)         | NULL 여부에 따라 다른 값 반환              |
| 일반 함수 | NULLIF(expr1, expr2)              | 두 값이 같으면 NULL, 다르면 expr1 반환     |
| 일반 함수 | COALESCE(expr1, expr2, ...)       | NULL이 아닌 첫 번째 값 반환                |
| 일반 함수 | CASE                              | 조건에 따라 다른 값을 반환                 |
| 일반 함수 | DECODE(expr, search, result, ...) | 특정 값에 대한 매핑 수행                   |

### NULL 관련 함수

- Oracle: NVL(표현식1, 표현식2) 오라클 함ㅁ수 ISNULL(표현식1, 표현식2)
- 함수 NULLIF(표현식1, 표현식2) COALESCE(표현식1, 표현식2, ...)(NULL이 아닌 첫 번째 값을 반환)

## ORDER BY 절 특징

- 기본 정렬 순서는 ASC
- 오라클에서는 NULL 값을 가장 큰 값으로, SQL Server에서는 NULL 값을 가장 작은 값으로 간주

## SELECT문 실행 순서

1. 발췌 대상 테이블 참조(FROM)
2. 발췌 대상 데이터가 아닌 것을 제거(WHERE)
3. 행들을 소그룹화(GROUP BY)
4. 그루핑된 값의 조건에 맞는 것만을 출력(HAVING)
5. 데이터 출력/계산(SELECT)
6. 데이터 정렬(ORDER BY)

## EQUI JOIN

```SQL
SELECT 테이블1.컬럼명, 테이블2.컬럼명
FROM 테이블1, 테이블2
WHERE 테이블1.컬럼명 = 테이블2.컬럼명;

SELECT 테이블1.컬럼명, 테이블2.컬럼명
FROM 테이블1 INNER JOIN 테이블2
ON 테이블1.컬럼명 = 테이블2.컬럼명;
```

## JOIN

- INNER JOIN은 JOIN 조건에서 동일한 값이 있는 행만 반환
- CROSS JOIN은 테이블 간 JOIN 조건이 없는 경우 생길 수 있는 모든 데이터의 조합으로 M \* N 건의 데이터 조합이 발생
- LEFT OUTER JOIN은 왼쪽 테이블의 모든 행을 포함하면서 오른쪽 테이블에 일치하는 값이 없는 컬럼에 대해 NULL을 반환
- RIGHT OUTER JOIN은 오른쪽 테이블의 모든 행을 포함하면서 왼쪽 테이블에 일치하는 값이 없는 컬럼에 대해 NULL을 반환
- FULL OUTER JOIN은 두 테이블에서 일치하는 모든 행을 포함하며 어느 한 쪽에 일치하는 값이 없다면 NULL을 반환

# SQL 활용

## 일반 집합 연산자와 SQL의 비교

- UNION 연산(합집합): UNION
- INTERSECTION 연산(교집합): INTERSECT
- DIFFERENCE 연산(차집합): EXCEPT(오라클: MINUS)
- PRODUCT 연산(데카르트 곱): CROSS JOIN

## PRIOR
CONNECT BY 절에 사용되는, 부모-자식 관계를 정의하고 부모-자식의 경우 순방향, 자식-부모의 경우 역방향으로 데이터를 재귀적으로 탐색

- START WITH: 계층 구조 전개의 시작 위치를 지정하는 구문
- ORDER SIBLINGS BY: 형제 노드(동일 레벨) 사이에서 정렬을 수행

## 계층형 질의(Hierarchical Query)
계층형 질의: 계층형 데이터(동일 테이블에 계층적으로 상위 / 하위 데이터가 포함된 데이터)가 존재하는 테이블을 조회하는 방법

## SELF JOIN
SELF JOIN: 동일 테이블 사이의 조인으로 식별을 위해테이블 별칭을 다르게 사용해야 함
```SQL
SELECT
	별칭1.컬럼명,
	별칭2.컬럼명
FROM
	테이블 별칭1,
	테이블 별칭2
WHERE
	별칭1.컬럼명 = 별칭2.컬럼명;
```

## 서브쿼리
- 단일 행 서브쿼리(Single Row): 서브쿼리의 실행 결과가 항상 1건 이하로 단일 행 비교연산자(=, < 등)과 함께 사용
- 다중 행 서브쿼리(Multi Row): 서브쿼리의 실행 결과가 여러 건인 서브쿼리로, 다중 행 비교연산자(IN, ALL, ANY, SOME, EXISTS)와 함께 사용
- 다중 컬럼 서브쿼리(Multi Column): 서브쿼리의 실행 결과로 여러 컬럼을 반환하여 메인쿼리의 조건절에서 여러 컬럼을 동시에 비교 가능

## 서브쿼리 사용 시 주의사항
- 서브쿼리를 괄호로 감싸서 사용
- 서브쿼리에서는 ORDER BY를 사용할 수 없음(SELECT문에서 하나만 존재할 수 있음)

## 인라인 뷰
인라인 뷰(InlineView): FROM 절에서 사용되는 서브쿼리로, 서브쿼리의 결과가 실행 시 동적으로 생성된 테이블인 것처럼 사용할 수 있음(DB에 해당 정보가 저장되지 않음)

## View
뷰(View): 가상의 테이블로 실제 데이터를 저장하지 않고 기존 테이블의 특정 데이터를 조회하는 역할을 함

## 뷰 사용의 장점
- 독립성: 테이블 구조가 변경되어도 뷰를 사용하는 응용프로그램은 변경하지 않아도 됨
- 편리성: 복잡한 질의를 뷰로 생성하여 관련 질의를 단순하게 작성할 수 있고, 자주 사용하는 형태의 SQL을 편리하게 이용 가능
- 보안성: 뷰 생성 시 숨기고 싶은 정보를 숨기고 생성하여 사용자에게 정보를 감출 수 있음

## GROUPING COLUMNS
가질 수 있는 모든 경우에 대한 부분합(Subtotal)을 구해야 할 때 CUBE를 사용하여 모든 가능한 조합에 대한 집계를 생성하는 것이 바람직하지만, 계층적 구조로 부분합을 생성하는 ROLLUP에 비해 시스템에 많은 부담을 줌

## GROUPING SETS
```SQL
SELECT column1, column2, SUM(agg_column)
FROM table_name
GROUP BY GROUPING SETS ((column1), (column2), (column1, column2), ());
```
GROUPING SETS에 표시된 인수들에 대한 계별 집계를 통해 원하는 집계만 계산할 수 있음

## RANK
RANK 함수는 ORDER BY를 포함한 QUERY 문에서 특정 항목(컬럼)에 대한 순위를 구하는 함수로, 동일한 값에 대해서는 동일한 순위를 부여함

- DENSE_RANK의 경우 동일한 순위를 하나의 건수로 취급함
- ROW_NUMBER 함수의 경우 동일한 값에 대해서도 고유한 순위를 부여함

## LAG
LAG: 현재 행을 기준으로 특정 행 수만큼 이전(row offset)의 값을 조회할 떄 사용
- LEAD: 이후의 값을 가져오는 함수로, SQL Server에서는 지원하지 않음

# 관리 구문

## 제약조건의 종류
- PRIMARY KEY
- UNIQUE KEY
- NOT NULL
- CHECK
- FOREIGN KEY

## 테이블 컬럼에 대한 정의 변경
```
[Oracle]
ALTER TABLE 테이블명
MODIFY (컬럼명1 데이터 유형 [DEFAULT 식] [NOT NULL],
	컬럼명2 데이터 유형...);
[SQL Server]
ALTER TABLE 테이블명
ALTER COLUMN 컬럼명 데이터 유형 [DEFAULT 식] [NOT NULL];
```

## 테이블 생성의 주의사항
- 테이블명은 객체를 의미할 수 있는 적절한 이름(단수형) 권고
- 테이블 명은 중복되서는 안됨
- 한 테이블 내에서 칼럼이 중복되서는 안됨
- 테이블 이름을 지정하고 각 컬럼들은 괄호로 묶어 지정
- 테이블명과 컬럼명은 반드시 문자로 시작해야 하고, 벤ㄷ별로 길이에 대한 한계가 있음
- 벤더에서 사전에 정한 예약어는 사용할 수 없음

## 테이블의 불필요한 칼럼 삭제
```SQL
ALTER TABLE 테이블명
DROP COLUMN 삭제할 컬럼명;
```

## 테이블에 데이터를 입력하는 두 가지 유형
```SQL
INSERT INTO 테이블명 (COLUMN_LIST)
VALUES (COLUMN_LIST에 넣을 VALUE_LIST);

INSERT INTO 테이블명
VALUES (전체 COLUMN에 넣을 VALUE_LIST);
```

## 입력된 데이터의 수정
```SQL
UPDATE 테이블명
SET 수정되어야 할 컬럼명 = 수정되기를 원하는 새로운 값;
```

## TRUNCATE TABLE
TRUNCATE TABLE은 테이블 자체를 삭제하는 것이 아닌 테이블이 들어있던 모든 행들이 제거되고 저장 공간을 재사용 가능하도록 해제
- 테이블 구조를 완전히 삭제하기 위해서는 DROP TABLE 실행

## 트랜잭션
트랜잭션: 데이터베이스에서 하나의 논리적인 작업 단위
- 원자성(Atomicity): 트랜잭션에서 정의된 연산들은 모두 성공적으로 실행되든지, 전혀 실행되지 않은 상태로 남아있든지 해야 함(all or nothing)
- 일관성(Consistency): 트랜잭션 실행 전의 데이터베이스 내용이 잘못되어 있지 않다면 트랜잭션이 실행된 이후에도 데이터베이스의 내용에 잘못이 있으면 안 됨
- 고립성(Isolation): 트랜잭션이 실행되는 도중 다른 트랜잭션의 영향을 받아 잘못된 결과를 만들어서는 안됨
- 지속성(Durability): 트랜잭션이 성공적으로 수행되면 그 트랜잭션이 갱신한 데이터베이스의 내용은 영구적으로 저장됨

## ROLLBACK
테이블 내에서 변경된 데이터에 대해 COMMIT 이전에 ROLLBACK을 통해 데이터 변경 사항을 취소하고, 관련된 행에 대한 잠금(LOCKING)이 풀려 다른 사용자들이 데이터 변경을 할 수 있게 됨

## BEGIN TRANSACTION
BEGIN TRANSACTION을 통해 트랜잭션을 시작하고 COMMIT [TRANSACTION] 또는 ROLLBACK [TRANSACTION]을 통해 트랜잭션 종료
- [Oracle] SAVEPOOINT, [SQL Server] SAVE TRANSACTION 을 통해 트랜잭션의 일부만 롤백되도록 할 수 있음

