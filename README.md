# 보안에 주의.
# EC2 <-> Host 및 Github <-> jenkins 간의 ssh키는 외부에 노출되지 않도록.
# 컨테이너는 사용하지 않을경우 중지 시켜둠.
# 가급적 제한적인 ip와 포트로의 접근만을 허용할 것
# EC2 사용기, 설치 파트와 config 파트, 웹설정파트로 나누기
