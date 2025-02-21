# ⭐ “나만의 영화 기록 사이트” - Django CRUD 프로젝트

## 📚 프로젝트 소개
"나만의 영화 기록 사이트"는 Django의 MTV 패턴을 익히고 CRUD 기능 구현을 연습하기 위한 프로젝트입니다. 사용자는 영화 리뷰를 작성하고, 수정하고, 삭제할 수 있으며, 리뷰 목록과 상세 페이지를 확인할 수 있습니다.

## 🔍 주요 기능

### 📅 리뷰 리스트 페이지
![Image](https://github.com/user-attachments/assets/f0e48323-3bc4-44bc-a58f-36d0182678f0)
✔️ 작성한 모든 리뷰 목록이 표시됨
  - 개요: 영화 제목, 개봉년도, 장르, 별점, 러닝타임, 포스터 포함

✔️ 영화 제목 클릭 시 해당 리뷰의 상세 페이지로 이동

✔️ "Add a New review" 버튼을 클릭하면 새 리뷰 작성 페이지로 이동

### 📝 리뷰 상세 페이지
![Image](https://github.com/user-attachments/assets/2d3314f5-98ff-4154-a393-c9261c8e0f51)
✔️ 해당 리뷰의 전체 내용 표시
  - 영화 제목, 개봉년도, 감독, 주연, 장르, 별점, 러닝타임, 리뷰 내용, 포스터 포함

✔️ "myMoviereviews" 버튼 클릭 시 리뷰 리스트 페이지로 이동

✔️ "수정" 버튼 클릭 시 해당 리뷰 수정 페이지로 이동

✔️ "삭제" 버튼 클릭 시 해당 리뷰 삭제

### 📁 리뷰 작성 & 수정 페이지
![Image](https://github.com/user-attachments/assets/8fc2d7c7-667e-4c48-b4b6-98d5fb60b7a6)
✔️ "Add a New review" 클릭 시 빈 입력 폼이 나타남





![Image](https://github.com/user-attachments/assets/48763187-c295-45a1-925f-1becafffab0a)
✔️ "수정" 클릭 시 기존 데이터가 입력된 폼이 나타남





✔️ 작성/수정 후 "Save" 버튼 클릭 시
  - 새 리뷰 작성 시 리뷰 리스트 페이지로 이동
  - 리뷰 수정 시 해당 리뷰 상세 페이지로 이동

## 🎨 챌린지
✔️ 장르를 선택 입력 방식으로 변경

✔️ 러닝타임을 시간 단위로 변환하여 출력

✔️ 리스트 페이지에서 리뷰 정렬 기능 추가 (제목, 별점, 러닝타임 기준)

## 🔧 기술 스택
- **백엔드:** Python, Django
- **데이터베이스:** SQLite
- **템플릿 엔진:** Django Template Language (DTL)
- **배포:** 로컬 개발 환경

## 💡 실행 방법
1. 프로젝트 클론
```sh
git clone https://github.com/Dosp74/myMovieReviews.git .
```
2. 가상 환경 설정 및 패키지 설치
```sh
python -m venv venv
source venv/Scripts/activate  # Windows
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
```
3. 마이그레이션 및 서버 실행
```sh
python manage.py migrate
python manage.py runserver
```
4. 웹 브라우저에서 `http://127.0.0.1:8000/` 접속

## 💪 후기
이 프로젝트를 통해 Django의 CRUD 기능을 익히고, 웹 애플리케이션 개발 경험을 쌓을 수 있었습니다. 추가로 챌린지 기능도 구현하여 보다 완성도 높은 서비스를 만들었습니다.

✨ "나만의 영화 기록 사이트"를 직접 만들어 보며 Django를 배우고 싶은 분들에게 도움이 되길 바랍니다! ✨
