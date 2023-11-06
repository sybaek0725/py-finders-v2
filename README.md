# Microworks Sourcing

## 개발 환경 세팅

### 파이썬 설치 방법

- Window / MacOS : [Python](https://www.python.org/) 에서 설치파일 다운로드 받은 뒤 설치
- MacOS : ```brew install python3``` 

```shell
$ pip3 install python 
```

설치된 파이썬 버전 확인 명령어

```shell
$ python3 --version
```

### 파이썬 라이브러리 관리 방법

설치된 패키지 목록을 텍스트 파일로 저장해주는 명령어

```shell
$ pip3 freeze > requirements.txt
```

저장된 패키지 파일 설치 명령어

```shell
$ $ pip3 install -r requirements.txt
```
