# 동국홀딩스 2026 중간점검 시스템

팀원 실적등록, 팀장 실적조회, 관리자 화면을 제공하는 Flask 웹 앱입니다.

## 로컬 실행

```bash
pip install -r requirements.txt
python app.py
```

- 로그인: http://127.0.0.1:5001/midterm/
- 헬스체크: http://127.0.0.1:5001/health

## Railway 배포

1. Railway에서 이 저장소 연결
2. 환경변수 설정: `SECRET_KEY`, `FLASK_DEBUG=False`, `DATA_DIR=/data`
3. Volume 마운트 경로 `/data` (실적 데이터 영속 저장)

## 접속 유형

| 유형 | 대상 |
|------|------|
| 실적등록 | 팀원 |
| 실적조회 | 팀장 |
| 관리자 | ID `11210110` |

## 데이터 파일

- `중간점검/backdata_performance.csv` — 계정 정보
- `중간점검/project_nm.csv` — 팀별 과제명
- `중간점검/performance_data.json` — 실적 저장 (런타임 생성)
