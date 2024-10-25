# 20241025 방송 docker-compose

## 도거의 특징

- 가벼움 / 빠름
- 외부 환경으로부터 자유로움
- 안정성
- 이식성
- 확장성

## Container Orchestration

어플리케이션 컨테이너의 네트워킹, 프로비저닝, 배포, 관리 간소화 및 자동화

- kubernetes
- minikube
- docker swarm
- docker compose

## PodMan

podman : 오픈소스로 중앙관리 Engine이 없어(데몬이 없음) 도커보다 자유로운 편

## Docker network

### Bridge mode

도커 네트워크의 기본 모드로 가장 많이 사용

- Bridge를 통해 Eth0에 통합 관리되는 구조

### Host mode

도커 네트워크를 사용하지 않고 서버 네트워크에 직접 접속하는 방법

- 각 컨테이너별로 Eth0에 직접 접속

### Overlay mode

각 호스트가 별도의 네트워크를 사용하나(eth0, eth1, ...), 이를 통합 관리하는 구조

- 복잡하게 얽혀 동작할 수도 있음(여러 네트워크를 하나의 장비처럼 사용 가능)

#### 오버레이 네트워크 제한사항

- 동일 Region
- 동일 Account
- 동일 Permission

#### 오버레이 네트워크 확장

- Overlay + VPN으로 제한사항을 쉽게 맞출 수 있음
  - 한국 + 미국 등의 도커 네트워크를 합쳐 대형화된 서버로 활용 가능

## Docker File

spring boot, python, node.js 등 프레임워크 프로젝트는 프로젝트 생성 시점부터 도커 이미지로 올려서 개발이 가능

- 도커파일에 따라 별도 설치 없이 도커 엔진 내부에서 모두 처리

## docker-compose.yml
