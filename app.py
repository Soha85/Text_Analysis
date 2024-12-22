import sys
import warnings
from KEM import KEM
import streamlit as st

warnings.filterwarnings("ignore")
# Streamlit interface
st.title("Text Analysis")
st.sidebar.header("Parameters")

# Parameters
Input_Answer = st.sidebar.text_area("Text to Enter")
Golden_Answer = st.sidebar.text_area("Answer to Compare")
if  st.sidebar.button("Analyze"):
    if (len(Golden_Answer.split(',')) > 1):
        n = len(Golden_Answer)
        lst = Golden_Answer.split(',')
        k = KEM(Input_Answer, lst)
        st.write(k.Extract_and_match())
    else:
        k = KEM(Input_Answer)
        st.write(k.Extractonly())

