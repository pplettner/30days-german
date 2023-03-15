import streamlit as st
import os
import numpy as np
import pandas as pd
import urllib.request
from PIL import Image
import glob

def update_params():
    st.experimental_set_query_params(challenge=st.session_state.day)

md_files = sorted([int(x.strip('Day').strip('.md')) for x in glob.glob1('content',"*.md") ])

# Logo and Navigation
col1, col2, col3 = st.columns((1,4,1))
with col2:
    st.image(Image.open('streamlit-logo-secondary-colormark-darktext.png'))
st.markdown('# 30 Tage Streamlit')

days_list = [f'Tag {x}' for x in md_files]

query_params = st.experimental_get_query_params()

if query_params and query_params["challenge"][0] in days_list:
    st.session_state.day = query_params["challenge"][0]

selected_day = st.selectbox('Start the Challenge 👇', days_list, key="day", on_change=update_params)

with st.expander("Über #30DaysOfStreamlit"):
    st.markdown('''
    **#30DaysOfStreamlit** ist eine Programmierherausforderung, welche dir dabei hilft mit dem Bauen von Streamlit Apps zu starten.
    
    Insbesonderes wirst du in der Lage sein:
    - Eine Entwicklungsumgebung zum Bauen von Streamlit Apps aufzusetzen
    - Deine erste Streamlit App zu bauen
    - Lerne über all die überragenden Komponenten, die du in der Streamlit App benutzen kannst
    ''')

# Sidebar
st.sidebar.header('Über')
st.sidebar.markdown('[Streamlit](https://streamlit.io) ist eine Pythonbibliothek, welche es erlaubt, interaktive, datengetriebene Webapplikationen in Python zu erstellen.')

st.sidebar.header('Materialien')
st.sidebar.markdown('''
- [Streamlit Dokumentation](https://docs.streamlit.io/)
- [Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)
- [Buch](https://www.amazon.com/dp/180056550X) (Getting Started with Streamlit for Data Science)
- [Blog](https://blog.streamlit.io/how-to-master-streamlit-for-data-science/) (How to master Streamlit for data science)
''')

st.sidebar.header('Hochladen')
st.sidebar.markdown('Du kannst Streamlit Apps schnell und mit nur wenigen Klicks auf [Streamlit Community Cloud](https://streamlit.io/cloud) hochladen.')

# Display content
for i in days_list:
    if selected_day == i:
        st.markdown(f'# 🗓️ {i}')
        j = i.replace(' ', '')
        with open(f'content/{j}.md', 'r') as f:
            st.markdown(f.read())
        if os.path.isfile(f'content/figures/{j}.csv') == True:
            st.markdown('---')
            st.markdown('### Grafiken')
            df = pd.read_csv(f'content/figures/{j}.csv', engine='python')
            for i in range(len(df)):
                st.image(f'content/images/{df.img[i]}')
                st.info(f'{df.figure[i]}: {df.caption[i]}')
