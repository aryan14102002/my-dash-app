#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from plotly.offline import iplot


# In[2]:


df03 = pd.read_csv("2003.csv")


# In[3]:


df04 = pd.read_csv("2004.csv")


# In[4]:


df05 = pd.read_csv("2005.csv")


# In[5]:


# df06 = pd.read_csv("2006.csv")


# # In[6]:


# df07 = pd.read_csv("2007.csv")


# # In[7]:


# df08 = pd.read_csv("2008.csv")


# # In[8]:


# df09 = pd.read_csv("2009.csv")


# # In[9]:


# df10 = pd.read_csv("2010.csv")


# # In[10]:


# df11 = pd.read_csv("2011.csv")


# # In[11]:


# df12 = pd.read_csv("2012.csv")


# # In[12]:


# df13 = df = pd.read_csv('2013.csv')


# # In[13]:


# df14 = pd.read_csv('2014.csv')


# # In[14]:


# df15 = pd.read_csv('2015.csv')


# # In[15]:


# df16 = pd.read_csv('2016.csv')


# # In[16]:


# df17 = pd.read_csv('2017.csv')


# # In[17]:


# df18 = pd.read_csv('2018.csv')


# # In[18]:


# df19 = pd.read_csv('2019.csv')


# In[19]:


#df20 = pd.read_csv('2020.csv')


# In[20]:


#df21 = pd.read_csv('2021.csv')


# In[21]:


#df22 = pd.read_csv('2022.csv')


# In[22]:


df_all = pd.concat([df03, df04, df05])#, df06, df07, df08, df09, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20, df21, df22])


# In[24]:



# In[25]:



# In[26]:


del df03, df04, df05#, df06, df07, df08, df09, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20, df21, df22


# In[27]:


