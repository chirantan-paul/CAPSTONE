import io
import numpy as np
import altair as alt
import pandas as pd
from pandas import json_normalize
import streamlit as st
from urllib.request import urlopen
import json
import matplotlib.pyplot

url1 = "https://thingspeak.com/channels/1995845/feed.json"
url2 = "https://thingspeak.com/channels/1538779/feeds/last.json"
response1 = urlopen(url1)
response2 = urlopen(url2)
data_json1 = json.loads(response1.read())
st.json(data_json1)
data_json2 = json.loads(response2.read())
st.write(data_json2)

dataframe=json_normalize(data_json1['feeds'])
dafra=pd.DataFrame(data_json1['feeds'], columns=['field1','field2','field3'])
st.title("Welcome To Our Boost Converter Monitoring Online UI")
st.write("Click to see the current parameters")
menu = ["Home", "Analysis"]
choice = st.sidebar.selectbox('Menu',menu)
if(choice=='Home'):
    st.write("Check out Analysis section")
elif(choice=='Analysis'):
    st.write("Streamlit From Colab")
    st.write(dataframe)
    st.line_chart(dataframe['field1'])
    st.bar_chart(dataframe['field1'])
    st.line_chart(dataframe['field2'])
    st.bar_chart(dataframe['field2'])
    st.line_chart(dataframe['field3'])
    st.bar_chart(dataframe['field3'])
    fig = matplotlib.pyplot.figure()
    matplotlib.pyplot.plot(dataframe['field1'])
    st.pyplot(fig)
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)
    st.write(dafra)
    st.line_chart(dafra)
    import altair as alt
    sourc=pd.DataFrame(data_json1['feeds'], columns=['entry_id','field1'])
    st.write(sourc)
    st.altair_chart(alt.Chart(sourc).mark_line().encode(x='entry_id:O',y='field1:N'))
