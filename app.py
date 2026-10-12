   import streamlit as st

   st.title("My first demo app")
   text = st.text_input("Type a review")
   if text:
       t = text.lower()
       good = sum(w in t for w in ["good", "great", "love", "excellent", "happy"])
       bad = sum(w in t for w in ["bad", "poor", "hate", "worst", "sad"])
       st.write("Positive" if good > bad else "Negative" if bad > good else "Neutral")
