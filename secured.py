import_database = {
    'default': {
    	# django db를 mysql로 사용하겠음
        'ENGINE': 'django.db.backends.mysql',
        # DB 이름 지어주기
        'NAME': 'djangodatabase',
        # 사용자 유저 계정 생성 후 입력하기
        'USER': 'root',
        # 사용자 비밀번호 생성 후 입력하기
        'PASSWORD': '1234',
        # default host인 localhost
        'HOST': 'db',
        # MySQL default 포트 번호
        'PORT': '3306',
    }
}
