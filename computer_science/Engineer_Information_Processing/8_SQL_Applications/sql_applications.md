## 102. SQL - DDL

### Data Define Language

DDL : DB를 구축하거나 수정할 목적으로 사용하는 언어

- SQL문에서 `[]`대괄호로 묶은 명령어는 생략 가능

### CREATE

CREATE : SCHEMA, DOMAIN, TABLE, VIEW, INDEX 정의

- `CREATE SCHEMA {스키마명} AUTHORIZATION {유저 id};`
- ```SQL
  CREATE DOMAIN {도메인명} [AS] {데이터 타입}
    [DEFAULT 기본값]
    [CONSTRAINT 제약조건명 CHECK {범위값}];
  ```
- ```SQL
    CREATE TABLE {테이블명}
    (속성명 {데이터 타입} [DEFAULT 기본값] [NOT NULL]
    [, PRIMARY KEY({기본키 속성명}, ...)]
    [, UNIQUE({대체키 속성명}, ...)]
    [, FOREIGN KEY({외래키 속성명}, ...)]
        [REFERENCES {참조 테이블}({기본키 속성명}, ...)]
        [ON DELETE {옵션}]
        [ON UPDATE {옵션}]
    [, CONSTRAINT {제약조건명}] [CHECK {조건식}]);
  ```
- ```SQL
    CREATE VIEW {뷰명}[(속성명, [, 속성명, ...])]
    AS {SELECT문};
  ```
- ```SQL
    CREATE [UNIQUE] INDEX {인덱스명}
    ON {테이블명}(속성명 [ASC | DESC] [, {속성명} ASC | DESC])
    [CLUSTER];
  ```

### ALTER

ALTER : TABLE에 대한 정의를 변경하는 데 사용함

- ```SQL
    ALTER TABLE {테이블명} ADD {속성명} {데이터 타입} [DEFAULT {기본값}];
    ALTER TABLE {테이블명} ALTER {속성명} [SET DEFAULT {기본값}];
    ALTER TABLE {테이블명} DROP COLUMN {속성명} [CASCADE];
  ```

### DROP

DROP : 제거하는 명령문

```SQL
    -- SCHEMA, DOMAIN, TABLE, VIEW, INDEX 모두 적용
    DROP TABLE {테이블명} [CASCADE | RESTRICT];
    --- 제약조건만
    DROP TABLE {제약조건명};
```

## 103. SQL - DCL
### Data Control Language
DCL : 데이터의 보안, 무결성, 회복, 병행 제어 등을 정의하는 데 사용하는 언어

### GRANT / REVOKE
GRANT : 권한 부여를 위한 명령어
```SQL
GRANT {사용자등급} TO {사용자 ID 리스트} [IDENTIFIED BY {암호}];
GRANT {권한 리스트} ON {개체} TO {사용자} [WITH GRANT OPTION];
```
REVOKE : 권한 취소를 위한 명령어
```SQL
REVOKE {사용자등급} FROM {사용자 ID 리스트};
REVOKE [GRANT OPTION FOR] {권한 리스트} ON {개체} FROM 사용자 [CASCADE];
```

### COMMIT / ROLLBACK
COMMIT : 트랜잭션 처리가 완료된 후 트랜잭션이 수행한 내용을 데이터베이스에 반영하는 명령

ROLLBACK : 변경되었으나 아직 커밋되지 않은 내용들을 모두 취소하고 데이터베이스를 이전 상태로 되돌리는 명령

SAVEPOINT : 트랜잭션 내 ROLLBACK 할 위치인 저장점을 지정하는 명령어

## 104. SQL - DML
### Data Manipulation Language
DML : 저장된 데이터를 실질적으로 관리하는 데 사용되는 언어

### INSERT
삽입문은 기본 테이블에 새로운 튜플을 삽입할 때 사용
```SQL
INSERT INTO {테이블명([{속성명 1}, {속성명 2}, ...])}
VALUES ({데이터 1},, {데이터 2}, ...);
```

### DELETE
삭제문은 기본 테이블에 있는 튜플 중 특정 튜플(행)을 삭제할 때 사용
```SQL
DELETE
FROM 테이블명
[WHERE 조건];
```

### UPDATE
갱신문은 기본 테이블에 있는 튜플들 중 특정 튜플의 내용을 변경할 때 사용
```SQL
UPDATE 테이블명
SET 속성명 = 데이터[, 속성명=데이터, ...]
[WHERE 조건];
```

### SELECT
```SQL
SELECT [PREDICATE] [테이블명.]속성명 [AS 별칭][, [테이블명.]속성명, ...]
FROM 테이블명[, 테이블명, ...]
[WHERE 조건]
[GROUP BY 속성명, [속성명, ...]]
[HAVING 조건]
[ORDER BY 속성명 [ASC / DESC]];
```

#### Conditional Operators
논리 연산자 : NOT / AND / OR

LIKE 연산자 : 지정된 속성의 값이 문자 패턴과 일치하는 튜플을 검색하기 위해 사용됨
- % : 모든 문자를 대표, _ : 문자 하나를 대표, # : 숫자 하나를 대표

#### GROUP functions
그룹 함수 : GROUP BY 절에 지정된 그룹의 속성의 값을 집계할 때 사용
- ```COUNT(속성명)``` : 그룹의 튜풀 수
- ```SUM(속성명)``` : 그룹의 합계
- ```AVG(속성명)``` : 그룹의 평균

#### 집합 연산자
- UNION : 두 SELECT 문의 조회 결과를 통합하여 모두 출력
- UNION ALL : 중복된 행을 두 번 출력(나머지는 위와 같음)
- INTERSECT : 두 SELECT 문의 조회 결과 중 공통된 행만 출력
- EXCEPT : 첫 SELECT문의 결과 중 두번째 SELECT 문의 결과를 제외한 행을 출력

### JOIN
JOIN : 두 개의 릴레이션에서 연관된 튜플들을 결합해 하나의 새 릴레이션을 반환함
#### INNER JOIN
공통 속성만을 기준으로 조건에 맞는 값만 포함해 새 릴레이션을 만듬
```SQL
SELECT 속성명, 속성명, ...
FROM 테이블명1, 테이블명2, ...
WHERE 조건
```

#### OUTER JOIN
공통 속성을 기준으로 조건에 맞지 않는 값들도 NULL 값을 넣어 INNER JOIN의 결과에 추가
```SQL
SELECT 속성명, 속성명, ...
FROM 테이블명1 LEFT OUTER JOIN 테이블명2
WHERE 조건
```
- ```LEFT OUTER JOIN``` : 좌측 항의 릴레이션들만 추가
- ```RIGHT OUTER JOIN``` : 우측 항의 릴레이션들만 추가
- ```FULL OUTER JOIN``` : 양 측 항의 릴레이션들을 모두 추가