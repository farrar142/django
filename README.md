# 보안에 주의.
##### EC2 <-> Host 및 Github <-> jenkins 간의 ssh키는 외부에 노출되지 않도록.
##### 컨테이너는 사용하지 않을경우 중지 시켜둠.
##### 가급적 제한적인 ip와 포트로의 접근만을 허용할 것
##### EC2 사용기, 설치 파트와 config 파트, 웹설정파트로 나누기
# sh파일 수정시 CRLF 절대 금지 LF로 저장
# 서버 배포간 다운타임
### 웹서버만 빌드시
##### 최소 30초에서
### DB까지 빌드시
##### 최대 4분

# 예상 시나리오

### 외부 EC2(niginx Docker (jenkins Docker(team1),jenkins Docker(team2),jenkins Docker(team3),jenkins Docker(team4)))
```
${EC2IPv4}:80/${teamN}/${ProjectName}
```
EC2의 nginx 가 ${EC2IPv4}:80/${teamN} 까지의 경로를 파싱해서 각 포트별로 나눠줌.
위에서 나눠진 포트를 각 도커 컨테이너로 할당함. 10001 = team1, 10002 = team2
${EC2IPv4}:80/${teamN} = 
