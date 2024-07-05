# JIRA
## Why JIRA?
- Issue Tracking(PM)
### Agile
- 에자일 소프트웨어 개발 선언:
    - 공정과 도구보다 개인과 상호작용을
    - 포괄적인 문서보다 작동하는 소프트웨어를
    - 계약 협상보다 고객과의 협력을
    - 계획을 따르기보다 변화에 대응하기를
- 위 4요소 오른쪽에 더 높은 가치를 둠을 의미함

#### Scrum
스크럼 미팅: 빠르게 진행상황 / 진행목표만을 공유하고 끝내는 미팅
### DevOps
Silo 현상: 개발팀(Dev)와 운영팀(Ops)이 마치 자기 Silo만 채우려는 것처럼 자신들의 입장만 고수하여 개발 - 운영의 악순환 고리를 만드는 것

DevOps: 개발과 운영을 한 팀으로 합쳐 유기적으로 흘러가도록 만드는 것
- 반복적인 작업들을 자동화
- 팀원 모두가 아는 하나의 공유된 지표가 필요
- 이슈에 대한 팀원들과의 공유가 필요
    - Jira를 활용한 이슈 관리 필요
### SRE
SRE(Site Reliability Engineering)
```class SRE implements DevOps```: SRE는 DevOps를 더 잘 진행하기 위한 개념

## Using JIRA
### JQL
Jira Query Language: Jira Issue를 구조적으로 검색하기 위해 제공하는 SQL과 유사한 문법
- Jira 각 필드에 맞는 특수한 예약어들을 제공
- Issue들을 재가공해 유의미한 데이터를 도출해 내는데 활용(Gadget, Agile Board 등)

[Use advanced search with Jira Query Language (JQL)](https://support.atlassian.com/jira-service-management-cloud/docs/use-advanced-search-with-jira-query-language-jql/)

JQL Dates
- Current(Today), -1d, +1w 등 상대 날짜의 개념
- endOfDay(), startOfDay() 등 JQL Functions 존재

### Why JQL
- JQL은 저장하여 필요할 떄마다 Jira에서 사용할 수 있음

### 현업에서의 Jira 활용
Issue Tracking에 Jira 활용
- Repo. Hosting, Code review는 Git(Github)
- GitLab, Github에 Jira 이슈를 연결할 수 있음

