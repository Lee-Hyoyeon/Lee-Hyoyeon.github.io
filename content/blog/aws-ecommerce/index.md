---
title: Ecommerce demo [java]
date: "2025-02-18"
discription: "phegon-dev-ecommerce"
---

#### ecommerce aws

1. IAM 만들고 -> S3 버킷 만들고
2. 버킷 퍼미션 내용 추가

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::mybucket-ecommerce-test/*"
        }
    ]
}
```

3. object upload (shoe사진 파일을 업로드 함 https://mybucket-ecommerce-test.s3.us-east-2.amazonaws.com/shoes.jpeg 오브젝트url클릭하면 이미지 보임)
4.
