# �ʼ�
<!-- https://it-and-life.tistory.com/43 ��ġ

cmdâ���� bash ���� ��
cd /
cd root
ls -a
vim .bashrc
���� a �� insert��� Ȱ��ȭ �������ܿ�
export PATH="$HOME/bin:$HOME/.local/bin:$PATH"
export PATH="$PATH:/mnt/c/Program\ Files/Docker/Docker/resources/bin"
alias docker=docker.exe
alias docker-compose=docker-compose.exe
�߰� ��
ESC : w Enter q Enter -->
jenkins ������ ��ġ


# 1 .ssh Ű����
```
mkdir C:/Program Files/Jenkins/.shh
ssh-keygen -t rsa -f C:/Program Files/Jenkins/.shh/jenkins_ci sshŰ ����
```

# 2 git hook�� ���� ���ξ������Ҵ�
npm install -g ngrok
ngrok http "��Ʈ��ȣ" �Է���
������ �ּҷ� ����,
ngrok�� �α����� auth token get
����
ngrok http -authtoken "authtokenvalue"
���� ���������� ���� ����.

# 3

### jenkins ���� ����
## 1 ��Ų������ shell exec ����
jenkins ����-> �ý��ۼ���-> shell executable ->

C:\Program Files\Git\bin\bash.exe �߰�.
## 2 - 1 ��Ų������ credential �� sshŰ �Է�
jenkins ���� -> security -> manage Credential ->
(global)[�ǾƷ�] add credential
kind = SSH Username with private key)
username = {identifier}
Private Key->Enterdirectly = cd C:/Program Files/Jenkins/.shh/jenkins_ci
jenkins_ci �� ����
## 2 - 2 ����꿡 ssh �߰�
github deploy Ű �߰�
https://github.com/{username}/{projectname}/settings/keys/new
->
cd C:/Program Files/Jenkins/.shh/jenkins_ci.pub �� ����
->add key


�� ��� �������͸� setting���� Webhooks �� ����.
payloadurl = {3.���� ������ �ּ�} + {/github-webhook/}



# 4
### ��Ų�� ����

������ �������͸��� SSH CODE�� ����.
->
���ο� ������
->
Freestyle project
->
�ҽ��ڵ����
->
git
->
repository url�� SSH CODE�� �ٿ��ֱ�
->
Credentials �� �Ʊ� �����ξ��� �������� ����.
->
Ʈ���� �귣ġ ����.

��������
->
GitHub hook trigger for GITScm polling
->
Build
->
window batch command
->
�׽�Ʈ�� ��ɾ�� �Է�.
recommend
```
cd docker/docker-dev
bash
sudo distribute.sh
```
