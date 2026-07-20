import streamlit as st

st.markdown("# 앱 UI 만들기")
name = st.text_input("이름", placeholder="이름을 쓰세요")
grade = st. radio("학년", [1,2,3,], horizontal=True)
cls= st.text_input("반", placeholder="반을 쓰세요")

st.header("2. 챗봇 설정")
level = st.slider("난이도", 0, 100, 50)
score = st.slider("점수", 0, 100, 50)
text = st.text_input("소감", placeholder="소감을 입력해주세요")

if st.button("확인"):
    st.success(f"{name} / ({grade}학년) / {cls}반 / {level}" )
    st.markdown(f"점수: '{score}'")
    st.info(f"소감: {text}")
