import streamlit as st
import requests
import pandas as pd
import streamlit.components.v1 as components
import json


st.set_page_config(layout="wide")
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
data = None

def langList():
    t = pd.read_csv('languages.csv')
    x = t['Language_en'].to_list()
    y = t['Language_native'].to_list()
    xx = [j.strip().split()[0] for j in x]
    yy = [j.strip().split()[0] for j in y]
    xx.extend(yy)
    return xx

def extList():
    t = pd.read_csv('extensions.csv')
    x = t['extensions'].to_list()
    return x
        

with st.sidebar:
    with st.form(key='my_form'):
        search_type = st.radio( "Please select search type ", ('Title', 'Author', 'Publisher'))
        text_input = st.text_input(label='Enter a keyword')
        search_limit = st.radio( "Number of results per page ", (25, 50, 100, 200))
        languageList = langList()
        extensionList = extList()
        option_language = st.selectbox('please select a language', options=languageList, key ='language' )
        option_extension = st.selectbox('please select a format', options= extensionList, key ='extension')
        submit_button = st.form_submit_button(label='Submit')
        
url = 'http://localhost:8000/books'
if submit_button:
    params = {'search':search_type, 'keyword':text_input, 'language': option_language,'extension':option_extension ,'limit':search_limit, 'page':0}
    response = requests.get(url, params=params)
    data = pd.DataFrame(response.json())
    if len(data)>0:
        data['link'] = "http://libgen.is/get.php?md5="+data['md5']
    st.session_state['page']=0

if st.button('Next Page >>'):
    st.session_state['page'] += 1
    st.write(st.session_state['page'])
    params = {'search':search_type, 'keyword':text_input, 'language': option_language,'extension':option_extension ,'limit':search_limit, 'page':st.session_state['page']}
    response = requests.get(url, params=params)
    data = pd.DataFrame(response.json())
    if len(data)>0:
        data['link'] = "http://libgen.is/get.php?md5="+data['md5']
    st.session_state['data'] = data

colms = st.columns((1, 5, 4, 2, 1, 1))
fields = ["№", 'Title', 'Author', 'Publisher', "Year", "Links"]
for col, field_name in zip(colms, fields):
    # header
    col.subheader(field_name)

if (data is not None):
    for x, row in data.iterrows():
        col1, col2, col3, col4, col5, col6 = st.columns((1, 5, 4, 2, 1, 1))
        col1.write(row['id'])  # index
        col2.write(row['title'])  # title
        col3.write(row['author'])  # author
        col4.write(row['publisher'])   # publisher
        col5.write(row['year'])  # year
        col6.write(f"[url]({row['link']})")   # link


    