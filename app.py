import warnings
from KEM import KEM
import streamlit as st

warnings.filterwarnings("ignore")
# Streamlit interface
st.title("Text Analysis")
st.sidebar.header("Parameters")

# Parameters
Input_Answer = st.sidebar.text_area("Text to Enter")
Golden_Answer = st.sidebar.text_area("Answers to Compare seprated by ;")
if  st.sidebar.button("Analyze"):
    if ';' not in Golden_Answer:
        k = KEM(Input_Answer, Golden_Answer.strip())
        k.Extract_and_match()
    elif (len(Golden_Answer.split(';')) >= 1)
        k = KEM(Input_Answer, Golden_Answer.split(';'))
        k.Extract_and_match()
    else:
        k = KEM(Input_Answer)
        k.Extractonly()

