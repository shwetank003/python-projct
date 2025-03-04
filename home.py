import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px


st.title("Sales Data Report")


st.markdown("This dataset represents synthetic sales data generated for practice purposes only. It is not real-time or based on actual business operations, and should be used solely for educational or testing purposes. The dataset contains information that simulates sales transactions across different products, regions, and customers. Each row represents an individual sale event with various details associated with it.")
st.markdown("Columns in the Dataset:")
st.markdown("1.Product_ID: Unique identifier for each product sold. Randomly generated for practice purposes.")
st.markdown("2.Sale_Date: The date when the sale occurred. Randomly selected from the year 2023.")
st.markdown("3.Sales_Rep: The sales representative responsible for the transaction. The dataset includes five random sales representatives (Alice, Bob, Charlie, David, Eve).")
st.markdown("4. Region: The region where the sale took place. The possible regions are North, South, East, and West")
st.markdown("5.Sales_Amount: The total sales amount for the transaction, including discounts if any. Values range from 100 to 10,000 (in currency units).")
st.markdown("6.Quantity_Sold: The number of units sold in that transaction, randomly generated between 1 and 50.")
st.markdown("7.Product_Category: The category of the product sold. Categories include Electronics, Furniture, Clothing, and Food.")
st.markdown("8.Unit_Cost: The cost per unit of the product sold, randomly generated between 50 and 5000 currency units.")
st.markdown("9.Unit_Price: The selling price per unit of the product, calculated to be higher than the unit cost.")
st.markdown("10.Customer_Type: Indicates whether the customer is a New or Returning customer.")
st.markdown("11.Discount: The discount applied to the sale, randomly chosen between 0% & 30%.")
st.markdown("12.Payment_Method: The method of payment used by the customer (e.g., Credit Card, Cash, Bank Transfer).")
st.markdown("13.Sales_Channel: The channel through which the sale occurred. Either Online or Retail.")
st.markdown("14.Region_and_Sales_Rep: A combined column that pairs the region and sales representative for easier tracking.")
st.markdown("Disclaimer:")
st.markdown("Please note: This data was randomly generated and is intended solely for practice, learning, or testing. It does not reflect real-world sales, customers, or businesses, and should not be considered reliable for any real-time analysis or decision-making.")
