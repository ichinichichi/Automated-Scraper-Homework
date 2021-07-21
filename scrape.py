#!/usr/bin/env python
# coding: utf-8

# # Automating Scraper Homework

# Objective: Sending out an e-mail every time there were changes made in the contents of the travel restrictions from the Ministry of Foreign Affairs Website Japan and showing the changes.

# ## Scraping the website

# In[34]:


import requests
r = requests.get('https://www.mofa.go.jp/ca/fna/page4e_001053.html')
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
scrapeddate= soup.find('div', attrs={'class':'rightalign'}).text
scrapeddate


# In[57]:


sectioncontent=soup.find_all('div', attrs={'class':'main-section section'})
len(sectioncontent)


# In[58]:


# looping through all the sections to get the title and content

records = []
for section in sectioncontent:
    Section_Title=section.find('h2', attrs={'class':'title2'}).text
    Content = section.find('div', attrs={'class':'any-area'}).text
    records.append((Section_Title, Content))
records


# In[65]:


# turn into a dataframe
import pandas as pd
df = pd.DataFrame(records, columns=['Title', 'Content'])

# add a title with the last update date
df.style.set_caption(f'Last Updated: {scrapeddate}')


# In[ ]:


# save as csv
df.to_csv('mofa.csv', index=False, encoding='utf-8')

