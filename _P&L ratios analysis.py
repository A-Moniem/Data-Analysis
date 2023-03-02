#!/usr/bin/env python
# coding: utf-8

# # Import different libraries

# In[1]:


import pandas as pd
import requests
import json
import plotly.graph_objects as go


# # Request Google financial statement "P&L" from "Financial Modeling Prep"
# 
# # Get the income statement for any company by change the company name in the {quote}

# In[2]:


def selectquote(quote):
       PL = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{quote}?limit=120&apikey=b5b0d168348e66678fcbabfeb75a9dc5")

       # Change the data to Dict
       PL = PL.json()

       # Create the data as dataframe
       df = pd.DataFrame.from_dict(PL)
       df = df.T
       df.columns = df.iloc[0]
       df.reset_index(inplace=True)
       df = df.iloc[8:36, 0:5]
       return df
df = selectquote('GOOG')
df.head()


# # Change the data from Object to numbers

# In[3]:


cols = df.columns.drop('index')
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
df.info()


# In[4]:


df.head()


# # Change the column names to years

# In[5]:


df.rename(columns={"index": "Description", df.columns[1]: "2022",df.columns[2]: "2021", df.columns[3]: "2020",
df.columns[4]: "2019"}, inplace=True)
df.head()


# # Create P&L ratios for all the statement elements

# In[6]:


df['2022_Ratios'] = df['2022'] / df.iloc[0,1]
df['2022_Ratios'] = pd.Series(['{:.2f}%'.format(val*100) for val in df['2022_Ratios']], index=df.index)
df['2021_Ratios'] = df['2021'] / df.iloc[0,2]
df['2021_Ratios'] = pd.Series(['{:.2f}%'.format(val*100) for val in df['2021_Ratios']], index=df.index)
df['2020_Ratios'] = df['2020'] / df.iloc[0,3]
df['2020_Ratios'] = pd.Series(['{:.2f}%'.format(val*100) for val in df['2020_Ratios']], index=df.index)
df['2019_Ratios'] = df['2019'] / df.iloc[0,4]
df['2019_Ratios'] = pd.Series(['{:.2f}%'.format(val*100) for val in df['2019_Ratios']], index=df.index)
df.head()


# # Creat variables for the statement elements

# In[7]:


# 2022 Variables
Rev22 = df[df['Description'] == 'revenue'].iloc[0][5]
COGS22 = df[df['Description'] == 'costOfRevenue'].iloc[0][5]
GrossProfit22 = df[df['Description'] == 'grossProfit'].iloc[0][5]
OperatingExp22 = df[df['Description'] == 'operatingExpenses'].iloc[0][5]
OperatingIncome22 = df[df['Description'] == 'operatingIncome'].iloc[0][5]
PretaxIncome22 = df[df['Description'] == 'incomeBeforeTax'].iloc[0][5]
NetIncome22 = df[df['Description'] == 'netIncome'].iloc[0][5]

# 2021 Variables

Rev21 = df[df['Description'] == 'revenue'].iloc[0][6]
COGS21 = df[df['Description'] == 'costOfRevenue'].iloc[0][6]
GrossProfit21 = df[df['Description'] == 'grossProfit'].iloc[0][6]
OperatingExp21 = df[df['Description'] == 'operatingExpenses'].iloc[0][6]
OperatingIncome21 = df[df['Description'] == 'operatingIncome'].iloc[0][6]
PretaxIncome21 = df[df['Description'] == 'incomeBeforeTax'].iloc[0][6]
NetIncome21 = df[df['Description'] == 'netIncome'].iloc[0][6]

# 2020 Variables

Rev20 = df[df['Description'] == 'revenue'].iloc[0][7]
COGS20 = df[df['Description'] == 'costOfRevenue'].iloc[0][7]
GrossProfit20 = df[df['Description'] == 'grossProfit'].iloc[0][7]
OperatingExp20 = df[df['Description'] == 'operatingExpenses'].iloc[0][7]
OperatingIncome20 = df[df['Description'] == 'operatingIncome'].iloc[0][7]
PretaxIncome20 = df[df['Description'] == 'incomeBeforeTax'].iloc[0][7]
NetIncome20 = df[df['Description'] == 'netIncome'].iloc[0][7]

