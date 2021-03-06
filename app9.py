## 여러 파일을 업로드 하는 앱

import streamlit as st
from PIL import Image
import pandas as pd
import os
from datetime import datetime
from streamlit.uploaded_file_manager import UploadedFile


# 디렉토리 정보와 파일을 알려주면, 해당 디렉토리에 
# 파일을 저장하는 함수
def save_uploaded_file(directory, file) :
    # 1. 디렉토리가 있는지 확인하여, 없으면 디렉토리부터 만든다.
    if not os.path.exists(directory) :
        os.makedirs(directory)
    # 2. 디렉토리가 있으니, 파일을 저장.
    with open(os.path.join(directory, file.name), 'wb') as f :
        f.write(file.getbuffer())
    return st.success('Saved file : {} in {}'.format(file.name,directory))


def main():
    st.title('여러 파일들을 업로드 하는 앱')
    
    # 사이드바용 메뉴 
    menu = ['Image','CSV','About']
    choice = st.sidebar.selectbox('메뉴',menu)
    
    if choice == 'Image' :
        uploaded_files = st.file_uploader('이미지 파일 업로드', type=['png','jpg','jpeg'], accept_multiple_files=True)
        print(uploaded_files)

        if uploaded_files is not None :

            for file in uploaded_files :
                save_uploaded_file('temp_files',file)

                img = Image.open(file)
                st.image(img)

## csv 파일 여러개 올리는 코드를 아래 작성하세요.
## csv 파일명은 시간.csv 의 조한된 파일명으로 저장하세요

    elif choice == 'CSV' :
        uploaded_files = st.file_uploader('CSV파일 업로드', type=['csv'], accept_multiple_files=True)
        print(uploaded_files)

        

        if uploaded_files is not None :

            for file in uploaded_files :
                current_time = datetime.now()
                # print(current_time)
                # print(current_time = current_time.isoformat().replace(':','_'))
                current_time = current_time.isoformat().replace(':','_')
                file.name = current_time + '.csv'

                save_uploaded_file('temp_csv', file)

                df=pd.read_csv(file)
                st.dataframe(df)
               





if __name__ == '__main__':
    main()