import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
import requests
import random

# Page layout
## Page expands to full width
st.set_page_config(layout="wide")

#---------------------------------#
# Title

#image = Image.open('logo.jpg')
#st.image(image, width = 500)

st.title('Meal App')
st.markdown("""
Random meal generation from www.giallozafferano.it
""")

#---------------------------------#
# Page layout (continued)
## Divide page to 3 columns (col1 = sidebar, col2 and col3 = page contents)
col2, col3 = st.beta_columns((3,1))

#---------------------------------#
if st.button('Antipasti'):

    # Web scraping of CoinMarketCap data
    @st.cache
    def antipasti():

        title_list = []
        url_list = []

        for page in range(0,85):
            try:
                cmc = requests.get(f'https://www.giallozafferano.it/ricette-cat/page{page}/Antipasti/')
                #cmc.content

                soup = BeautifulSoup(cmc.content, 'html.parser')

                # retrieve recipes titles and urls
                article = soup.find_all('article')
                for  i in article:
                    info = i.find_all("div", {'class': 'gz-description'})#.find('a')
                    for c in info:
                        title = c.find('a')['title']
                        url = c.find('a')['href']
                        
                        # append to list
                        title_list.append(title)
                        url_list.append(url)
            except:
                pass

    
        df = pd.DataFrame(list(zip(title_list,url_list)), columns=['title', 'url'])
        return df
    
    df = antipasti()

    # random select
    rand = random.randint(10, len(df))
    st.subheader('Random generation')
    st.dataframe(df.iloc[rand])
    st.subheader('Full list')
    st.dataframe(df)


if st.button('Primi'):

    # Web scraping of CoinMarketCap data
    @st.cache
    def primi():

        title_list = []
        url_list = []

        for page in range(0,85):
            try:
                cmc = requests.get(f'https://www.giallozafferano.it/ricette-cat/page{page}/Primi/')
                #cmc.content

                soup = BeautifulSoup(cmc.content, 'html.parser')

                # retrieve recipes titles and urls
                article = soup.find_all('article')
                for  i in article:
                    info = i.find_all("div", {'class': 'gz-description'})#.find('a')
                    for c in info:
                        title = c.find('a')['title']
                        url = c.find('a')['href']
                        
                        # append to list
                        title_list.append(title)
                        url_list.append(url)
            except:
                pass


        df = pd.DataFrame(list(zip(title_list,url_list)), columns=['title', 'url'])
        return df

    df = primi()

    # random select
    rand = random.randint(10, len(df))
    st.subheader('Random generation')
    st.dataframe(df.iloc[rand])
    st.subheader('Full list')
    st.dataframe(df)
    
    
if st.button('Secondi'):

    # Web scraping of CoinMarketCap data
    @st.cache
    def secondi():

        title_list = []
        url_list = []

        for page in range(0,85):
            try:
                cmc = requests.get(f'https://www.giallozafferano.it/ricette-cat/page{page}/Secondi-piatti/')
                #cmc.content

                soup = BeautifulSoup(cmc.content, 'html.parser')

                # retrieve recipes titles and urls
                article = soup.find_all('article')
                for  i in article:
                    info = i.find_all("div", {'class': 'gz-description'})#.find('a')
                    for c in info:
                        title = c.find('a')['title']
                        url = c.find('a')['href']
                        
                        # append to list
                        title_list.append(title)
                        url_list.append(url)
            except:
                pass

        df = pd.DataFrame(list(zip(title_list,url_list)), columns=['title', 'url'])
        return df

    df = secondi()

    # random select
    rand = random.randint(10, len(df))
    st.subheader('Random generation')
    st.dataframe(df.iloc[rand])
    st.subheader('Full list')
    st.dataframe(df)




   