def dataframe(isi):
    IN = df_all.loc[df_all['ISIN'].isin([isi])]
    arr = ['']*240
    month = ['January','February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for j in range(0,3):
        for i in range(0,12):
               arr[12*j+i]= month[i]+" "+str(2003+j)
                
    m = []
    for i in range(0,36):
        Mon = IN.loc[IN['Trade Date'].isin([arr[i]])]
        ax =  Mon.describe()
        a = ax['YTM / Yield'][1]
        m.append(a)
    ytm = pd.DataFrame(list(zip(arr, m)))
    ytm.set_axis(['Month', 'YTM'], axis='columns', inplace=True)
    return ytm


# In[28]:



app = dash.Dash()   #initialising dash app
server = app.server
app.layout = html.Div(id = 'parent', children = [
    html.Div([
    html.H1(id = 'H1', children = 'YTM vs TIME', style = {'textAlign':'center',\
                                            'marginTop':40,'marginBottom':40}),

        
        dcc.Dropdown( id = 'dropdown',
        options = [
            {'label':'6.30% GS 2023', 'value':'IN0020030014' },
            {'label': '7.37% GS 2023', 'value':'IN0020180025'},
            {'label': '4.26% GS 2023', 'value':'IN0020210046'},
            {'label': '7.16% GS 2023', 'value': 'IN0020130012'},
            {'label': '1.44% IIGS 2023', 'value': 'IN0020130046'},
            {'label': '6.17% GS 2023 conv', 'value': 'IN0020030055'},
            {'label': '4.48% GS 2023', 'value': 'IN0020200211'},
            {'label': '4.56% GS 2023', 'value': 'IN0020210210'},
            {'label': '8.83% GS 2023', 'value': 'IN0020130061'},
            {'label': '7.68% GS 2023', 'value': 'IN0020150010'},
            {'label': '7.32% GS 2024', 'value': 'IN0020180488'},
            {'label': '7.35% GS 2024', 'value': 'IN0020090034'},
            {'label': '6.69% GS 2024', 'value': 'IN0020220052'},
            {'label': '8.40% GS 2024', 'value': 'IN0020140045'},
            {'label': '6.18% GS 2024', 'value': 'IN0020190396'},
            {'label': 'FRB 2024', 'value': 'IN0020160084'},
            {'label': '9.15% GS 2024', 'value': 'IN0020110048'},
            {'label': '6.89% GS 2025', 'value': 'IN0020220128'},
            {'label': '7.72% GS 2025', 'value': 'IN0020150036'},
            {'label': '5.22% GS 2025', 'value': 'IN0020200112'},
            {'label': '8.20% GS 2025', 'value': 'IN0020120047'},
            {'label': '5.97% GS 2025 conv', 'value': 'IN0020030071'},
            {'label': '5.15% GS 2025', 'value': 'IN0020200278'},
            {'label': '7.59% GS 2026', 'value': 'IN0020150093'},
            {'label': '7.27% GS 2026', 'value': 'IN0020190016'},
            {'label': '5.63% GS 2026', 'value': 'IN0020210012'},
            {'label': '8.33% GS 2026', 'value': 'IN0020120039'},
            {'label': '6.97% GS 2026', 'value': 'IN0020160035'},
            {'label': '10.18% GS 2026', 'value': 'IN0020010081'},
            {'label': '5.74% GS 2026', 'value': 'IN0020210186'},
            {'label': '8.15% GS 2026', 'value': 'IN0020140060'},
            {'label': '8.24% GS 2027', 'value': 'IN0020060078'},
            {'label': '6.79% GS 2027', 'value': 'IN0020170026'},
            {'label': '7.38% GS 2027', 'value': 'IN0020220037'},
            {'label': '8.26% GS 2027', 'value': 'IN0020070036'},
            {'label': '8.28% GS 2027', 'value': 'IN0020070069'},
            {'label': '6.01% GS 2028 C Align', 'value': 'IN0020020247'},
            {'label': '7.17% GS 2028', 'value': 'IN0020170174'},
            {'label': '7.10% GOI SGrB 2028', 'value': 'IN0020220136'}, 
            {'label': '8.60% GS 2028', 'value': 'IN0020140011'},
            {'label': '6.13% GS 2028', 'value': 'IN0020030022'},
            {'label': 'FRB 2028', 'value': 'IN0020210160'},
            {'label': '7.59% GS 2029', 'value': 'IN0020150069'},
            {'label': '7.26% GS 2029', 'value': 'IN0020180454'},
            {'label': '7.10% GS 2029', 'value': 'IN0020220011'},
            {'label': '6.45% GS 2029', 'value': 'IN0020190362'},
            {'label': '6.79% GS 2029', 'value': 'IN0020160118'},
            {'label': '7.88% GS 2030', 'value': 'IN0020150028'},
            {'label': '7.61% GS 2030', 'value': 'IN0020160019'},
            {'label': '5.79% GS 2030', 'value': 'IN0020200070'},
            {'label': '5.77% GS 2030', 'value': 'IN0020200153'},
            {'label': '9.20% GS 2030', 'value': 'IN0020130053'},
            {'label': '5.85% GS 2030', 'value': 'IN0020200294'},
            {'label': '8.97% GS 2030', 'value': 'IN0020110055'},
            {'label': '6.10% GS 2031', 'value': 'IN0020210095'},
            {'label': '6.68% GS 2031', 'value': 'IN0020170042'},
            {'label': 'FRB 2031', 'value': 'IN0020180041'},
            {'label': '6.54% GS 2032', 'value': 'IN0020210244'},
            {'label': '8.28% GS 2032', 'value': 'IN0020060086'},
            {'label': '8.32% GS 2032', 'value': 'IN0020070044'},
            {'label': '7.26% GS 2032', 'value': 'IN0020220060'},
            {'label': '7.95% GS 2032', 'value': 'IN0020020106'},
            {'label': '8.33% GS 2032', 'value': 'IN0020070077'},
            {'label': '7.29% GOI SGrB 2033', 'value': 'IN0020220144'},
            {'label': '7.57% GS 2033', 'value': 'IN0020190065'},
            {'label': 'FRB 2033', 'value': 'IN0020200120'},
            {'label': '8.24% GS 2033', 'value': 'IN0020140052'},
            {'label': '6.57% GS 2033', 'value': 'IN0020160100'},
            {'label': '7.50% GS 2034', 'value': 'IN0020040039'},
            {'label': '6.19% GS 2034', 'value': 'IN0020200096'},
            {'label': 'FRB 2034', 'value': 'IN0020210137'},
            {'label': '7.73% GS 2034', 'value': 'IN0020150051'},
            {'label': 'FRB, 2035', 'value': 'IN0020042050'},
            {'label': '6.22% GS 2035', 'value': 'IN0020200245'},
            {'label': '6.64% GS 2035', 'value': 'IN0020210020'},
            {'label': '7.40% GS 2035', 'value': 'IN0020050012'},
            {'label': '6.67% GS 2035', 'value': 'IN0020210152'},
            {'label': '7.54% GS 2036', 'value': 'IN0020220029'},
            {'label': '8.33% GS 2036', 'value': 'IN0020060045'},
            {'label': '7.41% GS 2036', 'value': 'IN0020220102'},
            {'label': '6.83% GS 2039', 'value': 'IN0020080050'},
            {'label': '7.62% GS 2039', 'value': 'IN0020190024'},
            {'label': '8.30% GS 2040', 'value': 'IN0020100031'},
            {'label': '8.83% GS 2041', 'value': 'IN0020110063'},
            {'label': '8.30% GS 2042', 'value': 'IN0020120062'},
            {'label': '7.69% GS 2043', 'value': 'IN0020190040'},
            {'label': '9.23% GS 2043', 'value': 'IN0020130079'},
            {'label': '8.17% GS 2044', 'value': 'IN0020140078'},
            {'label': '8.13% GS 2045', 'value': 'IN0020150044'},
            {'label': '7.06% GS 2046', 'value': 'IN0020160068'},
            {'label': '7.72% GS 2049', 'value': 'IN0020190032'},
            {'label': '7.16% GS 2050', 'value': 'IN0020200054'},
            {'label': '6.67% GS 2050', 'value': 'IN0020200252'},
            {'label': '6.62% GS 2051', 'value': 'IN0020160092'},
            {'label': '6.99% GS 2051', 'value': 'IN0020210194'},
            {'label': '7.36% GS 2052', 'value': 'IN0020220086'},
            {'label': '7.72% GS 2055', 'value': 'IN0020150077'},
            {'label': '7.63% GS 2059', 'value': 'IN0020190057'},
            {'label': '7.19% GS 2060', 'value': 'IN0020200039'},
            {'label': '6.80% GS 2060', 'value': 'IN0020200187'},
            {'label': '6.76% GS 2061', 'value': 'IN0020200401'},
            {'label': '6.95% GS 2061', 'value': 'IN0020210202'},
            {'label': '7.40% GS 2062', 'value': 'IN0020220094'},
            ],
                     
        value = 'IN0020030014'),
        dcc.Graph(id = 'line_plot'),
    ]),
    
])
    


# In[29]:


@app.callback(Output(component_id='line_plot', component_property= 'figure'),
              [Input(component_id='dropdown', component_property= 'value')])
def plotone(dropdown_value):
    df = dataframe(dropdown_value)
    df = df.dropna()
    fig = px.line(df, x = 'Month', y = 'YTM', title='YTM for 2003-2022')
    return fig


# In[30]:


if __name__ == '__main__':
    app.run_server()


# In[ ]:




