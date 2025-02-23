---
title: google oauth login chat
date: "2025-02-22"
discription: "google oauth login chat"
---

### Login Chat Portfolio

<a href="./Login Chat.pdf">📄 LoginChat.pdf</a>

---

##### Run

- frontend start
  - npm start;
- backend start
  - sever/ node index.js;

##### Local setting

- 구글 클라우드 클라이언트에서
  - 브라우저 요청에 사용 http://localhost:3000
  - .env local 환경 세팅 : REACT_APP_REDIRECT_URL=http://localhost:3000

##### Aws Amplify deploy

1. create new app
2. github link
3. commit 하면 자동 배포 ???
4. domain : https://main.d3j4dwe7mj38lf.amplifyapp.com/

---

#### Reference

내 구글 클라우드 클라이언트- https://console.cloud.google.com/auth/clients?invt=AbjhLw&project=hy-project-439904&inv=1

웹 서버 애플리케이션 설명
https://developers.google.com/identity/protocols/oauth2/web-server#node.js_5

참고했던 블로그 한국
https://ahn3330.tistory.com/166

구글 클라우드 가이드
https://cloud.google.com/apigee/docs/api-platform/security/oauth/access-tokens?hl=ko

깃에 있는 모드모듈 지우기
git rm -r --cached .
git add .
git commit -m "remove node_modules"
git push
