import streamlit as st
from newsapi import NewsApiClient
import json
import requests
from pandas.io.json import json_normalize


# Create an instance of the NewsApiClient class
newsapi = NewsApiClient(api_key='d5f016a9f9be4a6d817211ca9833172b')

def top_headlines():
    # Get the country and category from the user
    country = st.selectbox("Which country are you interested in?", ["in", "us", "gb", "de", "fr"])
    category = st.selectbox("Which category are you interested in?", ["business", "entertainment", "general", "health", "science", "technology"])
    start_date = st.date_input("Start date")
    end_date = st.date_input("End date")
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
        all_articles = news["articles"]
        for article in all_articles:
            st.write("**" + article["title"] + "**")
            st.write("Source : ", article["source"]["name"])
            st.write("Published at : ", article["publishedAt"])
            st.write(article["url"])
            st.write("\n\n")
    else:
        st.write("Sorry, No results found")

if __name__ == "__main__":
 st.title("Top Headlines")
   top_headlines()
