---
title: python
date: "2025-02-10"
discription: "파이썬...."
---

#### 한투 파이썬 실행

```
hy_test git:(main) ✗ python3.13 -m pip install --upgrade pip

[notice] A new release of pip is available: 24.3.1 -> 25.0
[notice] To update, run: python3.13 -m pip install --upgrade pip
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try brew install
xyz, where xyz is the package you are trying to
install.
이런 에러가 났을 대 가상 환경에서 인스톨

➜ hy_test git:(main) ✗ python3 -m venv venv
➜ hy_test git:(main) ✗ source venv/bin/activate
(venv) ➜ hy_test git:(main) ✗ python3 -m pip install requests
(venv) ➜ hy_test git:(main) ✗ pip install python-dotenv
(venv) ➜ hy_test git:(main) ✗ python3 KoreaStockAutoTrade.py 파일 실행
```
