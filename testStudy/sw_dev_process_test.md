# 소프트웨어 개발주기와 테스트

## 테스트의 구분

구조적 테스팅: 구조(코드, 제어 흐름도)

기능 테스팅: 요구 기능 테스트

비가능 테스팅: 성능, 사용성 테스트

## V-Model

요구사항 분석 <-------> 인수 테스트

설계 <-----> 시스템 테스트

상세설계 <---> 통합 테스트

코딩 <-> 단위 테스트

### 단위 테스트

단위 테스트: 단위 기능 검증을 목적으로 코드, DB 모듈을 테스트

- 구조적 테스팅 : 커버리지 측정
- 비기능 테스팅 : 메모리 누수, 견고성 테스팅(이상값 검증)

#### 주요 테스팅 접근법

테스트 주도 개발

- 단위 테스트는 개발을 수행한 개발자가 수행하나, 필요시 타 개발자 또는 제 3자에 의해 실시될 수 있음

### 통합 테스트

통합 테스트: 컴포넌트 간 연동 확인을 목적으로 OS, 파일, 하드웨어의 연동을 테스트

- 테스트 베이시스 : 와이어프레임, 유즈케이스, 아키텍쳐, 워크플로우

- 전체 구조를 테스트하며, 통합 단계에서의 기능이 있다면 기능 테스트로도 진행되며, **성능 테스팅**이 수행됨

#### 주요 테스팅 접근법

- 상향식 통합
- 하향식 통합
- 백본 통합
- 빅뱅 통합

### 시스템 테스트

시스템 테스트 : 시스템의 정상 동작 확인을 목표로 시스템의 정상동작과 요구사항 만족을 테스트

- 테스트 베이시스 : 유즈케이스, 요구사항서, 기능명세서, 리스크 분석서

### 인수 테스트

인수 테스트 : 기능에 확신을 주기 위한 목적으로 비즈니스, 운영, 유지보수 프로세스가 정상 동작하는지 테스트

- 테스트 베이시스 : 유즈케이스, 요구사항서, 기능명세서, 리스크 분석서
- 상황에 따라 사용자 인수 테스팅, 운영상의 인수 테스팅, 계약 인수 테스팅, 규정 인수 테스팅, 알파 / 베타 테스팅 등 다양한 테스팅 존재