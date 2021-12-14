# 필수
https://it-and-life.tistory.com/43
cmd창에서 bash 접속 후
cd /
cd root
ls -a
vim .basharc
이후
export PATH="$HOME/bin:$HOME/.local/bin:$PATH"
export PATH="$PATH:/mnt/c/Program\ Files/Docker/Docker/resources/bin"
alias docker=docker.exe
alias docker-compose=docker-compose.exe
추가 후
ESC : w Enter q Enter
jenkins 윈도우 설치

# 1
```
mkdir C:/Program Files/Jenkins/.shh
ssh-keygen -t rsa -f C:/Program Files/Jenkins/.shh/jenkins_ci ssh키 생성
```

# 2
npm install -g ngrok
ngrok http "포트번호" 입력후
생성된 주소로 접속,
ngrok에 로그인후 auth token get
이후
ngrok http -authtoken "authtokenvalue"
이후 정상적으로 접속 가능.

# 3

### jenkins 관리
->
manage Credential
->
(global)[맨아래] add credential
(kind = SSH Username with private key)
username = {identifier}
Private Key->Enterdirectly)
cd C:/Program Files/Jenkins/.shh/jenkins_ci
jenkins_ci 의 내용

github deploy 키 추가
https://github.com/{username}/{projectname}/settings/keys/new
->
cd C:/Program Files/Jenkins/.shh/jenkins_ci.pub 의 내용
->add key


깃 허브 리포지터리 setting에서 Webhooks 에 접근.
payloadurl = {3.에서 생성된 주소} + {/github-webhook/}



# 4
### 젠킨스 설정

본인의 리포지터리의 SSH CODE를 복사.
->
새로운 아이템
->
Freestyle project
->
소스코드관리
->
git
->
repository url에 SSH CODE를 붙여넣기
->
Credentials 에 아까 만들어두었던 프로필을 선택.
->
트리거 브랜치 선택.

빌드유발
->
GitHub hook trigger for GITScm polling
->
Build
->
window batch command
->
테스트할 명령어들 입력.
