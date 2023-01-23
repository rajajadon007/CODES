import streamlit as st
from newsapi import NewsApiClient
import json
import requests
from pandas.io.json import json_normalize
from datetime import datetime , timedelta
import pandas as pd


# Create an instance of the NewsApiClient class
newsapi = NewsApiClient(api_key='d5f016a9f9be4a6d817211ca9833172b')

def top_headlines():
    today = datetime.now()
    start_date = today.strftime("%Y-%m-%d")
    end_date = (today + timedelta(days=7)).strftime("%Y-%m-%d")
    
    # Get the country and category from the user
    country = st.selectbox("Which country are you interested in?", ["in", "us", "gb", "de", "fr"])
    category = st.selectbox("Which category are you interested in?", ["business", "entertainment", "general", "health", "science", "technology"])
    keyword = st.text_input("Enter keyword")
    if keyword:
        news = newsapi.get_everything(q=keyword,
                                      from_param=start_date,
                                      to=end_date,
                                      language='en',
                                      sort_by='relevancy')
    else:
        news = newsapi.get_top_headlines(
            category=category,
            language='en',
            country=country,
            from_param=start_date,
            to=end_date)
        
    if news["status"] == "ok":
        st.write("Results Found : ", news["totalResults"])
     
        df = pd.DataFrame(news['articles'])
        st.dataframe(df)
       
    else:
        st.write("Sorry, No results found")

if __name__ == "__main__":
 st.title("Top Headlines")
 top_headlines()
