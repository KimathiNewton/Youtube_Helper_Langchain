import streamlit as st
import langchain_helper as lch
import textwrap

st.title("YouTube Assistant")
st.write("""I'm here to assist you in answering questions about the Youtube video you share. 
            Just paste the link to the Youtube video and feel free to ask me anything!""")

st.image("Images/Youtube_Helper.jpg")
with st.sidebar:
    with st.form(key='my_form'):
        youtube_url = st.sidebar.text_area(
            label="What is the YouTube video URL?",
            max_chars=50
            )
        query = st.sidebar.text_area(
            label="Ask me about the video?",
            max_chars=50,
            key="query"
            )
        openai_api_key = st.sidebar.text_input(
            label="OpenAI API Key",
            key="langchain_search_api_key_openai",
            max_chars=100,
            type="password"
            )
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
        "[View the source code](https://github.com/Newton23-nk/Youtube_Helper_Langchain)"
        submit_button = st.form_submit_button(label='Submit')

if query and youtube_url:
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    else:
        db = lch.create_db_from_youtube_video_url(youtube_url)
        response, docs = lch.get_response_from_query(db, query)
        st.subheader("Answer:")
        st.text(textwrap.fill(response, width=85))
