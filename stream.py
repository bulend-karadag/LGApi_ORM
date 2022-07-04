import streamlit as st
import requests
import pandas as pd
import streamlit.components.v1 as components
import json


st.set_page_config(layout="wide")
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

with st.sidebar:
    with st.form(key='my_form'):
        search_type = st.radio( "Please select search type ", ('Title', 'Author', 'Publisher'))
        text_input = st.text_input(label='Enter a keyword')
        search_limit = st.radio( "Number of results per page ", (25, 50, 100, 200))
        submit_button = st.form_submit_button(label='Submit')
        
url = 'http://localhost:8000/books'
if submit_button:
    params = {'search':search_type, 'keyword':text_input, 'limit':search_limit, 'page':0}
    response = requests.get(url, params=params)
    data = pd.DataFrame(response.json())
    data['link'] = "http://libgen.is/get.php?md5="+data['md5']
    st.session_state['data'] = data   
    st.session_state['page']=0
    
    


if 'data' in st.session_state:
    data=st.session_state['data']
    col1, col2 = st.columns(2)
    with col1:
        option_language = st.selectbox('please select a language', options=data['language'].unique(), key ='language' )
        pass

    with col2:
        option_extension = st.selectbox('please select a format', options= data['extension'].unique(), key ='extension')
        pass

    if ('language' in st.session_state and 'extension' in st.session_state):
        data_filtered = data.loc[(data['language']==option_language) & (data['extension']==option_extension)]
    elif 'language' in st.session_state:
        data_filtered = data.loc[data['language']==option_language]
    elif 'extension' in st.session_state:
        data_filtered = data.loc[data['extension']==option_extension]
    else:
        data_filtered = data

    colms = st.columns((1, 5, 4, 2, 1, 1))
    fields = ["№", 'Title', 'Author', 'Publisher', "Year", "Links"]
    for col, field_name in zip(colms, fields):
        # header
        col.write(field_name)

    for x, row in data_filtered.iterrows():
        col1, col2, col3, col4, col5, col6 = st.columns((1, 5, 4, 2, 1, 1))
        col1.write(row['id'])  # index
        col2.write(row['title'])  # title
        col3.write(row['author'])  # author
        col4.write(row['publisher'])   # publisher
        col5.write(row['year'])  # year
        col6.write(f"[url]({row['link']})")   # link
        
    if st.button('Next Page >>'):
        st.session_state['page'] += 1
        params = {'search':search_type, 'keyword':text_input, 'limit':search_limit, 'page':st.session_state['page']}
        response = requests.get(url, params=params)
        data = pd.DataFrame(response.json())
        data['link'] = "http://libgen.is/get.php?md5="+data['md5']
        st.session_state['data'] = data

    