## GIT

### 분산 버전 관리 시스템

- 버전 : 이전 버전으로부터의 변경 사항을 기록
- 분산 : 버전을 여려 개의 복제된 저장소에 저장
    - 협업의 효율화(개인 공간에서 작업 후 이후 동기화 가능)

GIT의 구조

- Working directory
- Staging Area : Working directory에서 변경된 파일을 저장하는 영역(파일 추가 / 제외 가능)
- Repository : 버전(commit) 이력과 파일들이 영구적으로 저장되는 영역
    
    
    *bash : UNIX의 터미널
```bash
git init
```   
- 로컬 저장소 설정(git의 버전 관리를 시작할 디렉토리에서 실행)
```bash
git add
```
- 변경사항이 있는 파일을 staging area에 추가
    - git add . : 한 번에 변경사항을 전부 staging area에 업로드
```bash
git commit -m “name”
```
- staging area의 파일들을 저장소에 기록(커밋)
```bash
git status
```
- git이 감지한 파일(변화)들을 확인
```bash
git log
```
- 커밋된 내용을 확인
    
    *git 저장소 안에 또 다른 git 저장소는 존재할 수 없음
    
    → git init을 진행한 상위 디렉토리 안의 하위 디렉토리 그 어디에서도 git init을 진행해서는 안됨
    

## 로컬

- 현재 사용자가 직접 접속하고 있는 기기 / 사용자가 직접 조작하는 환경 ( 온라인 연결 X )

## GITHUB 실습하기

```bash
git remote add origin remote_repo_url
```

- 로컬 저장소에 원격 저장소 주소 추가
    - git remote : Manage set of tracked repositories
    - origin : 추가하는 원격 저장소 별칭(선언)

```bash
git remote set-url origin remote_repo_url
```

- 로컬 저장소에 원격 저장소 주소 변경

```bash
git remote -v
```

- 등록된 저장소 확인

*clone : 전부 복제해서 가져옴, pull : 업데이트된 버전만 땡겨옴

```bash
git push -u origin master
```

- 원격 저장소에 commit 목록을 업로드
    
    *원격 저장소에는 commit만이 올라감!
    

```bash
git pull origin master
```

- 원격 저장소의 변경사항(버전)만을 받아옴 (업데이트)

```bash
git clone remote_repo_url
```

- 원격 저장소 전체를 복제 (다운로드)
    - 이미 주소가 있기에 굳이 git remote add를 통해 주소를 추가할 필요가 없음

### gitignore : git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는 데 사용되는 텍스트 파일

*공유하지 말아야 되는 파일에 사용

- 파일명 : .gitignore (확장자 없음)

*이미 git의 관리를 받은 파일에 gitignore을 설정해도 적용되지 않음
