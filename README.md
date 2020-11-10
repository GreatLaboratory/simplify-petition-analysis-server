## API 목록

- GET /api/wordCloud/:category (분아별 워드클라우드 이미지 반환)
  - request param : category -> 분야별 시리얼 넘버
  - 해당 분야의 청원글 제목을 크롤링하여 워드클라우드로 시각화&저장 후 해당 파일로 리다이렉트
  - ex) /api/wordCloud/35 => /wordCloud_35.png
- GET /api/summary/:petitionID (특정 청원의 청원내용과 답변내용 요약)
  - request param : petitionID -> 요약하려는 특정 청원글 id
  - 해당 청원내용과 답변내용을 요약한 문자열을 응답
  ```json
  {
    "question": "...",
    "answer": "..."
  }
  ```
