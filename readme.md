# �ʼ�
https://it-and-life.tistory.com/43
cmdâ���� bash ���� ��
cd /
cd root
ls -a
vim .basharc
����
export PATH="$HOME/bin:$HOME/.local/bin:$PATH"
export PATH="$PATH:/mnt/c/Program\ Files/Docker/Docker/resources/bin"
alias docker=docker.exe
alias docker-compose=docker-compose.exe
�߰� ��
ESC : w Enter q Enter
jenkins ������ ��ġ

# 1
```
mkdir C:/Program Files/Jenkins/.shh
ssh-keygen -t rsa -f C:/Program Files/Jenkins/.shh/jenkins_ci sshŰ ����
```

# 2
npm install -g ngrok
ngrok http "��Ʈ��ȣ" �Է���
������ �ּҷ� ����,
ngrok�� �α����� auth token get
����
ngrok http -authtoken "authtokenvalue"
���� ���������� ���� ����.

# 3

### jenkins ����
->
manage Credential
->
(global)[�ǾƷ�] add credential
(kind = SSH Username with private key)
username = {identifier}
Private Key->Enterdirectly)
cd C:/Program Files/Jenkins/.shh/jenkins_ci
jenkins_ci �� ����

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
