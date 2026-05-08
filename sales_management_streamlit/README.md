# 판매 관리 시스템

Streamlit 기반 판매 데이터 관리 웹 애플리케이션입니다.

## 설치 및 실행

1. 가상환경 생성 및 활성화:
   ```powershell
   python -m venv venv
   .\\venv\\Scripts\\Activate.ps1
   ```

2. 패키지 설치:
   ```powershell
   pip install -r requirements.txt
   ```

3. 앱 실행:
   ```powershell
   streamlit run app.py
   ```

4. 브라우저에서 `http://localhost:8501` 접속

## 앱 구조

앱은 `app.py`에서 사이드바 페이지 네비게이션을 사용하여 각 페이지를 불러옵니다.

- `sales_management_streamlit/app.py`: 메인 실행 파일
- `sales_management_streamlit/pages/`: 왼쪽 사이드바에서 선택할 수 있는 각 페이지
- `sales_management_streamlit/src/`: 데이터 로드, 전처리, 분석, 시각화 함수
- `sales_management_streamlit/data/`: 원본, 전처리, 월별 다운로드용 데이터
- `sales_management_streamlit/assets/`: 로고 및 스타일
- `sales_management_streamlit/config/config.yaml`: 경로 및 컬럼 설정
- `sales_management_streamlit/reports/`: 리포트 저장용 디렉터리

## 페이지 설명

- `01_대시보드`: 매출 요약, KPI, 차트
- `02_판매데이터_조회`: 필터/검색 및 다운로드
- `03_월별_다운로드`: 월별 엑셀 다운로드
- `04_제품별_분석`: 제품별 매출/수량 분석
- `05_판매처별_분석`: 판매처별 매출/수량 분석