# 2019 Variables

Rev19 = df[df['Description'] == 'revenue'].iloc[0][8]
COGS19 = df[df['Description'] == 'costOfRevenue'].iloc[0][8]
GrossProfit19 = df[df['Description'] == 'grossProfit'].iloc[0][8]
OperatingExp19 = df[df['Description'] == 'operatingExpenses'].iloc[0][8]
OperatingIncome19 = df[df['Description'] == 'operatingIncome'].iloc[0][8]
PretaxIncome19 = df[df['Description'] == 'incomeBeforeTax'].iloc[0][8]
NetIncome19 = df[df['Description'] == 'netIncome'].iloc[0][8]


# # Create waterfall to compare the P&L ratios for the 4 years for the main P&L elements

# In[8]:


fig = go.Figure()

fig.add_trace(go.Waterfall(
    x = [["2022", "2022", "2022", "2022", "2022", "2022", "2022", "2022"],
        ["Revenue", "COGS", "GrossProfit", "OperatingExp", "OperatingIncome","PretaxIncome","NetIncome"]],
    measure = ["absolute", "absolute", "absolute", "absolute", "absolute", "absolute", "absolute"],
    textposition = "outside",
    text = [Rev22, COGS22, GrossProfit22, OperatingExp22, OperatingIncome22, PretaxIncome22, NetIncome22],
    y = [Rev22, COGS22, GrossProfit22, OperatingExp22, OperatingIncome22, PretaxIncome22, NetIncome22 ],
    base = 1000
))


fig.add_trace(go.Waterfall(
    x = [["2021", "2021", "2021", "2021", "2021", "2021", "2021", "2021"],
        ["Revenue", "COGS", "GrossProfit", "OperatingExp", "OperatingIncome","PretaxIncome","NetIncome"]],
    measure = ["absolute", "absolute", "absolute", "absolute", "absolute", "absolute", "absolute"],
    textposition = "outside",
    text = [Rev21, COGS21, GrossProfit21, OperatingExp21, OperatingIncome21, PretaxIncome21, NetIncome21],
    y = [Rev21, COGS21, GrossProfit21, OperatingExp21, OperatingIncome21, PretaxIncome21, NetIncome21],
    base = 1000
))

fig.add_trace(go.Waterfall(
    x = [["2020", "2020", "2020", "2020", "2020", "2020", "2020", "2020"],
        ["Revenue", "COGS", "GrossProfit", "OperatingExp", "OperatingIncome","PretaxIncome","NetIncome"]],
    measure = ["absolute", "absolute", "absolute", "absolute", "absolute", "absolute", "absolute"],
    textposition = "outside",
    text = [Rev20, COGS20, GrossProfit20, OperatingExp20, OperatingIncome20, PretaxIncome20, NetIncome20],
    y = [Rev20, COGS20, GrossProfit20, OperatingExp20, OperatingIncome20, PretaxIncome20, NetIncome20],
    base = 1000
))

fig.add_trace(go.Waterfall(
    x = [["2019", "2019", "2019", "2019", "2019", "2019", "2019", "2019"],
        ["Revenue", "COGS", "GrossProfit", "OperatingExp", "OperatingIncome","PretaxIncome","NetIncome"]],
    measure = ["absolute", "absolute", "absolute", "absolute", "absolute", "absolute", "absolute"],
    textposition = "outside",
    text = [Rev19, COGS19, GrossProfit19, OperatingExp19, OperatingIncome19, PretaxIncome19, NetIncome19],
    y = [Rev19, COGS19, GrossProfit19, OperatingExp19, OperatingIncome19, PretaxIncome19, NetIncome19],
    base = 1000
))


fig.update_layout(
    waterfallgroupgap = 0.0,
        title = 'Google P&L ratios for the past 4 years'
    
)

fig.show()


# In[ ]:




