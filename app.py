import streamlit as st

st.markdown("# 앱 UI 만들기")
import streamlit as st

user_id = st.text_input("이름", placeholder="example_user")
grade = st. radio("학년", [1,2,3,], horizontal=True)
user_id = st.text_input("반", placeholder="example_user")

st.header("2. 챗봇 설정")
creativity = st.slider("난이도", 0, 100, 50)
creativity = st.slider("점수", 0, 100, 50)
user_id = st.text_input("소감", placeholder="example_user")

if st.button("질문 전송하기"):
    if agree:
        st.success(f"성공적으로 전송되었습니다! ({user_id}님)")
        st.markdown(f"""
        * **질문 내용:** {question}
        * **선택 모델:** `{ai_model}` | **말투:** `{tone}`
        * **활성화 기능:** {', '.join(features) if features else '없음'}
        * **창의성:** `{creativity}%` | **처리 속도:** `{ai_speed}`
        """)
        
        if age < 14:
            st.info("참고: 14세 미만 사용자이므로 보호자 모드가 활성화됩니다.")
    else:
        st.error("⚠️ 동의 항목에 체크해야 전송이 가능합니다.")
