import streamlit as st

st.set_page_config(page_title="자기소개", page_icon="👋", layout="centered")

st.markdown(
    """
    <style>
    body {
        background-color: #ffe9f0;
    }
    .stApp, .css-18e3th9, .main, .block-container {
        background-color: #ffe9f0 !important;
    }
    .css-1d391kg, .css-ffhzg2, section[data-testid="stSpacer"] {
        background-color: #ffe9f0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("안녕하세요! 🎉")
st.subheader("수학교육에 진심인 숙명여대 학부생입니다")

st.write("## 소개")
st.write("**이름:** 정서희\n\n**직업/소속:** 숙명여대 학부생\n\n저는 아이들과 함께하는 수학교육에 특히 정이 많은 학생입니다. 수학을 가르칠 때 학생들의 눈높이를 먼저 생각하고, 한 사람 한 사람의 이해도와 자신감을 함께 키워나가고 싶습니다. 친근한 선생님으로서 학생들이 수학을 부담 없이 다가갈 수 있도록 돕고, 수학의 원리를 생활 속 예시로 풀어 설명하는 방식을 좋아합니다. 수학 공부 자체가 즐거운 경험이 되도록 따뜻하고 포용적인 수업 분위기를 만들고자 노력합니다.")

st.write("## 관심사")
st.write("- 학생들이 스스로 생각하도록 돕는 수업 설계\n- 수학 개념을 쉽고 친근하게 전달하는 교육 콘텐츠 제작\n- 놀이와 프로젝트 기반의 수학교육\n- 학습자 맞춤형 피드백과 멘토링\n- 데이터 기반으로 학습 성과를 분석하고 개선하는 방법")

st.write("## 경력 및 활동")
st.write("- 수학교육 관련 교재 개발 과제 참여 및 발표\n- 학부 연구 프로젝트에서 초·중학생용 수업 자료 제작 지원\n- 학교 수업 보조 활동과 학생 멘토링 경험\n- 수학 동아리에서 워크숍 기획 및 참여\n- 학습 상담을 통해 학생들의 수학 자신감 향상에 기여")

st.write("이 페이지는 더 자유롭게 수정하여 자기소개 내용을 추가할 수 있습니다.")

