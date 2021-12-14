import streamlit as st
import pandas as pd
# 이미지 처리를 위한 라이브러리
from PIL import Image

def main():

    img = Image.open('data/image_03.jpg')
    print(img)
    st.image(img)

    st.image(img, use_column_width=True)

    st.image('https://ae01.alicdn.com/kf/HTB1IGCpd_qWBKNjSZFxq6ApLpXay/-.jpg_Q90.jpg_.webp')

    
    video_file = open('data/cat.mp4','rb')
    st.video(video_file)

    # audio_file = open('data/song.mp3','rb')
    # st.audio(audio_file.read(),format='audio/mp3')



if __name__ == '__main__' :
    main()