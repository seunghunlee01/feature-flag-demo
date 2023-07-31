# feature-flag-demo

## Description
- AWS AppConfig 기반 Feature Flag Demo

## Prerequisite
- AWS CLI

## How to use
### Python
``` bash
$ python3 -m venv venv
$ source venv/bin/activate
$ poetry install
```

### Env
- .env.dev 파일 생성 후 아래 내용 추가
``` bash
APPLICATION_NAME=
ENVIRONMENT_NAME=dev
PROFILE_NAME=
```
- `APPLICATION_NAME` : AppConfig Application Name
- `ENVIRONMENT_NAME` : AppConfig Environment Name
- `PROFILE_NAME` : AWS CLI Profile Name

### Run
``` bash
$ aws sso login --profile ${PROFILE_NAME}
$ python -m uvicorn main:app --reload 
```
- http://127.0.0.1:8000/api/v1/appconfig
  - AppConfig 에 설정된 Feature Flag 값 확인 

### Test
``` bash
$ pytest
```

