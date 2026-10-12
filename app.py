import streamlit as st
st.title("My first demo app v2")
text = st.text_input("Type a review").lower()
good = sum(w in text for w in ["good", "great", "love", "excellent", "happy"])
bad = sum(w in text for w in ["bad", "poor", "hate", "worst", "sad"])
st.write("Type something above" if text == "" else "Positive" if good > bad else "Negative" if bad > good else "Neutral")
