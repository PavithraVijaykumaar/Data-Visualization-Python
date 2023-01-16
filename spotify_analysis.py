#!/usr/bin/env python
# coding: utf-8

# # IMPORTING NECESSARY LIBRARIES

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # IMPORTING EXCEL

# In[9]:


df_tracks=pd.read_csv('E:/DA_PROJECTS/spotify.csv')
df_tracks.head()


# # checking total number of null values in each column of the dataset

# In[7]:


pd.isnull(df_tracks).sum()


# # SHOWING THE DATATYPES

# In[8]:


df_tracks.info()


# # Highest number of weeks retained by a song in the topsongs chart

# In[10]:


sort_df=df_tracks.sort_values('weeks_on_chart',ascending=False).head(10)
sort_df


# In[11]:


df_tracks.describe().transpose()


# # Showing track name with the respective artist using iloc 

# In[12]:


df_tracks[["track_name","artist_names"]].iloc[30]


# # converting track duration in milliseconds to minutes

# In[ ]:


df_tracks["duration"]=df_tracks["duration_ms"].apply(lambda x:(x*1.66667e-5))
df_tracks.drop("duration_ms",inplace=True,axis=1)


# In[14]:


df_tracks.duration.head()


# # Creating correlation heatmap using PEARSON method

# In[15]:


corr_df=df_tracks.drop({"key","mode"},axis=1).corr(method="pearson")
plt.figure(figsize=(14,6))
heatmap=sns.heatmap(corr_df,annot=True,fmt=".1g",vmin=-1,vmax=1,center=0,cmap="inferno",linewidths=1,linecolor="Black")
heatmap.set_title("CORRELATION HEATMAP BETWEEN VARIABLES")
heatmap.set_xticklabels(heatmap.get_xticklabels(),rotation=90)


# # Total number of dataset in the excel

# In[16]:


sample_df=df_tracks.sample(int(len(df_tracks)))
print(len(sample_df))


# # Correlation betwen loudness and energy

# In[17]:


plt.figure(figsize=(10,6))
sns.regplot(data= sample_df,y="loudness",x="energy",color="c").set(title="LOUDNESS VS ENERGY CORRELATION")


# # Correlation between danceability and tempo

# In[18]:


plt.figure(figsize=(10,6))
sns.regplot(data= sample_df,y="danceability",x="tempo",color="b").set(title="DANCEABILITY VS TEMPO CORRELATION")


# # Correlation between acousticness and tempo

# In[25]:


plt.figure(figsize=(10,6))
sns.regplot(data= sample_df,y="acousticness",x="tempo",color="g").set(title="ACOUSTICNESS VS TEMPO CORRELATION")


# In[ ]:




