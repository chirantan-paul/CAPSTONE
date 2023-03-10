import io
import numpy as np
import altair as alt
import pandas as pd
from pandas import json_normalize
import streamlit as st
from urllib.request import urlopen
import json

url1 = "https://thingspeak.com/channels/1995845/feed.json"
url2 = "https://thingspeak.com/channels/1538779/feeds/last.json"
response1 = urlopen(url1)
response2 = urlopen(url2)
data_json1 = json.loads(response1.read())
data_json2 = json.loads(response2.read())

st.title("Welcome To Our Boost Converter Monitoring Online UI")

menu = ["Home", "Analysis"]
choice = st.sidebar.selectbox('Menu',menu)
if(choice=='Home'):
    st.title("Home Section")
    st.write("Click on the Arrow and scroll down to see the current parameters")
    st.json(data_json1,expanded=True)
    st.write(data_json2,expanded=False)
    st.write("Check out Analysis Section for more information")
elif(choice=='Analysis'):
    st.title("Analysis Section")
    st.write("Data Table")
    dataframe=pd.DataFrame(data_json1['feeds'], columns=['entry_id','field1','field2','field3'])
    st.write(json_normalize(data_json1['feeds']))
    st.write(dataframe)
    st.write("Line Chart for Voltage")
    st.altair_chart(alt.Chart(dataframe).mark_line(color='yellow').encode(x=alt.X('entry_id:O',axis=alt.Axis(labelAngle=-90)),y='field1:Q').interactive(),use_container_width=True)
    st.write("Line Chart for Current")
    st.altair_chart(alt.Chart(dataframe).mark_line(color='red').encode(x='entry_id:O',y='field2:Q').interactive(),use_container_width=True)
    st.write("Line Chart for Power")
    st.altair_chart(alt.Chart(dataframe).mark_line(color='purple').encode(x='entry_id:O',y='field3:Q').interactive(),use_container_width=True)
    
    st.write("Line Chart Comparison of Voltage, Current and Power")
    st.altair_chart(alt.layer(alt.Chart(dataframe).mark_line(color='blue').encode(x='entry_id:O',y='field1:Q').interactive(),
                              alt.Chart(dataframe).mark_line(color='yellow').encode(x='entry_id:O',y='field2:Q').interactive(),
                              alt.Chart(dataframe).mark_line(color='red').encode(x='entry_id:O',y='field3:Q').interactive()),use_container_width=True)
    
    st.write("Area Chart for Voltage")
    st.altair_chart(alt.Chart(dataframe).mark_area(color='orange').encode(x='entry_id:O',y='field1:Q').interactive(),use_container_width=True)
    st.write("Area Chart for Current")
    st.altair_chart(alt.Chart(dataframe).mark_area(color='magenta').encode(x='entry_id:O',y='field2:Q').interactive(),use_container_width=True)
    st.write("Area Chart for Power")
    st.altair_chart(alt.Chart(dataframe).mark_area(color='yellow').encode(x='entry_id:O',y='field3:Q').interactive(),use_container_width=True)
    
    st.write("Bar Chart for Voltage")
    st.altair_chart(alt.Chart(dataframe).mark_bar(color='red').encode(x='entry_id:O',y='field1:Q').interactive(),use_container_width=True)
    st.write("Bar Chart for Current")
    st.altair_chart(alt.Chart(dataframe).mark_bar(color='green').encode(x='entry_id:O',y='field2:Q').interactive(),use_container_width=True)
    st.write("Bar Chart for Power")
    st.altair_chart(alt.Chart(dataframe).mark_bar(color='cyan').encode(x='entry_id:O',y='field3:Q').interactive(),use_container_width=True)
