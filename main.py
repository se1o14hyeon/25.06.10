import streamlit as st
st.title("나의첫 app")
st.write("hello")
name=st.text_input("이름 입력")
if name:
  if name=="홍길동":
    st.success("반갑습니다, 홍길동님!")
  else:
    st.warning("누구세요?")
