import pandas as pdimport numpy as npimport streamlit as stst.title("Sentiment Analysis and LSTM")st.markdown("A machine learning analysis of apple stock informed by twitter sentiment over time. Submitted as a final project by Farhang Douroudian, Yuwen Yu and Liam Sweeney")def get_tweets():    tweets = pd.read_csv("https://raw.githubusercontent.com/LiamMerrill/LSTM/main/tweets_02.csv")    return (tweets)df = get_tweets()st.write(df)