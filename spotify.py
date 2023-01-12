#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[12]:


df_tracks=pd.read_csv('E:/SQL/spotify.csv')
df_tracks.head()


# In[13]:


#to check the totoal number of null values in each column of the dataset
pd.isnull(df_tracks).sum()


# In[14]:


df_tracks.info()


# In[15]:


#shows the highest number of weeks retained by a song in the topsongs chart
sort_df=df_tracks.sort_values('weeks_on_chart',ascending=False).head(10)
sort_df


# In[16]:


df_tracks.describe().transpose()


# In[17]:


#finding the track name with the respective artist name using iloc 
df_tracks[["track_name","artist_names"]].iloc[30]


# In[ ]:





# In[ ]:





# In[ ]:





# In[18]:


#converting track duration in milliseconds to minutes
df_tracks["duration"]=df_tracks["duration_ms"].apply(lambda x:(x*1.66667e-5))
df_tracks.drop("duration_ms",inplace=True,axis=1)


# In[19]:


df_tracks.duration.head()


# In[48]:


corr_df=df_tracks.drop({"key","mode"},axis=1).corr(method="pearson")
plt.figure(figsize=(14,6))
heatmap=sns.heatmap(corr_df,annot=True,fmt=".1g",vmin=-1,vmax=1,center=0,cmap="inferno",linewidths=1,linecolor="Black")
heatmap.set_title("CORRELATION HEATMAP BETWEEN VARIABLES")
heatmap.set_xticklabels(heatmap.get_xticklabels(),rotation=90)


# 

# In[39]:


#shows total number of dataset present in the excel
sample_df=df_tracks.sample(int(len(df_tracks)))
print(len(sample_df))


# In[45]:


plt.figure(figsize=(10,6))
sns.regplot(data= sample_df,y="loudness",x="energy",color="c").set(title="LOUDNESS VS ENERGY CORRELATION")


# In[46]:


plt.figure(figsize=(10,6))
sns.regplot(data= sample_df,y="weeks_on_chart",x="energy",color="b").set(title="WEEKS ON CHART VS ENERGY CORRELATION")


# In[ ]:





# In[ ]:




