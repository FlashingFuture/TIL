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

## 103. SQL - 
