import streamlit as st
from PIL import Image

st.title("🎈 テスト（画像表示アプリ）")

uploaded_file = st.file_uploader("画像を選択してください", type=["png", "jpg", "jpeg"])