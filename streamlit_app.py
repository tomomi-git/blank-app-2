import streamlit as st
from PIL import Image

st.title("🎈 テスト（画像表示アプリ）")

uploaded_file = st.file_uploader("画像を選択してください", type=["png", "jpg", "jpeg"])

image = Image.open(uploaded_file)    
max_size = (300, 300)
image.thumbnail(max_size)
original_width, original_height = image.size