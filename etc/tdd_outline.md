# TDD

## Test Driven Development

TDD : 소프트웨어 개발 방법론 중 하나로, 코드 작성 전 테스트를 먼저 작성하고 그 테스트를 통과하는 코드를 구현하는 방식

- 테스트 작성 -> 코드 구현 -> 리팩토링의 단계를 반복하면서 개발 진행

- TDD의 철학 : 테스트를 먼저 작성해 개발자들이 목표를 명확히 하고 코드가 실제 기대한 대로 동작하는지를 지속적으로 확인

- TDD의 효과
  - 코드를 신뢰하고 유지보수를 쉽게 해 줌
  - 모듈화, 책임 분리를 쉽게 해 줌
  - 유연하고 확장 가능한 코드를 가능하게 함

## 코드 품질 요소

가독성

- 코드의 기능?
- 테스트케이스로 쉽게 파악

유지보수성

- 변경 시 영향도 파악이 필요
- 자동화 테스트로 가능

확장성

- 모듈화된 설계 유도
- 테스트 가능한 코드 구조

낮은 결합도

- 작고 독립적인 테스트 유도
- 의존성 주입/인터페이스

## TDD 적용 시 유의할 점

- 테스트 작성으로 시간이 더 걸릴 수 있음

  - 테스트케이스 작성을 기능 분석 단계에서 미리 수행하여 장기적으로 비용 절감에 도움을 줌

- 테스트코드 또한 유지보수가 필요