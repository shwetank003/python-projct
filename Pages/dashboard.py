import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px

df = pd.read_csv("sales_data.csv")

st.title('Welcome to Sales Data')

st.dataframe(df)

st.sidebar.header("Filter options")

#Product filter
Prodect = st.sidebar.multiselect('Product',
                                options=df['Region'].unique(),
                                default=df['Region'].unique())

#Sales Amount filter
min_salary,max_salary= st.sidebar.slider('Sales_Amount',
                            min_value=int(df['Sales_Amount'].min()),
                            max_value= int(df['Sales_Amount'].max()),
                            value=(int(df['Sales_Amount'].min()),int(df['Sales_Amount'].max())))



#create a pie chart for Product distribution
st.subheader("Product Distribution")
fig = px.pie(df,names='Product_ID',title="Product Distribution")
st.plotly_chart(fig)


#create a histogram for Product distribution
fig= px.histogram(df,x='Product_ID',title="Product Distribution", nbins=20)
st.plotly_chart(fig)

#Create a bar graph for Product Category in Region
fig= px.bar(df,x='Product_Category',y='Region',title= "Product Category in Region")
st.plotly_chart(fig)

#Line graph for Sales Rep and Unit Price	
fig= px.line(df,x='Sales_Rep',y='Unit_Price', title="Sales Rep and Unit Price")
st.plotly_chart(fig)

#Scatter plot for Sales_Amount and Unit_Cost
fig=px.scatter(df,x='Sales_Amount',y='Unit_Cost',title="Sales Amount and Unit Cost")
st.plotly_chart(fig)

#Box plot Graph for Unit Price
fig=px.box(df,y="Unit_Price")
st.plotly_chart(fig)

#Violin graph for Discount
fig=px.violin(df,y="Discount")
st.plotly_chart(fig)

#Line chart for Sales Amount and Discount
fig=px.line(df,x='Sales_Amount',y='Discount')
st.plotly_chart(fig)

#Violin graph for Sales Amount
fig=px.violin(df,y="Sales_Amount")
st.plotly_chart(fig)

