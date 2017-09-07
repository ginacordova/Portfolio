
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[12]:


df=pd.read_csv('911.csv')


# In[15]:


x=df['title'].iloc[0]


# In[16]:


x.split(':')[0]


# In[13]:


df['Reason'] = df['title'].apply(lambda title: title.split()[0])


# In[14]:


df['Reason']


# What is the most common Reason for a 911 call based off of this new column?

# In[17]:


df['Reason'].value_counts()


# Countplot of 911 calls by Reason using seaborn

# In[19]:


sns.countplot(x='Reason', data=df)


# What is the data type of the objects in the timeStamp column?

# In[20]:


df.info()


# Based on the above info() for df, the Data column labeled timeStamp is an object type.

# In[24]:


type(df['timeStamp'].iloc[0])


# The timestamps are strings. Using pd.to_datetime will convert the column values from strings to DateTime objects.

# In[25]:


df['timeStamp']= pd.to_datetime(df['timeStamp'])


# In[26]:


type(df['timeStamp'].iloc[0])


# We can now grab specific attributes from a Datetime object by calling them for example:
# 
#     time=df['timeStamp'].iloc[0]
#     time.hour
#   
# We can use Jupyter's tab method to explore the various attributes we can call. Now that the timestamp column is actually DateTime objects, we use .apply() to create 3 new columns called Hour, Month, and Day of Week. These columns will be created based off of the timeStamp column.
#     
#     

# In[40]:


time=df['timeStamp'].iloc[0]
time.hour


# In[39]:


time


# In[31]:


time.year


# In[32]:


time.dayofweek


# In[34]:


time.month


# Now we will call attributes off of the timeStamp column to create new Hour, Month, and Day of Week columns. 

# In[36]:


df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)


# In[38]:


df['Hour']


# In[43]:


df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)


# In[44]:


df.head()


# Notice how the Day of Week values are integers from 0-6. We will use .map() with this dictionary to map the actual string names to the day of the week:
# 
#     dmap = {0:'Mon', 1:'Tue', 2:'Wed', 3:'Thu', 4:'Fri', 5:'Sat', 6:'Sun'}

# In[45]:


dmap = {0:'Mon', 1:'Tue', 2:'Wed', 3:'Thu', 4:'Fri', 5:'Sat', 6:'Sun'}


# In[46]:


df['Day of Week'] = df['Day of Week'].map(dmap)


# In[47]:


df.head()


# Now we use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column.

# In[54]:


sns.countplot(x='Day of Week', data=df, hue='Reason', palette='viridis')
# To relocate the Legend
plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0.)


# Now we use seaborn to create a countplot of the Month column with the hue based off of the Reason column.

# In[55]:


sns.countplot(x='Month', data=df, hue='Reason', palette='viridis')
# To relocate the Legend
plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0.)


# Create a groupby objected called byMonth, where the DataFrame is grouped by the month column and the count() method is used for agreegation.

# In[59]:


byMonth = df.groupby('Month').count()


# In[65]:


byMonth.head()


# Create a simple plot off of the dataframe indicating the count of calls per month.

# In[62]:


byMonth['lat'].plot()


# Use seaborn's implot() to create a linear fit on the number of calls per month. 

# In[63]:


sns.lmplot(x='Month', y='twp', data=byMonth.reset_index())


# Create a new column called 'Date' that contains the date from the timeStamp column. Using apply() along with date() method.

# In[69]:


t = df['timeStamp'].iloc[0]


# In[70]:


t


# In[72]:


t.date()


# In[74]:


df['Date'] = df['timeStamp'].apply(lambda t: t.date())


# In[76]:


df.head()


# In[79]:


df.groupby('Date').count().head()


# In[81]:


df.groupby('Date').count()['lat']


# In[93]:


df.groupby('Date').count()['lat'].plot()
plt.tight_layout()
plt.title('Date')


# Re-create this plot but create 3 separate plots with each plot representing a Reason for the 911 call.

# In[96]:


df[df['Reason']=='Traffic:'].groupby('Date').count()['lat'].plot()
plt.tight_layout()
plt.title('Traffic')


# In[97]:


df[df['Reason']=='Fire:'].groupby('Date').count()['lat'].plot()
plt.tight_layout()
plt.title('Fire')


# In[98]:


df[df['Reason']=='EMS:'].groupby('Date').count()['lat'].plot()
plt.tight_layout()
plt.title('EMS')


# Create heatmaps with seaborn and our data. The dataframe will first be restructured so that the columns become the Hours and Index becomes the Day of the Week. The unstack method will be used, combined with groupby.

# In[109]:


dayHour=df.groupby(by=['Day of Week', 'Hour']).count()['Reason'].unstack()


# In[114]:


plt.figure(figsize=(12,6))
sns.heatmap(dayHour, cmap='viridis')


# Create a clustermap using this dataframe

# In[120]:


sns.clustermap(dayHour, cmap='viridis')


# In[ ]:




