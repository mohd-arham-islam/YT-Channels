#!/usr/bin/env python
# coding: utf-8

# ### Importing the libraries

# In[2]:


from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns


# ### Raising request to the Youtube API to get the data (Using google-client-api)

# In[3]:


api_key = 'AIzaSyAu8S7E4EzMJKP0g2NgoG5NY_KWydfdmho'
channel_id = ['UCHnyfMqiRRG1u-2MsSQLbXA', #Veritasium
              'UC9x0AN7BWHpCDHSm9NiJFJQ', #NetworkChuck
              'UCRI00CwLZdLRCWg5BdDOsNw', #CanadianLad
              'UCY1kMZp36IQSyNx_9h4mpCg'  #MarkRober
             ]
youtube = build('youtube','v3',developerKey=api_key)


# ### Defining a function that returns a list of channel data

# In[4]:


def get_stats(youtube,channel_id):
    channel_data = list()
    request = youtube.channels().list(part ='snippet,contentDetails,statistics',id =','.join(channel_id))
    response = request.execute()
    for i in range(len(response['items'])):
        data = dict(Channel_Name = response['items'][i]['snippet']['title'], Subscribers_M = response['items'][i]['statistics']['subscriberCount'], Total_Views = response['items'][i]['statistics']['viewCount'], Total_Videos = response['items'][i]['statistics']['videoCount'])
        channel_data.append(data)
    return channel_data


# ### Storing the data in a Data Frame using Pandas

# In[5]:


channel_stats = get_stats(youtube,channel_id)
channel_data = pd.DataFrame(channel_stats)
channel_data['Subscribers_M']=pd.to_numeric(channel_data['Subscribers_M'])
channel_data['Total_Views']=pd.to_numeric(channel_data['Total_Views'])
channel_data['Total_Videos']=pd.to_numeric(channel_data['Total_Videos'])
channel_data['Subscribers_M']=(channel_data['Subscribers_M']/1000000)
channel_data


# ### Plotting the data using Seaborn 

# In[6]:


sns.barplot(x='Channel_Name',y='Subscribers_M',data = channel_data).set(title='Subscribers (in Millions)')


# In[7]:


sns.barplot(x='Channel_Name',y='Total_Views',data = channel_data).set(title='Total Views (in Billions)')


# In[9]:


sns.barplot(x='Channel_Name',y='Total_Videos',data=channel_data).set(title='Total Videos Uploaded')


# In[ ]:




