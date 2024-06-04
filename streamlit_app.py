import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Samsung Lions!!


"""
with open('https://m.sports.naver.com/game/20240604SSSK02024','r') as f:
    html_string=f.read()
st.markdown(html_string, unsafe_allow_html=True)
