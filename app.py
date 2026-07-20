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

if st.button("확인"):
    if agree:
        st.success(f"{name} / ({grade}학년) / {cls}반 / {level}" )
        st.markdown(f"점수: '{score}':)
        st.info(f"소감: {text)")
