import streamlit as st
import streamlit.components.v1 as components

# HTML 파일 읽기
with open('index.html', 'r') as file:
    html_code = file.read()

# HTML 코드 표시
components.html(html_code, height=300)