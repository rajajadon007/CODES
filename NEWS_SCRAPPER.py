import streamlit as st
import json
import requests
from newsapi import NewsApiClient
from pandas.io.json import json_normalize
# Create an instance of the NewsApiClient class
newsapi = NewsApiClient(api_key='d5f016a9f9be4a6d817211ca9833172b')

def top_headlines():
    # Get the country and category from the user
    country = st.selectbox("Which country are you interested in?", ["in", "us", "gb", "de", "fr"])
    category = st.selectbox("Which category are you interested in?", ["business", "entertainment", "general", "health", "science", "technology"])

    # Get the top headlines for the specified country and category
    top_headlines = newsapi.get_top_headlines(
        category=category, language='en', country=country,page=5)
    top_headlines = json_normalize(top_headlines['articles'])
    newdf = top_headlines[["title", "url"]]
    dic = newdf.set_index('title')['url'].to_dict()
    for (k, v) in dic.items():
        st.write("**" + k + "**")
        st.write(v)

if __name__ == "__main__":
    st.title("Top Headlines")
    top_headlines()
