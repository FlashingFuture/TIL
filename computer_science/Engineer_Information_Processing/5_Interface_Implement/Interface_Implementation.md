## 079. 미들웨어 솔루션
### 미들웨어
미들웨어 : 운영체제와 응용프로그램, 또는 서버와 클라이언트 사이 다양한 서비스를 제공하는 소프트웨어
- DB, RPC, MOM, TP-Monitor, ORB, WAS 등

## 080. 모듈 연계를 위한 인터페이스 기능 식별
### Enterprise Application Integration
EAI : 기업 내 각종 애플리케이션 및 플랫폼 간 상호 연동이 가능하게 해주는 솔루션
- Point-to-Point : 애플리케이션들을 1 : 1로 연결
- Hub & Spoke : 단일 접점인 허브 시스템을 통해 데이터를 전송
- Message Bus(ESB) : 미들웨어 버스를 두어 처리하는 방식
- Hybrid : 허브와 버스를 혼합

### Web Service
웹 서비스 : 네트워크의 정보를 표준화된 서비스 형태로 만들어 공유하는 기술
- 서비스 지향 아키텍쳐(SOA) 개념 실현의 대표적인 방법
- SOAP, UDDI, WSDL 등

## 083. 인터페이스 구현
### Javascript Object Notation
JSON : 데이터 객체를 속성 - 값의 쌍(Attribute-Value Pairs)로 나타내는 개방형 표준 포맷
- AJAX에서 XML을 대체하여 사용

### Asynchronous JavaScript and XML
AJAX : JS를 활용해 클라이언트와 서버 간 XML 데이터를 주고 받는 비동기 통신 기술

## 084. 인터페이스 보안
### 인터페이스 보안 기능 적용
네트워크 영역에서의 보안 : 인터페이스 송수신 간 스니핑 등에 의한 데이터 탈취 및 변조 위협을 방지하기 위해 네트워크 트래픽에 대한 암호화를 설정
- IPSec(패킷 단위 변조 방지 및 은닉), SSL(4~7계층 인증, 암호화, 무결성 보장 프로토콜), S-HTTP(클라이언트 - 서버 간 메시지 암호화) 등

### 데이터 무결성 검사 도구
- Tripwire, AIDE, Samhain, Claymore, Slipwire, Fcheck 등

## 085. 인터페이스 구현 검증
### 인터페이스 구현 검증 도구
- xUnit : 테스트코드를 여러번 작성하지 않게 도와주고 자동화된 해법을 제공하는 단위 테스트 프레임워크
- STAF : 서비스 호출, 컴포넌트 재사용 등 다양한 환경을 지원하는 테스트 프레임워크로 크로스 플랫폼 / 분산 소프트웨어 테스트 환경을 지원
- 그 외 FitNesse, NTAF, Selenium, watir 등