#!/usr/bin/env python
# coding: utf-8

# # The Sparks Foundation
# 
# ## Intern Name: Shweta Nalawade
# 
# ## Task 3: Exploratory Data Analysis on dataset ‘SampleSuperstore’

# ### In this task as business manager,I have to find out weak areas where I can work to make profit.

# In[115]:


# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
get_ipython().run_line_magic('matplotlib', 'inline')


# In[116]:


data_df = pd.read_csv("D:\downloads\SampleSuperstore.csv")


# In[117]:


data_df


# In[118]:


data_df.drop_duplicates().sum()
data_df.shape


# In[119]:


data_df


# ### So in this dataset total 17 duplicate columns are found hence we will eliminate them.

# In[120]:


data_df.drop_duplicates(inplace = True)
data_df.shape


# In[123]:


data_df
del data_df['Country']


# In[124]:


data_df


# In[125]:


del data_df['Postal Code']


# In[126]:


data_df


# In[181]:


data_df.isnull().any()


# #### This means we dont have null data

# In[182]:


financial = data_df.loc[:,['Sales','Quantity','Discount','Profit']]
sns.pairplot(financial)


# In[183]:


correlation = financial.corr()
sns.heatmap(correlation,xticklabels = correlation.columns, yticklabels = correlation.columns , annot = True)


# ### From the above heatmet we can observe that there is negative correlation between profit and discount which indicates higher discounts gives lesser profits.

# In[134]:


num_data.describe()


# ## Finding total sales and profits of the company

# In[141]:


sales_and_profits = data_df.groupby("Segment").sum().iloc[:,[1,-1]].sum()
round(sales_and_profits,2)


# ### In this step we will find top ten states by sales and profit 

# In[146]:


Top_10_sales = data_df.groupby("State").Sales.sum().nlargest(n=10)
Top_10_profits = data_df.groupby("State").Profit.sum().nlargest(n = 10)
Top_10_sales.index


# In[147]:


Top_10_profits.index


# In[158]:


plt.style.use('seaborn')
Top_10_sales.plot(kind = 'bar',figsize = (15,9),fontsize = 16)
plt.xlabel('states',fontsize = 16)
plt.ylabel('Total sales',fontsize = 16)
plt.title("Top 10 states by sales",fontsize = 16)
plt.show()


# In[165]:


plt.style.use('seaborn')
Top_10_profits.plot(kind = 'bar',figsize = (15,9),fontsize = 16, color = 'green')
plt.xlabel('states',fontsize = 16)
plt.ylabel('Total Profits',fontsize = 16)
plt.title("Top 10 states by Profits",fontsize = 16)
plt.show()


# ## Above graph shows that we have got highest profits in New York and California

# In[170]:


plt.style.use('seaborn')
data_df.plot(kind = "scatter",figsize = (15,9), x = "Sales", y= "Profit", c = "Discount", s = 20,fontsize = 16, marker = "o", colormap = "viridis")
plt.ylabel('Total Profits',fontsize = 16)
plt.title("Interdependency of Sales,Profits and Discounts",fontsize = 16)
plt.show()


# In[174]:


plt.figure(figsize=(15,10))
data_df['Sub-Category'].value_counts().plot.pie(autopct = '%1.1f%%')
plt.show()


# ## From the above plots we can conclude that
# ### 1. Profits and sales are positively correlated
# ### 2. Discounts and Profits are negatively correlated

# ## Conclusion
# ### 1. If we give more Discount on our products sales will increass but profit goes down
# ### 2. We should concentrate on the sales of 'west Virginia' and 'san Luis   Obispo'and'Woodland' city.   
# ### 3. For getting more profit we should sale more products to the states which are licking our products like 'New York' and 'California'.
# 

# # Thank you!

# In[ ]:




