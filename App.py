import streamlit as st

col1, col2 = st.columns(2) 

with col1 :
    st.title("T-Rex Runner Game")
    game_url = "https://vianroyal.github.io/t-rex-runner/"
    st.markdown(
        f"""
        <iframe src="{game_url}" width="800" height="600" frameborder="0"></iframe>
        """,
        unsafe_allow_html=True,
        '<div style="text-align: left;'> game_url </div>', unsafe_allow_html=True
    )

with col2:
    cap = Videocapture(0)
